---
title: "Đăng ký nguồn, hạn dùng dữ liệu & Đội tàu"
trigger: always_on
version: 5.0
---

# ĐĂNG KÝ NGUỒN, HẠN DÙNG DỮ LIỆU & ĐỘI TÀU

## 1. Quy tắc hết hạn dữ liệu

Dữ liệu đúng hôm qua có thể sai hôm nay. Mọi dữ kiện dùng trong output đối ngoại phải kèm **ngày kiểm chứng**. Không có ngày = coi như chưa kiểm chứng.

Tra cứu chính sách/sản phẩm Vietjet bắt đầu ở `../research/official-vietjet-sources.json`; đọc hướng dẫn tại `../research/official-vietjet-sources.md`. Sổ chứa snapshot nguồn công khai, ngày kiểm tra, ngày hiệu lực được xác minh, phạm vi và ngữ cảnh cần có. `reviewAfter` là hạn kiểm lại của dự án; `approvedForPublic` là rà soát nguồn công khai, không phải phê duyệt doanh nghiệp. Quá hạn hoặc không đọc lại được nguồn thì ghi rõ chưa xác minh hiện tại, không suy ra quyền lợi của vé cụ thể.

| Loại dữ liệu | Hạn dùng | Quá hạn thì |
|---|---|---|
| Giá vé & tần suất đối thủ | **30 ngày** | Phải tra lại trước mọi claim so sánh công khai. Dùng số quá hạn trong quảng cáo là rủi ro pháp lý (gây hiểu nhầm), không chỉ rủi ro chính xác |
| Giá nhiên liệu Jet A-1 | **7 ngày** | Tra lại; không bao giờ lấy từ trí nhớ |
| Tỷ giá | **1 ngày** | Tra lại |
| Load factor / booking curve | **Theo kỳ báo cáo** | Ghi rõ kỳ dữ liệu, không dùng kỳ cũ như hiện tại |
| Quy định pháp luật | **Mỗi quý** | Luật thay đổi; tra lại kèm link + ngày |
| Slot bay, lịch khai thác | **Theo mùa IATA** | Đổi mùa là đổi dữ liệu |
| Danh sách đối thủ & cấu trúc thị trường | **6 tháng** | Thị trường hàng không biến động nhanh; xác minh lại hãng nào còn khai thác |
| Lịch lễ hội / mùa vụ | **Mỗi quý** | Xác nhận ngày với nguồn chính thức |
| Chính sách Vietjet trong sổ nguồn | **Theo `reviewAfter` từng thẻ (khởi tạo 7 ngày)** | Tra lại trước cam kết cụ thể hoặc phát hành; hạn này không chứng minh chính sách chưa thay đổi |

## 2. Danh sách đối thủ — cần xác minh lại

`[CẦN XÁC MINH — Market Intelligence]` Danh sách đối thủ trong tài liệu v2 (Vietnam Airlines, Bamboo, AirAsia, Scoot…) chưa kèm ngày kiểm chứng. Bối cảnh hãng bay nội địa Việt Nam đã biến động đáng kể — **phải xác minh lại hãng nào còn đang khai thác, trên tuyến nào, trước khi dùng danh sách này cho bất kỳ phân tích nào.**

Không agent nào được dùng danh sách đối thủ mà không có ngày kiểm chứng đi kèm.

## 3. ĐỘI TÀU — NGUỒN SỰ THẬT DUY NHẤT

Bản v2 có ba mô tả đội tàu khác nhau ở ba file. Đây là nguồn duy nhất; mọi file khác tham chiếu về đây.

`[CẦN XÁC MINH — Flight Ops / Network Planning]` Chưa có sổ đội tàu theo hãng khai thác, đường bay và ngày bay được Ops xác nhận trong plugin. Không dùng bảng định hướng bên dưới làm bằng chứng cho loại tàu, cấu hình hoặc số lượng đang khai thác:

| Thực thể khai thác | Đội tàu | Ghi chú |
|---|---|---|
| Vietjet Air (Việt Nam) | `[CẦN XÁC MINH]` | Ops xác nhận loại tàu/cấu hình của chặng và ngày bay |
| Thai Vietjet hoặc hãng đối tác thực khai thác | `[CẦN XÁC MINH]` | Dùng tên hãng khai thác trên vé và nguồn chính thức tương ứng |

Không suy ra có một hãng Vietjet nội địa tại Australia hoặc gán loại tàu từ tên thị trường. Đường bay đến/đi Australia là phạm vi hành trình, không tự tạo ra pháp nhân khai thác mới.

**Quy tắc cứng:** loại tàu xuất hiện trong Key Visual, trong bài đăng, hoặc trong tính toán payload/range **phải khớp với loại tàu thực khai thác trên đúng đường bay đó**. Creative Studio phải hỏi Flight Ops khi không chắc, không tự chọn.

## 4. Ranh giới giữa các thực thể Vietjet

Hệ thống hỗ trợ nghiên cứu/soạn nháp về **Vietjet Air (Việt Nam & quốc tế)**; tên thương hiệu không chứng minh plugin được quyền đại diện hãng. Nếu yêu cầu liên quan một hãng khai thác khác đã được xác minh, hãng đó có thể có:
- đội tàu khác, AOC khác, khung pháp lý khác;
- có thể có bộ agent/guardrail riêng.

**Không trộn dữ kiện giữa các thực thể.** Khi một yêu cầu chạm tới thực thể khác, agent phải nêu rõ ranh giới và hỏi lại thay vì giả định. Rủi ro nhầm lẫn thương hiệu giữa hai thực thể cùng nhận diện là rủi ro pháp lý và vận hành thật.

Với chuyến liên danh, đọc thẻ `vietjet-codeshare-guidance-vi`; hãng bán vé và hãng khai thác có thể khác nhau. Với điều lệ Vietjet, tham chiếu thẻ `vietjet-conditions-of-carriage-vi` và ưu tiên bản tiếng Việt theo chính điều lệ. Nguồn IATA/gstack trong nghiên cứu là căn cứ tham khảo thiết kế, không chứng nhận plugin đáp ứng tiêu chuẩn ngành hoặc được Vietjet/YC chứng thực.

## 5. Cú pháp gắn nguồn chuẩn

```
[Chỉ số] = [Giá trị] [XÁC THỰC — Nguồn: <hệ thống>, kỳ dữ liệu <kỳ>, truy vấn <ngày>]
[Chỉ số] = [Giá trị] [SỐ LIỆU MINH HỌA - cần thay bằng dữ liệu thật]
[Quy định] [CẦN XÁC MINH — Pháp chế]
```

Nguồn thứ cấp (báo chí, blog ngành) phải gắn nhãn "Nguồn thứ cấp — cần kiểm chứng" và không bao giờ được dùng làm căn cứ duy nhất cho một quyết định thương mại hoặc một claim công khai.

## 6. Bảng đăng ký nguồn hệ thống

| Loại dữ liệu | Hệ thống nguồn | Tool | Trạng thái kết nối |
|---|---|---|---|
| Đặt vé, load factor, booking curve | Navitaire PSS / RMS | `nl2sql_query` | `[CẦN XÁC MINH]` |
| Tài chính, chi phí, P&L | SAP S/4HANA | | `[CẦN XÁC MINH]` |
| Giá nhiên liệu Jet A-1 | IATA Jet Fuel Monitor / Platts | | `[CẦN XÁC MINH]` |
| Lịch bay, slot, đội tàu | Jeppesen / AIMS | | `[CẦN XÁC MINH]` |
| Quảng cáo | Meta / Google / TikTok Ads API | `query_ads_platform` | `[CẦN XÁC MINH]` |
| Kênh B2B/OTA | B2B Agent Portal / NDC API | | `[CẦN XÁC MINH]` |
| Social listening | | `social_listening_search` | `[CẦN XÁC MINH]` |
| Pháp lý | CAAV, ACCC, DGCA, IATA | `web_search` / `query_legal_db` | Công khai |

Agent chỉ được ghi tên hệ thống ở cột 2 làm nguồn khi cột "Trạng thái kết nối" là đã kết nối **và** đã thực sự truy vấn trong phiên.

<!-- check-output: rules-doc -->
