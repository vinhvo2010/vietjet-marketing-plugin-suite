---
title: "Vietjet AI Marketing — Rules Index"
trigger: always_on
version: 5.0
---

# TẦNG QUY CHUẨN (RULES LAYER)

Mọi agent và skill trong hệ thống Vietjet AI Marketing PHẢI tuân thủ toàn bộ tầng này. Đây là nguồn sự thật duy nhất — agent KHÔNG được lặp lại nội dung các file này trong file của mình, chỉ tham chiếu. Khi có mâu thuẫn giữa agent/skill và rules, **rules thắng**.

| File | Nội dung | Ai phải đọc |
|---|---|---|
| `vietjet-group-marketing-operating-model.md` | North Star, dual demand engine, airline retail loop, hub/chapter/pod | **Toàn bộ 18 agent — bắt buộc mọi phiên** |
| `vietjet-agent-collaboration.md` | Dependency waves, handoff contract, reviewer độc lập | **Toàn bộ 18 agent — bắt buộc mọi phiên** |
| `vietjet-data-integrity.md` | Quy tắc toàn vẹn dữ liệu, chống bịa số, nhãn nguồn | **Toàn bộ 18 agent — bắt buộc mọi phiên** |
| `vietjet-governance-gates.md` | One-Way / Two-Way Door, thẩm quyền phê duyệt, hạn mức chi tiêu | Toàn bộ 18 agent |
| `vietjet-brand-safety.md` | Nhận diện thương hiệu, chuẩn thể hiện hình người, nội dung cấm | Creative, Performance, PR, CRM, Localization |
| `vietjet-data-protection.md` | PII, khung privacy theo thị trường, rào chắn kỹ thuật NL2SQL | BI, CRM, Performance, Trade, CX, MarTech, Market Pod |
| `vietjet-source-and-expiry.md` | Đăng ký nguồn, hạn dùng dữ liệu, đội tàu (nguồn sự thật duy nhất) | Market Intelligence, Revenue, Finance, Flight Ops, Creative |
| `vietjet-delivery-standard.md` | Outcome, evidence ledger, quality gate và hợp đồng bàn giao | **Toàn bộ agent và skill** |

## Nguyên tắc nền

1. **Không có số nào không có nhãn.** Xem `vietjet-data-integrity.md`.
2. **Không tự đi qua cổng người.** Xem `vietjet-governance-gates.md`.
3. **An toàn bay không bao giờ là chủ đề marketing.** Mọi nội dung chạm tới an toàn, sự cố, tai nạn → dừng, chuyển `vietjet_pr_social_crisis`, chờ người.
4. **Không biết thì nói không biết.** Câu trả lời đúng khi thiếu dữ liệu là "Tôi không có dữ liệu để trả lời chính xác câu này, cần [nguồn X]" — không phải một con số nghe hợp lý.
5. **Khi nghi ngờ, dừng lại và hỏi người.** Chi phí của một lần hỏi thừa nhỏ hơn nhiều chi phí của một lần sai trong ngành hàng không.
6. **Không kết thúc ở ý tưởng.** Mỗi nhiệm vụ phải có trạng thái bàn giao, bằng chứng, cổng duyệt và hành động tiếp theo theo `vietjet-delivery-standard.md`.

## Về các dấu [CẦN XÁC MINH]

Tầng rules này ghi rõ những chỗ cần Pháp chế / An toàn / Tài chính xác nhận bằng văn bản nội bộ thay vì điền số hiệu văn bản pháp lý từ trí nhớ. **Đây là hành vi đúng, không phải thiếu sót.** Điền một số hiệu thông tư sai vào tài liệu governance nguy hiểm hơn để trống có đánh dấu.

<!-- check-output: rules-doc -->
