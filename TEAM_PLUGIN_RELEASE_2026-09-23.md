# Đưa 18 vai trò Vietjet Marketing AI lên plugin dùng chung

Trạng thái ngày 23/09/2026: **bản thử nghiệm 5.0.3 qua marketplace Git**, không phải plugin đã được duyệt trong OpenAI Plugins Directory. Gói này chứa 18 vai trò chuyên môn dưới dạng 24 skill có thể gọi trong Codex; nó không chạy 18 agent tự động và không thay thế người phê duyệt. Nguồn thử nghiệm là repository GitHub công khai do tài khoản `vinhvo2010` quản lý: `https://github.com/vinhvo2010/vietjet-marketing-plugin-suite`. Marketplace và bản 5.0.2 đã được xác minh trực tiếp trên GitHub; bản 5.0.3 cần kiểm tra lại sau khi phát hành.

## Hai đường phát hành

1. **Team dùng Codex:** chủ sở hữu đưa nội dung thư mục `team-plugin-marketplace/` vào repository Git được phép chia sẻ với team. Người dùng thêm repository đó làm marketplace và cài plugin một lần. Các lần sau làm mới marketplace để nhận bản mới, rồi mở task mới. Repository hiện dự kiến công khai để người thử nghiệm không cần tài khoản GitHub; đây vẫn không phải niêm yết trong OpenAI Plugins Directory.
2. **Mọi tài khoản ChatGPT/Codex:** nộp plugin lên [OpenAI Plugin Directory](https://platform.openai.com/plugins) bằng tài khoản nhà phát hành đủ điều kiện, với website, hỗ trợ, quyền sử dụng thương hiệu/nội dung và chính sách riêng tư/điều khoản phù hợp. Sau rà soát và phát hành, người dùng mới có thể tìm/cài theo kênh công khai. Việc có ZIP hoặc connector ID chưa hoàn thành bước này.

App/MCP hosted riêng chỉ cung cấp các công cụ đã đăng ký; 18 vai trò Codex và App/MCP **không tự đồng bộ phiên bản**. File `.app.json` của plugin tham chiếu connector ở chế độ phát triển; tài khoản khác có thể không nhìn thấy hoặc kết nối được cho tới khi App được chia sẻ/phát hành đúng cách. Không hứa `@` hoạt động cho mọi người ở giai đoạn này.

## Cách team cài sau khi có repository được phê duyệt

```bash
codex plugin marketplace add vinhvo2010/vietjet-marketing-plugin-suite
codex plugin add vietjet-ai-marketing-suite@vietjet-team
```

Tạo **task Codex mới** sau khi cài. Gõ `$vietjet-ai-marketing-suite:vietjet-marketing-squad` hoặc `/vietjet-ai-marketing-suite:vietjet-marketing-squad` để kiểm tra skill. `@` là bề mặt App/connector, không phải cách gọi 18 skill. Các tài khoản chỉ dùng ChatGPT Go/Plus cần kênh Plugin Directory/App được hỗ trợ trên chính tài khoản của họ; không thể coi marketplace Codex Mac là đã cài cho ChatGPT.

## Cập nhật các bản sau

Chủ sở hữu phát hành phiên bản mới với manifest tăng version, kiểm tra đủ 18 agent/24 skill, rà soát dữ liệu nhạy cảm và quyền phát hành, rồi cập nhật repository/Directory theo đúng kênh. Người dùng Codex đã cài từ marketplace Git chỉ cần làm mới nguồn:

```bash
codex plugin marketplace upgrade vietjet-team
```

Sau đó mở task mới và thử gọi skill có namespace. Đây là **một lệnh refresh + task mới**, không phải cập nhật nội dung trong task đang mở. Nếu máy vẫn hiện version cũ, kiểm tra `codex plugin list` và hướng dẫn cập nhật của bản Codex đang dùng; không xoá plugin cũ trước khi có bản sao lưu và thử nghiệm. Không giả định rằng mọi máy tự cập nhật tức thì hoặc App/MCP riêng cũng được cập nhật theo.

## Cổng phát hành còn thiếu

- Xác nhận ai có quyền phát hành tên, nhận diện và nội dung Vietjet; vì source hiện ghi giấy phép `Proprietary`.
- Kiểm tra commit thực tế trên repository Git dùng chung; việc chuẩn bị ZIP không đồng nghĩa đã đưa bản mới lên GitHub. Nộp Directory là bước khác.
- Chạy kiểm thử trên một tài khoản Codex **khác**: cài từ nguồn được chia sẻ, task mới, gọi skill; nếu dùng `@`, kiểm tra App và quyền kết nối trên tài khoản đó.
- Rà soát từng thông tin hàng không/giá/lịch bay, dữ liệu cá nhân, pháp lý và nguồn Vietjet chính thức ở thời điểm sử dụng. Plugin chỉ hỗ trợ nghiên cứu, phân tích, nháp và review; không tự cấp quyền phát hành, chi tiền, đổi giá hoặc xử lý sự cố an toàn bay.

Các hướng dẫn kỹ thuật cập nhật theo [OpenAI Plugins](https://developers.openai.com/plugins/build/plugins) và [quy trình nộp](https://developers.openai.com/plugins/deploy/submission); cần đối chiếu lại giao diện tài khoản thực tế trước khi hướng dẫn đại trà.
