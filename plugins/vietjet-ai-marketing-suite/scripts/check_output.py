#!/usr/bin/env python3
"""
check_output.py — Kiểm tra tự động output của hệ thống Vietjet AI Marketing.

Quét một file (hoặc thư mục) và bắt bốn loại lỗi mà tầng rules cấm:

  1. HALLUCINATION  — con số đứng cạnh tên hệ thống nguồn thật mà không có nhãn XÁC THỰC
  2. UNLABELED      — con số tài chính/hiệu suất không mang nhãn nào
  3. BRAND          — từ khoá vi phạm chuẩn thể hiện con người hoặc guardrail thương hiệu
  4. GATE           — nội dung One-Way Door mà thiếu cờ chờ phê duyệt

Dùng:
    python3 check_output.py <file_hoặc_thư_mục> [--strict]

Mã thoát: 0 = sạch · 1 = có BLOCK · 2 = chỉ có WARN (với --strict thì cũng trả 1)

Lưu ý: script này bắt các mẫu văn bản. Nó KHÔNG thay thế người duyệt —
nó chỉ đảm bảo những lỗi đã biết không lọt qua lần nữa.
"""

import re
import sys
import os

# --- Tên hệ thống nguồn thật: nếu xuất hiện cạnh số mà không có nhãn XÁC THỰC -> BLOCK
SOURCE_SYSTEMS = [
    "navitaire", "sap", "s/4hana", "s4hana", "iata jet fuel", "jet fuel monitor",
    "platts", "jeppesen", "aims", "amadeus", "sabre", "ndc api", "b2b agent portal",
    "meta ads", "google ads", "tiktok ads", "ga4", "google analytics",
]

LABEL_VERIFIED = re.compile(r"\[XÁC THỰC", re.I)
LABEL_ILLUSTRATIVE = re.compile(r"\[SỐ LIỆU MINH HỌA", re.I)
LABEL_TOVERIFY = re.compile(r"\[CẦN XÁC MINH", re.I)
ANY_LABEL = re.compile(r"\[(XÁC THỰC|SỐ LIỆU MINH HỌA|CẦN XÁC MINH|CHƯA XÁC MINH|DECISION REQUIRED)", re.I)

# Con số có vẻ là chỉ số tài chính/hiệu suất
METRIC_NUMBER = re.compile(
    r"(?:^|[\s=:(])"
    r"(?:\$|USD|VND|A\$|đ\s)?\s?"
    r"\d{1,3}(?:[.,]\d{3})*(?:[.,]\d+)?"
    r"\s?(?:%|đ|USD|VND|tỷ|triệu|/barrel|/pax|/khách|/chuyến)?",
    re.I,
)

METRIC_CONTEXT = re.compile(
    r"(load factor|yield|rask|cask|casm|ctr|cpa|cpc|roas|contribution|"
    r"doanh thu|chi phí|lợi nhuận|p&l|break-even|hoà vốn|hòa vốn|"
    r"attach rate|conversion|tỷ lệ chuyển đổi|ancillary|giá vé|fare|"
    r"jet fuel|nhiên liệu|tần suất|thị phần|market share)",
    re.I,
)

# --- Brand safety: chuẩn thể hiện con người + guardrail
BRAND_BLOCK = {
    r"\bbikini\b": "Vi phạm chuẩn thể hiện con người (rules/vietjet-brand-safety.md §2.2)",
    r"\bswimsuit\b": "Vi phạm chuẩn thể hiện con người",
    r"\bsexy\b": "Vi phạm chuẩn thể hiện con người",
    r"\bseductive\b": "Vi phạm chuẩn thể hiện con người",
    r"\balluring\b": "Vi phạm chuẩn thể hiện con người",
    r"\bcurvy\b": "Vi phạm chuẩn thể hiện con người",
    r"\brevealing\b": "Vi phạm chuẩn thể hiện con người",
    r"low[- ]angle": "Góc máy từ dưới lên với chủ thể người — cấm (§2.1)",
    r"\bcleavage\b": "Vi phạm chuẩn thể hiện con người",
}

BRAND_WARN = {
    r"\bcheapest\b|\brẻ nhất\b": "Claim so sánh tuyệt đối — cần substantiation",
    r"\bkhông bao giờ\b|\bwe will never\b": "Cam kết tuyệt đối — dùng 'We will not knowingly…'",
    r"\bguaranteed on[- ]time\b|\bcam kết đúng giờ\b": "Cam kết SLA cần Ops/Legal/Finance xác nhận",
    r"\btuyến không thể sai\b|\bcan't-miss route\b": "Không kết luận route economics khi thiếu dữ liệu",
    r"\bearned media value\b": "Không dùng làm KPI thành công chính (§guardrail)",
    r"nguyên nhân (?:là|do|được cho là)": "Có thể đang nêu nguyên nhân sự cố — kiểm tra crisis-shield §4.3",
}

# --- One-Way Door: nội dung cần cờ duyệt
GATE_TRIGGERS = {
    r"hoàn (?:tiền|vé)|bồi thường|đổi vé miễn phí|refund|compensation": "Cam kết với khách hàng (§2.2)",
    r"an toàn bay|sự cố|tai nạn|incident|accident": "An toàn bay (§2.1)",
    r"thông cáo báo chí|press release": "Nội dung công bố (§2.4)",
    r"\bp&l\b|lợi nhuận trình|trình ban giám đốc": "Số liệu tài chính trình BOD (§2.4)",
    r"bật (?:chi tiêu|ngân sách)|kích hoạt chi tiêu|launch campaign spend": "Tiền thật (§2.3)",
}

GATE_FLAG = re.compile(
    r"(CẦN NGƯỜI PHÊ DUYỆT|BẢN NHÁP|CHƯA PHÁT HÀNH|CHỜ DUYỆT|⚠️)", re.I
)


# --- Ngữ cảnh CẤM: dòng đang cấm một từ khoá, không phải đang dùng nó
PROHIBITION_CONTEXT = re.compile(
    r"(KHÔNG\s|KHONG\s|cấm|Cấm|CẤM|không được|không bao giờ|tuyệt đối|"
    r"vi phạm|Vi phạm|VI PHẠM|--no\b|❌|\bnever\b|\bavoid\b|\bdo not\b|"
    r"không dùng|không nêu|không cam kết|không công bố|phải từ chối|"
    r"ngôn ngữ đúng|thay bằng|dùng thay|SAI:|ĐÚNG:)",
    re.I,
)

# File tự khai báo là tài liệu định nghĩa quy tắc -> bỏ qua BRAND/GATE
OPT_OUT = re.compile(r"<!--\s*check-output:\s*rules-doc\s*-->")


class Finding:
    def __init__(self, level, code, line_no, line, msg):
        self.level, self.code = level, code
        self.line_no, self.line, self.msg = line_no, line.strip(), msg

    def __str__(self):
        icon = "🛑" if self.level == "BLOCK" else "⚠️"
        snippet = self.line[:100] + ("…" if len(self.line) > 100 else "")
        return f"{icon} [{self.code}] dòng {self.line_no}: {self.msg}\n     → {snippet}"


def check_text(text):
    findings = []
    lines = text.split("\n")
    has_gate_flag = bool(GATE_FLAG.search(text))
    is_rules_doc = bool(OPT_OUT.search(text))
    frontmatter_end = 0
    if lines and lines[0].strip() == "---":
        for index, value in enumerate(lines[1:], 1):
            if value.strip() == "---":
                frontmatter_end = index
                break

    for i, line in enumerate(lines, 1):
        # Metadata describes the document; it is not campaign output.
        if i <= frontmatter_end + 1:
            continue
        low = line.lower()

        # 1. HALLUCINATION — tên hệ thống + số, không có nhãn XÁC THỰC
        for sysname in SOURCE_SYSTEMS:
            if sysname in low and METRIC_NUMBER.search(line) and not is_rules_doc:
                if not LABEL_VERIFIED.search(line) and not PROHIBITION_CONTEXT.search(line):
                    findings.append(Finding(
                        "BLOCK", "HALLUCINATION", i, line,
                        f"Số liệu đứng cạnh nguồn thật '{sysname}' nhưng thiếu nhãn [XÁC THỰC — Nguồn, ngày]. "
                        f"Đây là lỗi bị cấm tuyệt đối (rules/vietjet-data-integrity.md §2)."))
                break

        # 2. UNLABELED — chỉ số tài chính/hiệu suất không nhãn
        if METRIC_CONTEXT.search(line) and METRIC_NUMBER.search(line):
            if (not ANY_LABEL.search(line) and not is_rules_doc
                    and not line.strip().startswith(("|", "#", ">", "-", "*", "1.", "2.", "3.", "4.", "5.", "6.", "7."))):
                findings.append(Finding(
                    "WARN", "UNLABELED", i, line,
                    "Chỉ số không mang nhãn dữ liệu. Cần [XÁC THỰC] / [SỐ LIỆU MINH HỌA] / [CẦN XÁC MINH]."))

        # Dòng đang CẤM một từ khoá thì không tính là vi phạm
        prohibiting = bool(PROHIBITION_CONTEXT.search(line)) or is_rules_doc

        # 3. BRAND
        if not prohibiting:
            for pat, msg in BRAND_BLOCK.items():
                if re.search(pat, low):
                    findings.append(Finding("BLOCK", "BRAND", i, line, msg))
            for pat, msg in BRAND_WARN.items():
                if re.search(pat, low):
                    findings.append(Finding("WARN", "BRAND", i, line, msg))

        # 4. GATE
        if not has_gate_flag and not is_rules_doc and not prohibiting:
            for pat, msg in GATE_TRIGGERS.items():
                if re.search(pat, low):
                    findings.append(Finding(
                        "BLOCK", "GATE", i, line,
                        f"Nội dung One-Way Door ({msg}) nhưng tài liệu KHÔNG có cờ chờ phê duyệt. "
                        f"Thêm '⚠️ BẢN NHÁP — CHƯA PHÁT HÀNH — CẦN NGƯỜI PHÊ DUYỆT' ở dòng đầu."))
                    break
    return findings


def check_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"Không đọc được {path}: {e}")
        return []
    findings = check_text(text)
    if findings:
        print(f"\n{'='*70}\n📄 {path}\n{'='*70}")
        for f_ in findings:
            print(f_)
    return findings


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    strict = "--strict" in sys.argv
    if not args:
        print(__doc__)
        return 0

    target = args[0]
    paths = []
    if os.path.isdir(target):
        for root, _, files in os.walk(target):
            paths += [os.path.join(root, f) for f in files if f.endswith(".md")]
    else:
        paths = [target]

    all_f = []
    for p in sorted(paths):
        all_f += check_file(p)

    blocks = [f for f in all_f if f.level == "BLOCK"]
    warns = [f for f in all_f if f.level == "WARN"]

    print(f"\n{'='*70}")
    print(f"Đã quét {len(paths)} file · 🛑 {len(blocks)} BLOCK · ⚠️  {len(warns)} WARN")
    if not all_f:
        print("✅ Không phát hiện vi phạm mẫu đã biết.")
    print("\nLưu ý: script bắt mẫu văn bản, KHÔNG thay thế người duyệt.")
    print(f"{'='*70}")

    if blocks:
        return 1
    if warns:
        return 1 if strict else 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
