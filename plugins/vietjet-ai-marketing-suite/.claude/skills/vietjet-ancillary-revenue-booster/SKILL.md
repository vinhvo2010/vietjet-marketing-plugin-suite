---
name: vietjet-ancillary-revenue-booster
description: "Thiết kế luồng Next-Best-Action bán chéo dịch vụ phụ trợ Vietjet Air — hành lý ký gửi, suất ăn, chọn ghế, bảo hiểm, ưu tiên — và tích hợp SkyJoy. Dùng khi cần tăng doanh thu ancillary trên mỗi khách, thiết kế offer theo hành trình đặt vé, hoặc kiểm tra một luồng upsell có minh bạch và hợp quy không."
---

# 💺 ANCILLARY REVENUE & NEXT-BEST-ACTION

`PLUGIN_ROOT` là thư mục chứa `plugin.json` của bản plugin đang nạp skill này. Mọi đường dẫn `../../...` tính từ thư mục chứa chính `SKILL.md`, không từ thư mục dự án đang mở. Nếu host không nêu đường dẫn skill, lấy `source.path` của bản đang bật từ `codex plugin list --json`; kiểm tra `PLUGIN_ROOT/rules/00_INDEX.md` trước khi đọc. Không xác định được thì báo thiếu và dừng.

## 0. NẠP TRƯỚC
`../../rules/vietjet-data-protection.md` (cá nhân hoá & PII) · `../../rules/vietjet-governance-gates.md` · `../../rules/vietjet-brand-safety.md` mục 4.

---

## 1. NGUYÊN TẮC BẤT DI BẤT DỊCH

**Ancillary là dịch vụ khách thực sự cần, được đề xuất đúng lúc — không phải phí ẩn được giấu khéo.**

Ba ranh giới:
1. **Minh bạch giá.** Tổng số tiền phải trả hiển thị rõ ở mọi bước. Không drip pricing — không lộ dần từng khoản phí qua từng màn hình.
2. **Không tick sẵn.** Mọi dịch vụ phụ trợ phải do khách **chủ động chọn**. Ô đã tick sẵn (pre-ticked) bị nhiều cơ quan quản lý coi là hành vi gây hiểu nhầm.
3. **Không cá nhân hoá giá theo dữ liệu cá nhân.** Cá nhân hoá **đề xuất, thứ tự hiển thị, ngôn ngữ** thì được. Cùng một sản phẩm, mọi khách thấy cùng một giá.

Vi phạm ba điều này làm hỏng chính thứ đang xây: sự tin cậy. Và tạo rủi ro pháp lý thật ở nhiều thị trường.

---

## 2. DANH MỤC ANCILLARY

| Nhóm | Sản phẩm |
|---|---|
| Hành lý | Ký gửi theo mức cân, hành lý quá khổ, dụng cụ thể thao |
| Ẩm thực | Suất ăn nóng, đồ uống, combo |
| Ghế | Chọn ghế thường, ghế nhiều chỗ để chân, ghế hàng đầu |
| Ưu tiên | Làm thủ tục ưu tiên, lên máy bay ưu tiên, hành lý ra trước |
| Bảo vệ | Bảo hiểm du lịch, bảo hiểm huỷ chuyến |
| Khác | Đưa đón sân bay, phòng chờ, wifi (nếu có) |

`[CẦN XÁC MINH — Thương mại]` Danh mục chính xác, tên thương mại, và giá theo từng thị trường.

---

## 3. THIẾT KẾ NEXT-BEST-ACTION

### 3.1 Theo thời điểm trong hành trình
| Thời điểm | Đề xuất phù hợp | Vì sao |
|---|---|---|
| Trong luồng đặt vé | Hành lý, chọn ghế | Khách đang ở tâm thế quyết định, biết rõ nhu cầu |
| Ngay sau xác nhận đặt chỗ | Bảo hiểm, đưa đón | Còn trong ngữ cảnh chuyến đi |
| T-7 tới T-3 ngày | Suất ăn, hành lý bổ sung | Khách bắt đầu chuẩn bị thật |
| T-24 giờ (check-in) | Nâng ghế, ưu tiên | Quyết định nhanh, giá trị rõ |
| Sau chuyến bay | SkyJoy, chuyến tiếp theo | Trải nghiệm còn mới |

### 3.2 Tín hiệu được dùng để cá nhân hoá **đề xuất**
✅ Được: loại hành trình (một chiều/khứ hồi) · thời lượng bay · số khách trong đặt chỗ · có trẻ em không · điểm đến · thời điểm trong hành trình · lịch sử **loại dịch vụ** đã mua (dạng tổng hợp)

❌ Không được: dữ liệu định danh cá nhân · suy đoán khả năng chi trả · dữ liệu nhạy cảm · bất kỳ tín hiệu nào dùng để **thay đổi giá**

### 3.3 Giới hạn tần suất
- Tối đa **một** đề xuất chính mỗi bước trong luồng đặt vé — không xếp chồng.
- Khách đã từ chối một dịch vụ → không đề xuất lại dịch vụ đó trong cùng hành trình.
- Không đề xuất ancillary trong bất kỳ giao tiếp nào liên quan gián đoạn chuyến bay. Xem mục 5.

---

## 4. SKYJOY

- Hiển thị điểm tích được **trước khi** khách quyết định, không phải sau.
- Điều kiện đổi điểm, hạn dùng, giới hạn ghế thưởng phải nêu rõ, không giấu trong điều khoản.
- Không dùng điểm thưởng làm lý do để giảm minh bạch giá tiền mặt.

`[CẦN XÁC MINH — Thương mại + Pháp chế]` Điều khoản chương trình, tỷ lệ tích/đổi, và quy định về chương trình khách hàng thân thiết tại từng thị trường.

---

## 5. ⚠️ NGỪNG BÁN KHI CÓ GIÁN ĐOẠN

Khi một chuyến bay bị chậm, huỷ, hoặc có sự cố:
- **Dừng toàn bộ đề xuất ancillary** tới khách trên chuyến đó
- Kênh liên lạc chỉ dùng cho **thông tin và hỗ trợ**
- Không đề xuất bảo hiểm, nâng hạng, hay bất kỳ sản phẩm nào cho khách đang bị ảnh hưởng

Bán thêm cho người đang mắc kẹt là thứ sẽ được chụp màn hình. Liên kết với kill-switch trong `../vietjet-crisis-shield/SKILL.md` mục 3.

---

## 6. ĐO LƯỜNG

| Chỉ số | Ghi chú |
|---|---|
| Doanh thu ancillary / khách | Chỉ số chính |
| Tỷ lệ gắn kèm (attach rate) theo sản phẩm | Theo từng thời điểm đề xuất |
| Tỷ lệ hoàn/khiếu nại ancillary | **Chỉ số cảnh báo** — tăng nghĩa là đang bán thứ khách không thực sự muốn |
| Tỷ lệ bỏ giỏ ở bước ancillary | Đề xuất quá nhiều sẽ làm mất cả vé |
| Contribution/chuyến | Đích cuối |

**Nếu attach rate tăng nhưng tỷ lệ hoàn/khiếu nại cũng tăng, luồng đang sai** — không phải đang thành công.

Mọi số dự kiến mang nhãn `[SỐ LIỆU MINH HỌA]` cho tới khi có dữ liệu thật.

---

## 7. CHECKLIST TRƯỚC KHI TRIỂN KHAI
- [ ] Không có ô tick sẵn ở bất kỳ bước nào
- [ ] Tổng tiền hiển thị rõ ở mọi màn hình
- [ ] Cùng sản phẩm = cùng giá cho mọi khách
- [ ] Cơ sở pháp lý cho việc dùng dữ liệu cá nhân hoá đã có
- [ ] Tối đa 1 đề xuất chính/bước
- [ ] Có cơ chế dừng khi chuyến bay gián đoạn
- [ ] Pháp chế đã duyệt cho thị trường đích
- [ ] Điều khoản SkyJoy hiển thị đúng

<!-- check-output: rules-doc -->
