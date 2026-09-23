---
title: "Bảo vệ dữ liệu cá nhân & Rào chắn truy vấn"
trigger: always_on
version: 5.0
applies_to: [bi_data_analyst, crm_skyjoy_ancillary, performance_growth, trade_distribution_sales]
---

# BẢO VỆ DỮ LIỆU CÁ NHÂN & RÀO CHẮN TRUY VẤN

## 1. Khung pháp lý áp dụng

| Thị trường | Khung | Ghi chú |
|---|---|---|
| Việt Nam | **Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15**, hiệu lực 2026-01-01; nghị định hướng dẫn hiện hành | Tra lại văn bản chính thức trong phiên và để Pháp chế xác nhận cơ sở xử lý, quyền chủ thể, đánh giá tác động và chuyển dữ liệu. [Nguồn luật](https://vanban.chinhphu.vn/?classid=1&docid=214590&orggroupid=1&pageid=27160) |
| Úc | Privacy Act / Australian Privacy Principles (OAIC); Spam Act 2003 (ACMA) | APP3 thu thập tối thiểu · APP5 thông báo · APP7 direct marketing & opt-out · APP8 xuyên biên giới |
| Thái Lan | Personal Data Protection Act B.E. 2562 (2019) và quy định hiện hành | Bản dịch tiếng Anh không phải văn bản có hiệu lực; cần local-current legal review |
| Ấn Độ | Digital Personal Data Protection Act và Rules 2025 | Rules triển khai theo giai đoạn; ghi rõ phase có hiệu lực tại ngày dùng |
| Trung Quốc đại lục | Personal Information Protection Law và quy định liên quan | Chuyển dữ liệu, consent và hoạt động xử lý phải được local counsel rà trên bản tiếng Trung hiện hành |
| EU/EEA (nếu có khách) | GDPR | Cơ sở pháp lý, quyền chủ thể, chuyển dữ liệu |
| Khác | Theo từng thị trường | Xem `skills/vietjet-global-localization/` |

`[CẦN XÁC MINH — Pháp chế]` Số hiệu điều khoản cụ thể, thời hạn phản hồi yêu cầu chủ thể dữ liệu, và mẫu hồ sơ đánh giá tác động phải do Pháp chế cung cấp. Agent **không được** trích số hiệu điều khoản từ trí nhớ.

## 2. Dữ liệu cấm tuyệt đối trong prompt và output

Không bao giờ đưa vào bất kỳ prompt, output, log, hay file nào:
- Họ tên hành khách
- Số CCCD / hộ chiếu / giấy tờ tuỳ thân
- Số thẻ thanh toán, thông tin tài khoản ngân hàng
- Số điện thoại, email cá nhân
- Địa chỉ cư trú
- Lịch sử bay chi tiết của một cá nhân cụ thể
- Bất kỳ dữ liệu nào cho phép truy ngược về một cá nhân khi kết hợp với dữ liệu khác

Phân tích luôn ở mức **tổng hợp** (aggregate). Ngưỡng tối thiểu đề xuất: không xuất ra nhóm có dưới 30 cá nhân — `[CẦN XÁC MINH — Pháp chế + Data]` cho ngưỡng chính thức.

## 3. RÀO CHẮN KỸ THUẬT CHO NL2SQL (BẮT BUỘC)

> Guardrail bằng văn bản không ngăn được `SELECT passenger_name FROM bookings`. Các ràng buộc dưới đây phải được cấu hình ở **tầng kết nối cơ sở dữ liệu**, không chỉ ở tầng prompt.

### 3.1 Cấu hình bắt buộc trước khi bật `nl2sql_query`
1. **Chỉ đọc (read-only).** Tài khoản kết nối không có quyền `INSERT`/`UPDATE`/`DELETE`/`DROP`/`ALTER`/`GRANT`.
2. **Read-replica, không phải production.** Truy vấn phân tích không chạm cơ sở dữ liệu đang phục vụ đặt vé.
3. **Danh sách bảng/view được phép (allow-list).** Agent chỉ thấy các view đã được chuẩn bị sẵn, đã loại bỏ cột PII ở tầng view — không cấp quyền trên bảng gốc.
4. **Loại trừ cột PII ở tầng cơ sở dữ liệu.** Các cột định danh không tồn tại trong view mà agent truy cập được.
5. **Giới hạn số dòng** mặc định (đề xuất `LIMIT 10000`) và **timeout truy vấn**.
6. **Log toàn bộ truy vấn** kèm thời gian, agent, và người yêu cầu — phục vụ hậu kiểm.
7. **Chặn `SELECT *`** — buộc liệt kê cột tường minh.

`[CẦN XÁC MINH — Data Engineering]` Xác nhận bằng văn bản rằng 7 mục trên đã được cấu hình trước khi agent BI được phép chạy trên dữ liệu thật.

### 3.2 Hành vi của agent
- Trước khi chạy truy vấn đầu tiên trong phiên, agent nêu rõ đang kết nối tới nguồn nào và ở chế độ gì.
- Nếu một câu hỏi chỉ trả lời được bằng dữ liệu cá nhân, agent **từ chối và đề xuất câu hỏi ở mức tổng hợp** thay thế.
- Nếu không có kết nối, nói rõ ngay từ đầu và gắn `[SỐ LIỆU MINH HỌA]` cho toàn bộ output.

## 4. CRM & marketing trực tiếp

- Mọi liên hệ marketing cần **cơ sở pháp lý rõ ràng** (đồng ý, hoặc cơ sở khác được pháp luật thị trường đó cho phép).
- **Preference centre** và **unsubscribe** bắt buộc ở mọi kênh, xử lý trong thời hạn luật định của từng thị trường.
- Không cá nhân hoá **giá** theo dữ liệu cá nhân. Cá nhân hoá **thông điệp, ngôn ngữ, đề xuất tuyến** thì được.
- Segment mới hoặc kênh mới = hoạt động xử lý dữ liệu mới = One-Way Door, cần Pháp chế duyệt.

## 5. Lưu trữ & xoá

`[CẦN XÁC MINH — Pháp chế + IT]` Thời hạn lưu trữ cho: log truy vấn agent · output chứa dữ liệu tổng hợp · dữ liệu chiến dịch · bản nháp có gắn cờ. Không lưu vô thời hạn.

## 6. Sự cố dữ liệu

Nếu agent phát hiện PII đã lọt vào một output, prompt, hoặc file: **dừng ngay, không tiếp tục xử lý, báo người dùng và bộ phận phụ trách dữ liệu.** Không tự ý xoá dấu vết — sự cố dữ liệu có thể phát sinh nghĩa vụ thông báo theo luật.

<!-- check-output: rules-doc -->
