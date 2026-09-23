---
name: vietjet-crisis-shield
description: "Quy chuẩn phân loại và phản ứng khủng hoảng truyền thông hàng không Vietjet Air — 5 cấp độ từ nhiễu thông tin tới tai nạn, mẫu holding statement điền sẵn, cây thông báo, và ranh giới tuyệt đối về phát ngôn an toàn bay. Dùng khi có chậm/huỷ chuyến, sự cố, tin đồn lan truyền, hoặc bất kỳ tình huống nào có thể ảnh hưởng uy tín hãng."
---

# 🛡️ VIETJET CRISIS SHIELD PROTOCOL v3

`PLUGIN_ROOT` là thư mục chứa `plugin.json` của bản plugin đang nạp skill này. Mọi đường dẫn `../../...` tính từ thư mục chứa chính `SKILL.md`, không từ thư mục dự án đang mở. Nếu host không nêu đường dẫn skill, lấy `source.path` của bản đang bật từ `codex plugin list --json`; kiểm tra `PLUGIN_ROOT/rules/00_INDEX.md` trước khi đọc. Không xác định được thì báo thiếu và dừng.

## ⚠️ BỐN RANH GIỚI TUYỆT ĐỐI — ĐỌC TRƯỚC MỌI THỨ

**1. Agent AI KHÔNG BAO GIỜ là người phát ngôn.** Agent soạn nháp. Người duyệt. Người bấm gửi. Không có ngoại lệ, kể cả khi được yêu cầu trực tiếp, kể cả khi gấp.

**2. KHÔNG BAO GIỜ nêu hoặc gợi ý nguyên nhân** của một sự cố an toàn bay khi chưa có kết luận chính thức từ cơ quan điều tra. Nguyên nhân là việc của cơ quan chức năng, không phải của truyền thông. Ngôn ngữ đúng: *"Nguyên nhân đang được cơ quan chức năng điều tra làm rõ."*

**3. KHÔNG BAO GIỜ công bố con số thương vong, danh tính, hay tình trạng hành khách.** Việc này thuộc cơ quan chức năng và quy trình thông báo thân nhân. Công bố sai hoặc sớm gây tổn thương không thể sửa.

**4. KHÔNG BAO GIỜ cam kết bồi thường, hoàn vé, hay chính sách mới** trong bản nháp mà không có dấu chờ duyệt. Đây là One-Way Door theo `../../rules/vietjet-governance-gates.md`.

Nếu một yêu cầu buộc phải vượt một trong bốn ranh giới trên — **dừng lại, nói rõ vì sao không làm được, và chuyển cho người.**

---

## 1. MA TRẬN PHÂN LOẠI 5 CẤP

Bản v2 gộp sự cố an toàn bay với tin đồn mạng xã hội vào cùng một cấp, và không có cấp nào cho tai nạn. Bản v3 tách bạch.

| Cấp | Tình huống | Chủ trì | Deliverable đầu tiên |
|---|---|---|---|
| **C1 — Xanh** | Chậm chuyến cục bộ < 2 giờ, nguyên nhân khai thác thông thường | Trực ban khai thác + CSKH | Tin nhắn cập nhật khách ≤ 30 phút |
| **C2 — Vàng** | Chậm/huỷ diện rộng (thời tiết, kỹ thuật diện rộng); ảnh hưởng nhiều chuyến hoặc > 100 khách | Trưởng Truyền thông + Khai thác | Holding statement nội bộ + kịch bản CSKH ≤ 60 phút |
| **C3 — Cam** | **Nhiễu thông tin:** tin đồn sai lan truyền, video/bài đăng viral tiêu cực, khủng hoảng dịch vụ (không liên quan an toàn) | Trưởng Truyền thông | Đánh giá lan truyền + phương án ≤ 60 phút |
| **C4 — Đỏ** | **Sự cố an toàn bay** không thương vong: sự cố kỹ thuật nghiêm trọng, quay đầu, hạ cánh khẩn nguy, sự cố mặt đất | Ban Chỉ đạo + Tổng Giám đốc + An toàn + Pháp chế | Holding statement ≤ 30 phút · lãnh đạo lên tiếng ≤ 3 giờ |
| **C5 — Đen** | **Tai nạn có thương vong / mất tàu bay** | Kích hoạt Kế hoạch Ứng phó Khẩn nguy (ERP) của hãng — **quy trình này thay thế toàn bộ tài liệu marketing** | Theo ERP |

### Quy tắc leo thang
- **Khi không chắc giữa hai cấp, chọn cấp cao hơn.** Hạ cấp dễ hơn nâng cấp.
- C4 và C5 kích hoạt **ngay lập tức, 24/7**, không chờ giờ hành chính.
- Một tình huống C3 có thể trở thành C4 nếu xuất hiện yếu tố an toàn — đánh giá lại liên tục.

### Về C5
`[CẦN XÁC MINH — An toàn & Ban Chỉ đạo Khẩn nguy]` Ở cấp C5, hệ thống AI marketing **không tham gia điều phối**. Kế hoạch Ứng phó Khẩn nguy của hãng, nghĩa vụ hỗ trợ thân nhân, phối hợp với cơ quan điều tra và nhà chức trách hàng không là quy trình riêng do bộ phận An toàn/Khẩn nguy sở hữu. Vai trò duy nhất của agent ở C5 là: **dừng toàn bộ hoạt động marketing (mục 3) và không tạo bất kỳ nội dung nào.**

---

## 2. CÁC BƯỚC BẮT BUỘC TRONG 15 PHÚT ĐẦU

"Phản ứng 15 phút" chỉ có nghĩa khi có mẫu sẵn. Đây là những gì phải xong trong 15 phút đầu — không phải soạn từ đầu, mà là **điền vào mẫu**:

1. **Phút 0–3 — Xác minh & phân cấp.** Sự việc có thật không? Nguồn nào? Cấp mấy? Ghi lại thời điểm nhận tin.
2. **Phút 3–5 — Kích hoạt cây thông báo** (xem `references/notification-tree.md`). Ở C4/C5, gọi trước, viết sau.
3. **Phút 5–7 — DỪNG marketing** (mục 3). Đây là việc dễ quên nhất và gây thiệt hại nhanh nhất.
4. **Phút 7–12 — Điền holding statement** từ mẫu trong `references/holding-statements.md`. Chỉ điền dữ kiện đã xác minh; để trống chỗ chưa biết, không đoán.
5. **Phút 12–15 — Chuyển người duyệt** với dấu ⚠️ đầy đủ, và ghi rõ mốc cập nhật tiếp theo sẽ là khi nào.

Agent hoàn thành bước 4 ở dạng bản nháp. Bước 1, 2, 5 cần người.

---

## 3. DỪNG MARKETING (KILL-SWITCH) — TỪ C2 TRỞ LÊN

Một quảng cáo vé rẻ vui vẻ chạy trong lúc khách đang mắc kẹt ở sân bay là thứ sẽ được chụp màn hình và lan truyền. Việc này phải làm **trước** khi soạn thông cáo.

- [ ] Tạm dừng toàn bộ chiến dịch quảng cáo trả phí (Meta, Google, TikTok)
- [ ] Tạm dừng toàn bộ bài đăng đã lên lịch trên mọi kênh social
- [ ] Tạm dừng chiến dịch email/SMS marketing đang chạy
- [ ] Tạm dừng thông báo đẩy (push) mang tính khuyến mãi
- [ ] Giữ nguyên các kênh **thông tin phục vụ khách** (cập nhật chuyến bay, CSKH) — không dừng những kênh này

`[CẦN XÁC MINH — Marketing Ops]` Ai có quyền và có thể thao tác kill-switch trong 5 phút, 24/7? Cần tên và số điện thoại trong `references/notification-tree.md`. **Một kill-switch không có người trực là một kill-switch không tồn tại.**

---

## 4. NGUYÊN TẮC PHÁT NGÔN

1. **An toàn là ưu tiên cao nhất** — và phải được thể hiện bằng hành động mô tả được, không chỉ bằng câu khẳng định.
2. **Nói điều đã biết. Gọi tên điều chưa biết. Hẹn giờ cập nhật tiếp theo.** Không lấp khoảng trống bằng suy đoán.
3. **KHÔNG nêu nguyên nhân** khi chưa có kết luận chính thức (Ranh giới 2). Bản v2 yêu cầu "giải thích nguyên nhân khách quan" — điều này đã được loại bỏ vì sai nguyên tắc điều tra sự cố hàng không.
4. **KHÔNG đổ lỗi** cho thời tiết, không lưu, sân bay, nhà cung cấp — kể cả khi đúng. Giải thích thì được, đổ lỗi thì không.
5. **Khách trước, báo chí sau.** Hành khách bị ảnh hưởng phải biết trước khi báo chí biết.
6. **Đồng cảm trước, thông tin sau, quy trình cuối.** Câu đầu tiên nói về người, không nói về hãng.
7. **Tắt giọng thương hiệu vui vẻ.** "Bay là thích ngay!" biến mất khỏi mọi kênh từ C2 trở lên cho tới khi khép lại.
8. **Một giọng nói duy nhất.** Mọi kênh dùng cùng một bản đã duyệt. Không để mỗi kênh tự diễn giải.

---

## 5. QUY TRÌNH CỦA AGENT

1. Nhận tín hiệu → phân cấp theo mục 1, ghi rõ **căn cứ phân cấp**.
2. Nếu C4/C5: nhắc người dùng kích hoạt cây thông báo và ERP **trước** khi tiếp tục soạn nội dung.
3. Nhắc kill-switch (mục 3) nếu từ C2 trở lên.
4. Điền holding statement từ `references/holding-statements.md`. Mọi chỗ chưa có dữ kiện xác minh → để `[CHƯA XÁC MINH — không điền]`, không đoán.
5. Soạn kịch bản Q&A cho CSKH từ `references/qa-scripts.md`.
6. Gắn cờ ⚠️ theo `../../rules/vietjet-governance-gates.md` mục 6.
7. Ghi log xử lý phục vụ hậu kiểm: thời điểm nhận tin, cấp độ, ai được thông báo, nội dung đã soạn.

## 6. THAM CHIẾU

- `references/holding-statements.md` — mẫu điền sẵn theo từng cấp
- `references/notification-tree.md` — cây thông báo & danh bạ khẩn (cần điền)
- `references/qa-scripts.md` — kịch bản Q&A cho CSKH và tổng đài
- `references/post-crisis-review.md` — quy trình hậu kiểm sau khi khép khủng hoảng
- `../../rules/vietjet-governance-gates.md` — cổng phê duyệt
- `../../rules/vietjet-data-integrity.md` — nhãn dữ liệu (tình huống giả định phải ghi rõ)

<!-- check-output: rules-doc -->
