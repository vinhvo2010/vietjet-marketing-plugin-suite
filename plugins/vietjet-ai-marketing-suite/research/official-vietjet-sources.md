# Sổ nguồn chính thức Vietjet — snapshot kiểm tra 23/09/2026

[Sổ nguồn có cấu trúc](official-vietjet-sources.json) là nguồn duy nhất cho các thẻ bên dưới. `verifiedAt` là ngày đọc nội dung trang công khai qua công cụ duyệt web; không khẳng định đã truy vấn hệ thống đặt vé hay dữ liệu thời gian thực. `effectiveDate` chỉ ghi ngày trang nói rõ; `null` nghĩa chưa xác minh được ngày chung cho toàn trang. `reviewAfter` là hạn kiểm lại do dự án đặt, không phải ngày chính sách hết hiệu lực.

`approvedForPublic: true` chỉ xác nhận thẻ này đã được rà soát trong phiên để chứa diễn giải ngắn từ nguồn công khai, không chứa hồ sơ hành khách hoặc tài liệu nội bộ. Trường này **không** biểu thị Vietjet, Pháp chế, Ops, chủ thương hiệu hay cơ quan quản lý đã phê duyệt plugin hoặc cấp quyền công bố thay mặt hãng.

## Nguồn đã đọc được

| ID | Nguồn chính thức | Bằng chứng đọc được | Ngày hiệu lực được trang nêu |
|---|---|---|---|
| `vietjet-conditions-of-carriage-vi` | [Điều lệ vận chuyển](https://www.vietjetair.com/vi/pages/dieu-le-van-chuyen-vietjet-1618221808366) | Tiêu đề/ngày hiệu lực; Điều 2 về phạm vi, thứ bậc và ngôn ngữ; Điều 4 về tiền vé. | 12/01/2026 |
| `vietjet-baggage-rules-vi` | [Quy định hành lý](https://www.vietjetair.com/VI/pages/de-co-chuyen-bay-tot-dep-1578323501979/quy-dinh-hanh-ly-1578483259803) | Các mục xách tay, ký gửi, vật phẩm có điều kiện; không gộp ngày của một mục thành ngày toàn trang. | Chưa xác minh ngày chung |
| `vietjet-fare-conditions-vi` | [Điều kiện vé](https://www.vietjetair.com/vi/pages/de-co-chuyen-bay-tot-dep-1578323501979/dieu-kien-ve-1641466500765) | Tiêu đề/ngày và bảng theo loại vé/nhóm hành trình; bảng có ô gộp. | 10/10/2023 |
| `vietjet-change-refund-cancellation-vi` | [Quy trình đổi, hoàn, hủy](https://www.vietjetair.com/vi/pages/quy-trinh-xu-ly-doi-hoan---huy-ve-1754655807306) | Tiêu đề/ngày; phân biệt điều kiện vé, phí và nơi nhận yêu cầu. | 01/06/2023 |
| `vietjet-travel-documents-vi` | [Giấy tờ tùy thân](https://www.vietjetair.com/vi/pages/de-co-chuyen-bay-tot-dep-1578323501979/giay-to-tuy-than-1578483122906) | Tiêu đề/ngày; mục nội địa và quốc tế. URL lấy từ liên kết chính thức ở chân trang. | 03/02/2026 |
| `vietjet-seat-selection-vi` | [Chọn chỗ ngồi ưu tiên](https://www.vietjetair.com/vi/pages/mua-hanh-ly-suat-an-chon-cho-ngoi-va-hon-the-nua-1754713926921/chon-cho-ngoi-uu-tien-1597291802312) | Nhóm chỗ, điều kiện và kênh đặt trước; không thấy ngày hiệu lực. | Chưa xác minh |
| `vietjet-codeshare-guidance-vi` | [Hướng dẫn liên danh](https://www.vietjetair.com/vi/pages/huong-dan-ve-chuyen-bay-lien-danh-codeshare-1780882375047) | Phân biệt hãng bán/hãng khai thác và phạm vi dịch vụ. | Chưa xác minh |
| `vietjet-skyjoy-redemption-en` | [Quy định đổi thưởng SkyJoy](https://skyjoy.vietjetair.com/en/tc/) | Nội dung các loại vé thưởng; tiêu đề ghi phiên bản 1.2. Website Vietjet có dẫn tới tên miền SkyJoy này. | 10/10/2023 |

## Cách dùng trong câu trả lời và nội dung marketing

- Chọn đúng thẻ theo nghiệp vụ; đọc `scope`, `requiredContext`, `limitations` trước tóm tắt. Chỉ hỏi các trường không định danh cần cho câu trả lời.
- Trích URL chính thức và ngày kiểm tra; nêu rõ snapshot khi chưa đọc lại trang trong phiên. Không gọi dữ liệu trong sổ là giá, lịch bay, ghế còn hoặc quyền lợi cá nhân đang được hệ thống xác nhận.
- Tất cả thẻ cần rà lại từ 30/09/2026. Với nội dung thương mại sắp phát hành, thay đổi quyền lợi hoặc quyết định hành trình, kiểm lại tại thời điểm sử dụng dù chưa đến hạn này.
- Nếu nội dung nguồn khác nhau, lưu cả hai nguồn và nêu điểm khác; không tự chọn điều kiện thuận lợi hơn. Điều lệ, điều kiện vé đã mua và hãng khai thác cần được đối chiếu đúng phạm vi; câu hỏi quyền lợi riêng chuyển về kênh hãng.
- Nguồn công khai không thay brandbook, hợp đồng cấp quyền thương hiệu hoặc người duyệt nội bộ. Chưa có bằng chứng chứng nhận ngành hay phê duyệt Vietjet cho plugin.

## URL chưa xác minh được trong phiên

Các URL dưới đây có trạng thái `not_verified` và **không** là thẻ được chấp nhận trong JSON. Không suy ra website ngừng hoạt động từ lỗi công cụ.

| URL đã thử | Kết quả | Cách xử lý |
|---|---|---|
| `https://www.vietjetair.com/vi/pages/giay-to-tuy-than-1578483122906` | Công cụ mở trang trả lỗi nội bộ. | Dùng URL đầy đủ dưới `de-co-chuyen-bay-tot-dep-1578323501979/` đã đọc được trong sổ. |
| `https://www1.vietjetair.com/vi/pages/mua-hanh-ly-suat-an-chon-cho-ngoi-va-hon-the-nua-1754713926921/chon-cho-ngoi-uu-tien-1597291802312` | Chỉ trả tiêu đề, không đủ nội dung. | Dùng liên kết cùng bài trên `www.vietjetair.com` từ điều hướng chính thức. |

<!-- check-output: rules-doc -->
