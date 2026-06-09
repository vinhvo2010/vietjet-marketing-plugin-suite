# PHƯƠNG ÁN ĐO LƯỜNG VÀ ĐÁNH GIÁ (MEASUREMENT WORKSHEET)
**Chiến dịch:** BAY TỚI MÙA HÈ BÓNG ĐÁ (Hè 2026)  
**Trạng thái tài liệu:** DỰ THẢO PHƯƠNG ÁN ĐO LƯỜNG NỘI BỘ (INTERNAL WORKING DRAFT) - KHÔNG PHẢI KHUNG BÁO CÁO ĐÃ PHÊ DUYỆT - KHÔNG PHẢI MÔ HÌNH ROI CUỐI CÙNG

---

### 1. Trạng thái tài liệu (Document Status)
*   **Mục đích:** Tài liệu phác thảo và hướng dẫn kỹ thuật thiết lập hệ thống thu thập dữ liệu đo lường.
*   **Giá trị pháp lý:** KHÔNG đại diện cho khung báo cáo chính thức, KHÔNG đại diện cho mô hình đo lường hiệu quả đầu tư (ROI model) được cam kết bởi Vietjet.

---

### 2. Mục tiêu đo lường (Measurement Purpose)
Để tránh các báo cáo phóng đại hiệu quả chiến dịch, tài liệu này phân tách rõ ràng 7 tầng hiệu suất từ truyền thông đến kết quả kinh doanh thực tế:
1.  **Nhận diện (Awareness):** Đo lường mức độ tiếp cận thương hiệu.
2.  **Tương tác (Engagement):** Đo lường sự phản hồi tự nhiên của cộng đồng.
3.  **Lưu lượng (Traffic):** Lượng truy cập thực tế trỏ về app/website.
4.  **Ý định mua vé (Booking Intent):** Số lượng người thực sự gõ tìm kiếm chuyến bay trên hệ thống. Governance: requires validation; not approved target; not forecast; do not use externally; evidence required.
5.  **Đặt vé gộp (Gross Bookings):** Tổng số giao dịch vé phát sinh có gắn tag chiến dịch. Governance: requires validation; not approved target; not forecast; do not use externally; evidence required.
6.  **Doanh thu gộp (Gross Revenue):** Tổng giá trị giao dịch gộp phát sinh có gắn tag. Governance: requires validation; not approved target; not forecast; do not use externally; evidence required.
7.  **Doanh thu tăng thêm (Incremental Revenue):** Giá trị doanh thu tăng thêm thực tế sau khi đã loại trừ lượng đặt vé tự nhiên (organic) bằng nhóm kiểm chứng. Governance: requires validation; not approved target; not forecast; do not use externally; evidence required.

---

### 3. Nguyên tắc đo lường (Measurement Principles)
- **Doanh thu gộp khác Doanh thu tăng thêm:** Doanh thu gộp (Gross Revenue) không đại diện cho doanh thu tăng thêm thực tế (Incremental Revenue) do chiến dịch tạo ra.
- **Yêu cầu đối chứng:** Tuyên bố về Doanh thu tăng thêm bắt buộc phải có Baseline lịch sử và thiết kế nhóm kiểm chứng (control/holdout group) hợp lệ.
- **Giới hạn tuyên bố:** Không đưa ra bất kỳ tuyên bố hiệu quả hoạt động ra bên ngoài khi chưa được đối chiếu và xác thực bằng dữ liệu hệ thống thực tế của Vietjet.
- **Giới hạn ROI:** Không báo cáo tỷ lệ hoàn vốn đầu tư (ROI/ROAS) khi chưa có sự đối khớp chính thức giữa chi phí thực tế phát sinh và doanh thu thực tế được kiểm toán.

---

### 4. Bảng phân loại chỉ số đánh giá (KPI Taxonomy)

| Phân nhóm KPI | Tên KPI | Định nghĩa (Definition) | Công thức (Formula) | Nguồn dữ liệu (Data Source) | Bộ phận xác thực | Giới hạn tuyên bố (Claim Boundary) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Awareness** | Reach | Số người dùng duy nhất tiếp xúc với chiến dịch ít nhất 1 lần | Theo thuật toán đếm của nền tảng | Meta Ads Manager, TikTok Ads Manager | Media Agency | Chỉ dùng làm dữ liệu quảng cáo truyền thông |
| **Engagement** | Engagement Rate | Tỷ lệ tương tác trên lượt hiển thị | Tổng tương tác / Impressions | Meta / TikTok Ads Manager | Media Agency | Chỉ dùng nội bộ |
| **Traffic** | Landing Sessions | Số lượt truy cập thành công trang landing hoặc mở app | Lượt tải trang thành công | Google Analytics, Firebase | Analytics Team | Chỉ phản ánh lượng click-through |
| **Booking Intent**| Search Sessions | Số lượt thực hiện tìm kiếm chuyến bay | Số sự kiện "search_flight" phát sinh | Web/App tracking log | Analytics Team | Đo lường mức độ quan tâm thương mại |
| **Booking** | Gross Bookings | Tổng số lượt đặt vé thành công có gắn tag quảng cáo | Tổng số mã đặt vé (PNR) thành công | Booking Engine Database | Revenue Team | Báo cáo gộp, không tương ứng với incremental |
| **CRM** | CRM Open Rate | Tỷ lệ mở tin app push / email | Lượt mở tin / Lượt phát tin thành công | CRM Platform (Salesforce/Insider) | CRM Team | Chỉ dùng để tối ưu hóa tần suất gửi |
| **Revenue** | Gross Revenue | Tổng doanh thu vé bán ra có gắn tag chiến dịch | Tổng tiền vé bán ra (chưa thuế phí) | Finance Database | Finance Team | Chỉ báo cáo nội bộ dạng doanh thu gộp |
| **Creative QA** | QA Pass Rate | Tỷ lệ sản phẩm sáng tạo vượt qua Visual QA trước khi launch | Số sản phẩm đạt / Tổng số sản phẩm | Bảng theo dõi QA nội bộ | Brand Team | Chỉ dùng đánh giá quy trình sản xuất Governance: requires validation; not approved target; not forecast; do not use externally; evidence required. |
| **Brand/IP Risk**| IP Flag Counts | Số lỗi vi phạm bản quyền giải đấu được phát hiện trước/sau launch | Số lỗi ghi nhận | Log kiểm duyệt pháp lý | Legal Department | Chỉ số kiểm soát vận hành an toàn |

---

### 5. Bảng tính toán phễu chuyển đổi (Funnel Worksheet)

Bảng tính toán này dùng để đối chiếu các giả định kịch bản toán học (ở Mục 13 chiến dịch gốc) với dữ liệu thực tế thu được sau khi triển khai:

*   *Formulas:*
    1.  `Landing/App Sessions` = Impressions × CTR
    2.  `Booking-Search Sessions` = Landing/App Sessions × Search Rate Governance: requires validation; not approved target; not forecast; do not use externally; evidence required.
    3.  `Estimated Bookings` = Booking-Search Sessions × Search-to-Booking CVR Governance: requires validation; not approved target; not forecast; do not use externally; evidence required.
    4.  `Estimated Gross Revenue` = Estimated Bookings × ABV Governance: requires validation; not approved target; not forecast; do not use externally; evidence required.

| Chỉ số trong phễu | Kịch bản 1: Thận trọng | Kịch bản 2: Cơ sở | Kịch bản 3: Tăng trưởng | Kết quả thực tế (Actual) | Trạng thái xác thực (Validation) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Impressions** | 10,000,000 | 25,000,000 | 100,000,000 | `[INPUT DATA]` | PLANNING ASSUMPTION |
| **CTR** | 0.8% - 1.2% | 1.2% - 1.8% | 1.8% - 2.5% | `[INPUT DATA]` | PLANNING ASSUMPTION |
| **Landing Sessions** | 80,000 - 180,000 | 300,000 - 630,000 | 1,080,000 - 2,500,000 | `[INPUT DATA]` | PLANNING ASSUMPTION |
| **Search Rate** | 30% | 35% | 40% | `[INPUT DATA]` | PLANNING ASSUMPTION |
| **Search Sessions** | 24,000 - 54,000 | 105,000 - 220,500 | 432,000 - 1,000,000 | `[INPUT DATA]` | PLANNING ASSUMPTION |
| **CVR (Search to Booking)**| 1.0% - 1.5% | 1.5% - 2.2% | 2.2% - 3.0% | `[INPUT DATA]` | PLANNING ASSUMPTION |
| **Bookings** | 240 - 810 | 1,575 - 4,851 | 9,504 - 30,000 | `[INPUT DATA]` | PLANNING ASSUMPTION |
| **Average Booking Value** | 2.0M - 3.0M VND | 2.0M - 3.0M VND | 2.0M - 3.0M VND | `[INPUT DATA]` | PLANNING ASSUMPTION |
| **Gross Revenue** | 480M - 2.43B VND | 3.15B - 14.55B VND | 19.0B - 90.0B VND | `[INPUT DATA]` | PLANNING ASSUMPTION |

---

### 6. Mô hình đánh giá Doanh thu tăng thêm (Incrementality Worksheet) Governance: requires validation; not approved target; not forecast; do not use externally; evidence required.
Mô hình này nhằm mục đích tính toán phần doanh số thực tế do chiến dịch mang lại sau khi loại bỏ sai lệch tự nhiên:

*   **Thời gian đối chiếu (Baseline Period):** Giai đoạn hè 2025 (không có giải bóng đá lớn) hoặc 2 tuần trước khi launch chiến dịch hè 2026.
*   **Nhóm tiếp xúc (Exposed Group):** Khách hàng mục tiêu nhìn thấy quảng cáo chiến dịch hoặc nhận CRM thông báo.
*   **Nhóm giữ lại (Control/Holdout Group):** 5% - 10% tệp đối tượng mục tiêu được giữ lại hoàn toàn ngẫu nhiên trên hệ thống CRM/quảng cáo để không tiếp xúc với bất kỳ thông điệp nào của chiến dịch hè bóng đá.
*   **Khung thời gian quy thuộc (Attribution Window):** 7 ngày kể từ lượt tương tác cuối cùng của khách hàng.
*   **Sự kiện chuyển đổi (Conversion Event):** Đặt vé thành công (Payment confirmed).
*   **Yếu tố gây nhiễu loại trừ (Confounders):** Sự thay đổi giá dầu làm thay đổi giá vé cơ bản; các chương trình khuyến mãi chéo từ phòng Thương mại; sự thay đổi thời tiết làm bùng nổ nhu cầu du lịch bãi biển đột ngột.
*   **Công thức tính toán:**
    $$\text{Incremental Bookings} = \text{Bookings}_{\text{Exposed}} - \left( \frac{\text{Bookings}_{\text{Control}}}{\text{Size}_{\text{Control}}} \times \text{Size}_{\text{Exposed}} \right)$$
    $$\text{Incremental Gross Revenue} = \text{Incremental Bookings} \times \text{Average Booking Value}$$

| Chỉ số đánh giá tăng thêm | Số liệu giả định kịch bản | Số liệu thực tế ghi nhận | Trạng thái tin cậy |
| :--- | :--- | :--- | :--- |
| **Incremental Bookings** | `NOT MEASURABLE` hiện tại | `[CALCULATED DATA]` | Chờ chạy holdout test |
| **Incremental Gross Revenue** | `NOT MEASURABLE` hiện tại | `[CALCULATED DATA]` | Chờ chạy holdout test |
| **Incremental Ancillary Revenue**| `NOT MEASURABLE` hiện tại | `[CALCULATED DATA]` | Đo lường chi phí mua thêm hành lý, chọn chỗ ngồi |
| **Mức độ tin cậy** | `No Confidence` | `[CONFIDENCE LABEL]` | Phụ thuộc vào độ sạch của nhóm kiểm chứng |

*   *Tuyên bố được phép:* Chiến dịch đạt được mức doanh số tăng thêm $X$ VND dựa trên kết quả đối sánh nhóm holdout sạch.
*   *Tuyên bố bị cấm:* "Chiến dịch mang lại $Y$ VND doanh thu gộp tăng thêm" (nếu không thiết lập nhóm holdout kiểm chứng).

---

### 7. Đo lường chiến dịch CRM (CRM Measurement Worksheet)
*   **Đối tượng mục tiêu:** Hội viên SkyJoy có lịch sử bay tối thiểu 1 lần trong 12 tháng qua.
*   **Tiêu chí đủ điều kiện (Eligibility):** Khách hàng đã mở quyền nhận thông báo ứng dụng (opt-in app push) và email.
*   **Quy mô tệp opt-in:** `DATA UNAVAILABLE` (cần CRM Team xác nhận).
*   **Tần suất gửi tin tối đa (Frequency Cap):** Tối đa 2 email/tuần và 3 push notification/tuần đối với mỗi khách hàng thuộc đối tượng chiến dịch.
*   **Phân chia kiểm chứng CRM:** 90% nhận thông điệp (Exposed CRM), 10% giữ lại hoàn toàn (Holdout CRM).
*   **Bảng theo dõi hiệu suất CRM:**

| Chỉ số CRM | Exposed CRM (90%) | Holdout CRM (10%) | Chỉ số tăng thêm (CRM Lift) |
| :--- | :--- | :--- | :--- |
| **Open Rate** | `[ACTUAL %]` | N/A | N/A |
| **CTR** | `[ACTUAL %]` | N/A | N/A |
| **Booking Conversion Rate** | `[ACTUAL CVR %]` | `[ACTUAL CVR %]` | `[CVR Exposed] - [CVR Holdout]` |
| **Unsubscribe Rate** | `[ACTUAL %]` | N/A | So sánh với baseline hủy nhận tin thường nhật |
| **Complaint/Spam Rate** | `[ACTUAL %]` | N/A | So sánh với ngưỡng an toàn (< 0.1%) |

*   *No-Dark-Pattern Check:* Tất cả email gửi đi phải chứa link hủy đăng ký (unsubscribe link) rõ ràng ở cuối thư, không dùng các thủ thuật che giấu hoặc gây khó dễ cho người dùng muốn opt-out.

---

### 8. Đánh giá hiệu suất sản phẩm sáng tạo (Creative Performance Worksheet)
Bảng này dùng để theo dõi xem định hướng sáng tạo nào mang lại hiệu quả tương tác thực tế tốt nhất:

| Mã Asset | Kênh phát sóng | Định dạng | Ngân sách chi tiêu | Reach thực tế | Impressions | Lượt xem video | Completion Rate | Engagement Rate | CTR thực tế | Kết quả QA | Ghi chú tối ưu |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **KV-01** | Facebook | 4:5 Portrait | `[VND]` | `[Reach]` | `[Imps]` | N/A | N/A | `[%]` | `[%]` | `HUMAN REVIEW REQUIRED` | Mockup nền đỏ-vàng Governance: requires validation; not approved target; not forecast; do not use externally; evidence required. |
| **VD-01** | Reels | 9:16 (8s) | `[VND]` | `[Reach]` | `[Imps]` | `[Views]` | `[%]` | `[%]` | `[%]` | `HUMAN REVIEW REQUIRED` | Video motion trail Governance: requires validation; not approved target; not forecast; do not use externally; evidence required. |
| **TC-01** | TikTok | 9:16 (15s) | `[VND]` | `[Reach]` | `[Imps]` | `[Views]` | `[%]` | `[%]` | `[%]` | `HUMAN REVIEW REQUIRED` | Challenge dance Governance: requires validation; not approved target; not forecast; do not use externally; evidence required. |
| **BN-01** | In-App | 16:9 | $0 VND | N/A | `[Imps]` | N/A | N/A | `[%]` | `[%]` | `HUMAN REVIEW REQUIRED` | Banner nút CTA Governance: requires validation; not approved target; not forecast; do not use externally; evidence required. |

---

### 9. Các thiết lập dữ liệu bắt buộc trước khi Launch (Data Required Before Launch)
- **Thiết lập UTM/Campaign Tagging:** Toàn bộ liên kết trỏ về app/web phải được gắn UTM có cấu trúc nhất quán:
  `utm_source=facebook&utm_medium=paid&utm_campaign=football_summer_2026&utm_content=kv_01`
- **Tích hợp Web/App Analytics:** Kiểm tra sự kiện click và sự kiện tìm kiếm chuyến bay ("search_flight") trên Google Analytics và Firebase để đảm bảo dữ liệu ghi nhận không bị thiếu hụt hoặc trùng lặp.
- **Tích hợp Booking Engine:** Thiết lập cơ chế ghi nhận mã đặt vé (PNR) thành công trỏ từ nguồn UTM tương ứng vào cơ sở dữ liệu bán vé.
- **Xác nhận người sở hữu chỉ số:** Xác định rõ nhân sự chịu trách nhiệm xuất báo cáo đo lường hàng tuần.

---

### 10. Các mẫu báo cáo hiệu suất (Reporting Templates)

#### Mẫu 1: Báo cáo nhanh hàng ngày (Daily Pulse Report)
*   *Gửi lúc:* 08:30 sáng mỗi ngày.
*   *Định dạng:* Tin nhắn ngắn trên kênh truyền thông nội bộ.
*   *Nội dung:*
    *   Ngân sách đã tiêu trong ngày hôm qua: `[VND]`
    *   Lượt impressions tích lũy: `[Số lượng]`
    *   Số lượt Click/Landing Sessions: `[Số lượng]`
    *   Số lượt Booking-Search Sessions: `[Số lượng]`
    *   Cảnh báo rủi ro pháp lý/IP (nếu có): `[Không có / Ghi nhận lỗi]`

#### Mẫu 2: Báo cáo tối ưu hóa hàng tuần (Weekly Optimization Report)
*   *Gửi lúc:* Thứ Hai hàng tuần.
*   *Định dạng:* Bản báo cáo slide 3 trang gửi Commercial Lead.
*   *Nội dung:*
    *   Phân tích hiệu suất phễu thực tế so với 3 kịch bản lập kế hoạch.
    *   Bảng xếp hạng hiệu suất tương tác các sản phẩm sáng tạo (Creative Performance).
    *   Đề xuất phân bổ lại ngân sách giữa các kênh (ví dụ: chuyển bớt ngân sách từ Facebook sang TikTok nếu TikTok đạt CPC rẻ hơn).

#### Mẫu 3: Báo cáo tổng kết sau chiến dịch (Post-Campaign Report)
*   *Gửi lúc:* 14 ngày sau khi chiến dịch kết thúc hoàn toàn.
*   *Định dạng:* Tài liệu PDF chính thức gửi chủ sở hữu phê duyệt launch cuối cùng theo chính sách phê duyệt của Vietjet, cần xác nhận.
*   *Nội dung:*
    *   Tổng hợp số liệu toàn chiến dịch (Reach, Impressions, Sessions, Bookings, Gross Revenue).
    *   Báo cáo Doanh thu tăng thêm (Incremental Revenue) dựa trên kết quả nhóm kiểm chứng holdout.
    *   Phân tích các bài học kinh nghiệm và đề xuất cho các chiến dịch hè tiếp theo.

---

### 11. Bảng phân định giới hạn tuyên bố (Claim Boundary)

| Tuyên bố ĐƯỢC PHÉP nói | Tuyên bố CHỈ ĐƯỢC PHÉP nói khi có dữ liệu | Tuyên bố CHỈ ĐƯỢC PHÉP nói khi có thiết kế kiểm chứng | Tuyệt đối KHÔNG ĐƯỢC PHÉP nói |
| :--- | :--- | :--- | :--- |
| "Chiến dịch đã hoàn tất sản xuất bộ mockup hình ảnh theo tiêu chuẩn IP an toàn." | "Chiến dịch hè bóng đá đã ghi nhận $X$ lượt hiển thị quảng cáo và thu hút $Y$ lượt click." | "Chiến dịch đã mang lại $Z$ VND doanh thu tăng thêm (incremental revenue) từ nhóm CRM." | "Chiến dịch hè bóng đá của Vietjet mang lại $W$ tỷ doanh thu tăng thêm" (khi chỉ đo doanh thu gộp). Governance: requires validation; not approved target; not forecast; do not use externally; evidence required. |
| "Khung kịch bản truyền thông và phân tích độ nhạy đã được xây dựng sẵn sàng." | "Nội dung video ngắn trên TikTok đạt tỷ lệ CTR trung bình là $A\%$." | "Tỷ lệ chuyển đổi đặt vé thực tế tăng thêm $B\%$ so với nhóm không tiếp xúc quảng cáo." | "Vietjet là đối tác chính thức đưa người hâm mộ bay đi xem giải đấu hè 2026." |

---

### 12. Khuyến nghị mức độ sẵn sàng đo lường (Measurement Readiness)
- **GO** cho việc chuẩn bị hạ tầng đo lường, phân bổ tag quảng cáo và thiết kế nhóm holdout.
- **NO-GO** cho bất kỳ báo cáo hiệu quả tài chính hay ROI gộp nào gọi là hiệu quả tăng thêm nếu không chạy thiết kế đối chứng holdout sạch.
- **NO-GO** cho việc công bố các số liệu giả định của phễu lập kế hoạch ra bên ngoài.
