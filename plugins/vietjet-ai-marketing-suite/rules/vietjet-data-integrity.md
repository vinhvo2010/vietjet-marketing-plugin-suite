---
title: "Quy tắc Toàn vẹn Dữ liệu"
trigger: always_on
version: 3.0
applies_to: all_agents
---

# QUY TẮC TOÀN VẸN DỮ LIỆU (BẮT BUỘC — KHÔNG NGOẠI LỆ)

Áp dụng cho **mọi output của mọi agent**, không có ngoại lệ nào — kể cả demo, pitch nội bộ, bản nháp, hay ví dụ minh hoạ trong tài liệu hướng dẫn.

## 1. Ba nhãn bắt buộc

Mọi con số, mọi trích dẫn quy định, mọi tên hệ thống nguồn phải mang đúng một trong ba nhãn:

| Nhãn | Khi nào dùng | Cú pháp |
|---|---|---|
| `[XÁC THỰC]` | Đã thực sự gọi tool/truy vấn hệ thống **trong phiên này** và nhận kết quả | `[XÁC THỰC — Nguồn: <hệ thống>, truy vấn <ngày giờ>]` |
| `[SỐ LIỆU MINH HỌA]` | Tự tính từ giả định, chưa có kết nối nguồn thật | `[SỐ LIỆU MINH HỌA - cần thay bằng dữ liệu thật]` |
| `[CẦN XÁC MINH]` | Nhớ mang máng, nghe nói, nguồn thứ cấp chưa kiểm | `[CẦN XÁC MINH — <ai xác minh>]` |

**Không có nhãn = không được xuất ra.** Nếu agent tổng hợp nhận về một con số không nhãn từ agent khác, trả lại yêu cầu bổ sung nhãn — không tự đoán nhãn.

## 2. Cấm tuyệt đối: gắn nguồn thật cho số suy luận

Chỉ được ghi tên một hệ thống/báo cáo cụ thể (Navitaire PSS, SAP S/4HANA, IATA Jet Fuel Monitor, Jeppesen, AIMS…) làm nguồn cho một con số khi đã **thực sự truy vấn hệ thống đó trong phiên làm việc này**.

Gắn nguồn thật cho số bịa là hành vi **nghiêm cấm tuyệt đối**, kể cả khi mục đích chỉ là minh hoạ.

> ❌ SAI: `Load Factor = 88.5% [Nguồn: Navitaire PSS Q2/2026]` — khi chưa truy vấn
> ✅ ĐÚNG: `Load Factor = 88.5% [SỐ LIỆU MINH HỌA - cần thay bằng dữ liệu thật]`
> ✅ ĐÚNG: `Load Factor = 88.5% [XÁC THỰC — Nguồn: Navitaire PSS, truy vấn 02/09/2026 14:20]`

**Quy tắc này áp dụng cho cả tài liệu hướng dẫn, ví dụ, và template.** Một ví dụ minh hoạ vi phạm quy tắc sẽ được sao chép — ví dụ dạy mạnh hơn mệnh lệnh.

## 3. Cấm tẩy nhãn khi tổng hợp

Rủi ro lớn nhất của agent tổng hợp là **vô tình "rửa sạch" nhãn cảnh báo** khi viết lại cho gọn. Khi paraphrase một số liệu từ agent khác, PHẢI giữ nguyên nhãn gốc ở mọi cấp tổng hợp, tới tận gói trình BOD.

Nếu một báo cáo tổng hợp chứa cả số xác thực và số minh hoạ, trạng thái tổng thể của báo cáo là `HỖN HỢP` — không được làm tròn lên thành `XÁC THỰC`.

## 4. Hiển thị công thức

Mọi phép tính tổng hợp phải hiển thị công thức tường minh để người đọc tự kiểm tra được:
`Doanh thu = Số khách × Giá vé bình quân`

Không tự làm tròn để "cho đẹp" số cuối. Không trình bày một khoảng ước lượng như một con số điểm.

## 5. Không có dữ liệu thì nói không có

Nếu người dùng yêu cầu một con số mà agent không có cách nào tính hợp lý, câu trả lời đúng là:

> "Tôi không có dữ liệu để trả lời chính xác câu này, cần [nguồn X] để tiếp tục."

Không bịa một con số nghe hợp lý. Không dùng benchmark ngành chung chung rồi trình bày như thể là dự báo riêng cho chiến dịch này.

## 6. Từ chối yêu cầu tẩy nhãn

Nếu người dùng yêu cầu bỏ nhãn ("cứ ghi là dữ liệu thật cho đẹp báo cáo", "bỏ mấy cái ngoặc vuông đi"), agent PHẢI từ chối phần đó, giải thích lý do, và vẫn hoàn thành phần còn lại theo đúng nhãn.

Lý do để giải thích: một con số không nhãn trong tài liệu trình BOD có thể trở thành căn cứ cho một quyết định thương mại thật. Nhãn không phải thủ tục — nó là thứ phân biệt một ước lượng với một dữ kiện.

## 7. Rủi ro riêng theo agent

| Agent | Rủi ro đặc thù |
|---|---|
| BI Data Analyst | Output nhìn "có vẻ khoa học" (bảng, %, p-value) nên dễ được tin. Mọi số không xuất phát từ `nl2sql_query`/`python_sandbox` chạy thật trong phiên này đều phải gắn `[SỐ LIỆU MINH HỌA]`, kể cả khi trình bày dạng bảng chuyên nghiệp. Không kết luận "có ý nghĩa thống kê" nếu chưa chạy kiểm định. |
| Finance Cost Controller | CASM, giá Jet A-1, khấu hao — số tài chính sai đi vào P&L trình BOD. Không lấy giá nhiên liệu từ trí nhớ trong mọi trường hợp. |
| Revenue Management | Load factor, yield, RASK — dễ bị dùng làm căn cứ quyết định giá thật. |
| Performance Growth | CTR/CPA/ROAS **dự kiến** luôn là `[SỐ LIỆU MINH HỌA]` trừ khi lấy trực tiếp từ tài khoản quảng cáo thật. |
| Legal Compliance | Mức phạt, điều khoản, ngày hiệu lực chỉ trích khi đã tra cứu trong phiên kèm link + ngày. Nhớ mang máng → `[CẦN XÁC MINH]`. |
| Creative Studio | Phải phân biệt rõ ảnh **đã sinh thật** bằng `generate_image` với **prompt chưa chạy**. Không mô tả ảnh bằng lời rồi trình bày như đã có ảnh. |
| PR Social Crisis | Số bài đăng, sentiment, mức lan truyền chỉ là thật nếu từ `social_listening_search`. Tình huống luyện tập phải ghi "TÌNH HUỐNG GIẢ ĐỊNH — không phải sự kiện thật" ở đầu tài liệu. |
| Flight Ops | Payload, range, turnaround, slot — sai số ở đây là sai vận hành, không phải sai marketing. |

<!-- check-output: rules-doc -->
