---
name: vietjet-global-localization
description: "Bản địa hoá nội dung marketing Vietjet Air cho các thị trường quốc tế — ngôn ngữ, văn hoá, tôn giáo, quy định quảng cáo và giá vé theo từng nước. Dùng khi đưa một chiến dịch sang thị trường mới, dịch nội dung, kiểm tra yếu tố văn hoá có phù hợp không, hoặc lên lịch theo mùa vụ/lễ hội địa phương."
---

# 🌏 BẢN ĐỊA HOÁ THỊ TRƯỜNG QUỐC TẾ

`PLUGIN_ROOT` là thư mục chứa `plugin.json` của bản plugin đang nạp skill này. Mọi đường dẫn `../../...` tính từ thư mục chứa chính `SKILL.md`, không từ thư mục dự án đang mở. Nếu host không nêu đường dẫn skill, lấy `source.path` của bản đang bật từ `codex plugin list --json`; kiểm tra `PLUGIN_ROOT/rules/00_INDEX.md` trước khi đọc. Không xác định được thì báo thiếu và dừng.

## 0. NẠP TRƯỚC
`../../rules/vietjet-group-marketing-operating-model.md` · `../../rules/vietjet-agent-collaboration.md` · `../../rules/vietjet-brand-safety.md` · `../../rules/vietjet-data-protection.md` · `../../rules/vietjet-source-and-expiry.md` · `references/market-profiles.md`

---

## 1. NGUYÊN TẮC

**Bản địa hoá ≠ dịch.** Một câu dịch đúng ngữ pháp vẫn có thể sai hoàn toàn về văn hoá, tôn giáo, hoặc pháp lý.

Ba tầng bắt buộc, theo thứ tự:
1. **Tầng pháp lý** — quy định quảng cáo, hiển thị giá, bảo vệ dữ liệu tại thị trường đó. Sai ở tầng này là rủi ro bị xử phạt.
2. **Tầng văn hoá** — tôn giáo, lịch sử, biểu tượng, màu sắc, con số, cử chỉ. Sai ở tầng này là rủi ro uy tín.
3. **Tầng ngôn ngữ** — từ ngữ, giọng điệu, cách xưng hô. Sai ở tầng này là rủi ro hiệu quả.

Làm ngược thứ tự là cách phổ biến nhất để hỏng: dịch xong đẹp rồi mới phát hiện không được phép chạy.

---

## 2. QUY TRÌNH

1. **Khóa scope**: `operating_entity`, `point_of_sale`, `source_market` hoặc `route_corridor`. Chỉ có tên quốc gia thì chưa đủ để làm tiếp.
2. **Xác định khung pháp lý áp dụng** → chuyển `legal_regulatory_compliance` tra cứu **trong phiên**, kèm link + ngày. Không dùng hiểu biết từ trí nhớ.
3. **Kiểm tra tầng văn hoá** theo checklist mục 4 và dùng bằng chứng, không dùng stereotype.
4. **Chuyển ngữ**, không dịch máy nguyên văn với nội dung thương hiệu.
5. **Rà lại giá, payment, service và điều kiện** theo POS/corridor thực tế.
6. **Người bản ngữ rà soát cuối** trước khi phát hành. `[CẦN XÁC MINH — Nhân sự/Agency]` ai là người rà cho từng audience/ngôn ngữ.

---

## 3. RÀNG BUỘC PHÁP LÝ THEO THỊ TRƯỜNG

`references/market-profiles.md` có baseline nguồn chính thức cho Việt Nam, Thái Lan, Australia, India và Mainland China. Baseline chỉ để định tuyến; Legal phải xác nhận văn bản, phase hiệu lực, giá và quyền hành khách trong phiên release.

**Quy tắc cứng:** không chạy quảng cáo có giá khi chưa có current-law price-display checklist cho đúng POS và approval của RM/Legal.

---

## 4. CHECKLIST VĂN HOÁ

Chạy cho mọi nội dung trước khi vào thị trường mới.

### Tôn giáo & tín ngưỡng
- [ ] Thực phẩm/đồ uống trong hình có phù hợp không (rượu, thịt lợn, thịt bò tuỳ thị trường)
- [ ] Thời điểm phát hành có trùng kỳ chay/lễ trọng không
- [ ] Biểu tượng tôn giáo có bị dùng làm yếu tố trang trí không
- [ ] Trang phục nhân vật có phù hợp chuẩn mực địa phương không

### Lịch sử & chính trị
- [ ] Bản đồ, đường biên giới, tên địa danh — **cực kỳ nhạy cảm ở nhiều thị trường**
- [ ] Cờ, quốc huy, biểu tượng quốc gia dùng đúng cách
- [ ] Không chạm tới xung đột lịch sử, tranh chấp lãnh thổ
- [ ] Ngày kỷ niệm nhạy cảm — kiểm tra lịch trước khi lên lịch đăng

### Biểu tượng & con số
- [ ] Màu sắc: ý nghĩa khác nhau theo văn hoá (trắng, đen, đỏ)
- [ ] Con số kiêng kỵ hoặc may mắn theo từng thị trường
- [ ] Cử chỉ tay trong hình ảnh
- [ ] Động vật, hoa, vật phẩm mang ý nghĩa riêng

### Xã hội
- [ ] Vai trò giới trong hình ảnh — áp dụng `../../rules/vietjet-brand-safety.md` mục 2 ở mọi thị trường
- [ ] Cấu trúc gia đình được thể hiện
- [ ] Hài hước — thường không chuyển ngữ được, mặc định bỏ

---

## 5. HIỂN THỊ GIÁ — ĐIỂM DỄ SAI NHẤT

Quy định hiển thị giá khác nhau đáng kể giữa các thị trường. Nguyên tắc an toàn nhất: **hiển thị giá đã gồm toàn bộ thuế và phí bắt buộc ở mọi thị trường**, kể cả nơi luật chưa yêu cầu.

Australia là thị trường cần kiểm tra total-price/component-pricing và availability claim trên hướng dẫn ACCC hiện hành. Agent không trích số điều luật từ trí nhớ; Legal ghi link + ngày tra cứu trong release packet.

Chuyển agent 12 rà soát trước mọi chiến dịch có yếu tố giá.

---

## 6. NGÔN NGỮ

- **Nội dung thương hiệu** (tagline, khẩu hiệu, thông điệp chính): người bản ngữ viết, không dịch máy.
- **Nội dung vận hành** (xác nhận đặt chỗ, thông báo chuyến bay, hỗ trợ): dịch chính xác, ưu tiên rõ ràng hơn hay ho.
- **Nội dung khủng hoảng**: mọi bản ngôn ngữ **cùng nội dung, không bản nào mềm hơn bản nào**. Xem `../vietjet-crisis-shield/SKILL.md`.
- Đa ngôn ngữ nên đặt ở: xác nhận đặt chỗ · trang chủ app · pre-departure · tại sân bay · hỗ trợ khách hàng. **Không làm rối các tài liệu vận hành quan trọng** như thẻ lên máy bay.

---

## 7. THAM CHIẾU
- `references/market-profiles.md` — operating baseline và checklist scope theo thị trường

<!-- check-output: rules-doc -->
