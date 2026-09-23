---
name: vietjet-campaign-orchestration
description: "SOP điều phối chiến dịch thương mại Vietjet Air theo tải ghế — quy tắc pacing, cấu trúc flash sale và vé khuyến mãi hợp quy, chuẩn UTM và khung đo lường, quy tắc auto-scale/auto-kill. Dùng khi lập chiến dịch đẩy tải, flash sale, mở tuyến, hoặc khi cần quyết định tăng/giảm ngân sách theo booking curve."
---

# ⚙️ SOP ĐIỀU PHỐI CHIẾN DỊCH THEO TẢI GHẾ

`PLUGIN_ROOT` là thư mục chứa `plugin.json` của bản plugin đang nạp skill này. Mọi đường dẫn `../../...` tính từ thư mục chứa chính `SKILL.md`, không từ thư mục dự án đang mở. Nếu host không nêu đường dẫn skill, lấy `source.path` của bản đang bật từ `codex plugin list --json`; kiểm tra `PLUGIN_ROOT/rules/00_INDEX.md` trước khi đọc. Không xác định được thì báo thiếu và dừng.

## 0. NẠP TRƯỚC
`../../rules/vietjet-data-integrity.md` · `../../rules/vietjet-governance-gates.md` · `../../rules/vietjet-brand-safety.md` mục 4 (giá).

---

## 1. NGUYÊN TẮC NỀN

**Marketing phục vụ đường bay, không phục vụ chỉ số marketing.** Mục tiêu cuối là **contribution của chuyến bay**, không phải load factor, không phải reach, không phải earned media value.

Một chuyến đầy khách ở mức giá dưới điểm hoà vốn là lỗ nhanh hơn — không phải thành công.

---

## 2. ĐIỀU PHỐI THEO BOOKING CURVE

Ngân sách và loại vé đẩy phụ thuộc vào **khoảng cách giữa tải thực tế và tải mục tiêu tại cùng thời điểm trong booking curve** — không phụ thuộc vào load factor tuyệt đối.

| Tình trạng | Hành động marketing | Loại vé đẩy |
|---|---|---|
| Tải **vượt** đường cong mục tiêu | Giảm chi tiêu; chuyển sang bán ancillary & hạng cao | SkyBoss, Deluxe, ancillary |
| Tải **bám sát** đường cong | Duy trì; tối ưu hiệu suất | Eco, ancillary |
| Tải **dưới** đường cong (khoảng cách vừa) | Tăng chi tiêu có kiểm soát; mở rộng tệp | Eco, Deluxe |
| Tải **dưới xa** đường cong, gần ngày bay | Cân nhắc flash sale — **cần Revenue Management quyết**, không phải Marketing | Vé khuyến mãi |

`[CẦN XÁC MINH — Revenue Management]` Ngưỡng cụ thể của "vừa" và "xa" theo từng loại tuyến và mùa vụ. Marketing **không tự đặt ngưỡng này**.

**Ranh giới vai trò:** Revenue Management sở hữu quyết định giá và mở fare bucket. Marketing sở hữu việc truyền thông quyết định đó. Không đảo ngược.

---

## 3. FLASH SALE & VÉ KHUYẾN MÃI — YÊU CẦU HỢP QUY

Vé 0đ và giá khuyến mãi là công cụ mạnh và cũng là rủi ro pháp lý lớn nhất trong marketing hàng không.

### Bắt buộc chốt TRƯỚC khi chạy quảng cáo
- [ ] Giá quảng cáo **đã gồm hay chưa gồm** thuế và phí bắt buộc — nêu rõ, hiển thị cùng khung hình
- [ ] **Số lượng ghế** áp dụng mỗi chuyến hoặc toàn chiến dịch
- [ ] **Thời gian mở bán** và **thời gian bay áp dụng** (travel window)
- [ ] **Ngày loại trừ** (blackout dates)
- [ ] Hành lý xách tay bao nhiêu kg; có phụ phí thanh toán không
- [ ] Điều kiện đổi/hoàn
- [ ] **Bằng chứng tồn kho (substantiation)** được lưu lại — chứng minh vé thực sự có ở mức giá quảng cáo
- [ ] Đã qua agent 12 (`legal_regulatory_compliance`) cho từng thị trường

Thiếu bất kỳ mục nào → `[DECISION REQUIRED]`, không chạy.

### Vì sao substantiation quan trọng
Quảng cáo một mức giá mà thực tế gần như không có vé ở mức đó là hành vi bị nhiều cơ quan quản lý xử phạt (ở Úc: bait advertising, ACL s35). Bằng chứng tồn kho phải được lưu **tại thời điểm quảng cáo chạy**, không dựng lại sau.

---

## 4. CHUẨN UTM

```
utm_source   = meta | google | tiktok | email | sms | affiliate | ota_<tên>
utm_medium   = cpc | cpm | display | video | social_organic | email | sms
utm_campaign = <thị_trường>_<tuyến>_<loại>_<YYYYMM>
               vd: vn_sgn-bkk_flashsale_202609
utm_content  = <định_dạng>_<biến_thể>     vd: 9x16_video_a
utm_term     = <tệp hoặc từ khoá>
```

Quy tắc: chữ thường, dùng `_` ngăn từ và `-` trong mã sân bay. **Một chiến dịch = một `utm_campaign`** xuyên mọi kênh, để so sánh được.

---

## 5. KHUNG ĐO LƯỜNG

Chuỗi bắt buộc: `hiển thị → click → tìm chuyến → chọn vé → thanh toán → bay`

| Nhóm | Chỉ số |
|---|---|
| Hiệu quả chi tiêu | CAC tới **booking hoàn tất** (không phải tới click) · ROAS · CPA theo bước funnel |
| Đóng góp đường bay | Contribution/chuyến · RASK · doanh thu ancillary/khách · điểm hoà vốn |
| Chất lượng | Tỷ lệ huỷ/hoàn sau đặt · chi phí CSKH phát sinh · tỷ lệ khiếu nại về giá |
| Kênh | Tỷ trọng đặt trực tiếp (app/web) · chi phí theo kênh phân phối |

**Không dùng làm chỉ số thành công chính:** reach, impression, earned media value, số follower.

Mọi chỉ số **dự kiến** luôn mang nhãn `[SỐ LIỆU MINH HỌA]` cho tới khi có dữ liệu thật từ nền tảng.

---

## 6. AUTO-SCALE / AUTO-KILL

> ⚠️ **Agent KHÔNG có quyền bật, tăng, hay giảm chi tiêu thật.** Tiền đã tiêu không lấy lại được — đây là One-Way Door theo `../../rules/vietjet-governance-gates.md` mục 2.3. Agent **đề xuất** quy tắc; người **cấu hình và bấm**.

### Khung quy tắc đề xuất (ngưỡng cần Tài chính + Marketing chốt)
`[CẦN XÁC MINH]` các giá trị dưới đây là **khung trống**, không phải khuyến nghị số:

- **Auto-kill** một biến thể quảng cáo khi: CPA vượt ngưỡng ___ trong ___ giờ liên tiếp với tối thiểu ___ lượt chuyển đổi.
- **Auto-scale** khi: CPA dưới ngưỡng ___ và ROAS trên ___ trong ___ ngày liên tiếp; mức tăng tối đa ___%/ngày.
- **Trần chi tiêu cứng** cấu hình tại tầng nền tảng quảng cáo: ___/ngày, ___/chiến dịch.

**Trần chi tiêu phải được đặt ở tầng nền tảng (spend cap), không chỉ ở tầng prompt.** Guardrail bằng văn bản không chặn được chi tiêu.

### Kill-switch khủng hoảng
Mọi chiến dịch phải có phương án dừng toàn bộ trong ≤ 5 phút, 24/7. Xem `../vietjet-crisis-shield/SKILL.md` mục 3. **Kiểm tra tình trạng khủng hoảng đang mở trước mỗi lần lên lịch đăng bài.**

---

## 7. CHECKLIST TRƯỚC KHI CHẠY

- [ ] Revenue Management đã xác nhận giá & tồn kho
- [ ] Flight Ops đã xác nhận đường bay, loại tàu, lịch
- [ ] Legal đã duyệt cho từng thị trường đích
- [ ] KV đã qua checklist brand (`vietjet-brand-mastery/references/kv-checklist.md`)
- [ ] UTM đã chuẩn hoá, tracking đã kiểm tra hoạt động
- [ ] Bằng chứng tồn kho đã sẵn sàng lưu
- [ ] Trần chi tiêu đã cấu hình tại nền tảng
- [ ] Kill-switch đã xác nhận có người trực
- [ ] Không có khủng hoảng nào đang mở
- [ ] Người phê duyệt chi tiêu đã ký

<!-- check-output: rules-doc -->
