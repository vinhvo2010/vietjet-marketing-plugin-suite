# THƯ VIỆN PROMPT THEO LOẠI CHIẾN DỊCH

Mọi prompt dưới đây kế thừa ràng buộc ở `SKILL.md` mục 2 và `rules/vietjet-brand-safety.md`. Thay `[...]` theo brief; **không thay bằng nội dung vi phạm chuẩn thể hiện con người**.

Màu, logo, slogan và livery phải lấy từ brandbook/asset có phiên bản đã được Brand xác nhận. Khi chưa có nguồn này, giữ placeholder và ghi rõ demo chưa xác minh nhận diện; không tự gán mã màu hoặc mô tả sản phẩm thật.

## 1. Mở tuyến mới
```
Commercial advertising photograph of a Vietjet Air airliner ([LOẠI TÀU])
with [LIVERY FROM VERIFIED AIRCRAFT REFERENCE],
banking gracefully above [MÔ TẢ CẢNH QUAN ĐẶC TRƯNG ĐIỂM ĐẾN — chung, không đích danh công trình].
Golden hour, cinematic travel poster composition, sense of arrival and possibility,
ultra-detailed, photorealistic, 8k.
```

## 2. Khuyến mãi / flash sale
```
Bold commercial travel advertising key visual, dominant [APPROVED PRIMARY BRAND COLOR]
with [APPROVED ACCENT COLOR], clean negative space reserved in the
[left third / lower third] for price and terms typography,
Vietjet Air aircraft ([LOẠI TÀU]) as hero element,
dynamic diagonal composition conveying speed and value,
high contrast, photorealistic, 8k.
```
⚠️ Phải chừa chỗ thật cho giá **và điều kiện** — không thiết kế rồi mới nhét chữ nhỏ vào.

## 3. Mùa vụ / lễ hội
```
Warm festive travel advertising photograph, Vietjet Air aircraft ([LOẠI TÀU])
in the background, foreground featuring [YẾU TỐ VĂN HOÁ MÙA VỤ — đã kiểm tra
phù hợp với thị trường đích], [COLORS FROM VERSIONED BRAND ASSETS] integrated naturally
into the seasonal palette, emotional homecoming atmosphere,
golden hour, photorealistic, 8k.
```
⚠️ Yếu tố văn hoá phải qua kiểm tra bản địa hoá — xem `skills/vietjet-global-localization/`.

## 4. Sản phẩm & dịch vụ trên không
```
Professional commercial photograph of a modern narrow-body aircraft cabin interior,
clean and bright, [SkyBoss seating / hot meal service / cabin ambience],
[CABIN DETAILS FROM VERIFIED PRODUCT REFERENCE],
natural daylight through windows, documentary advertising style,
photorealistic, 8k.
```
⚠️ **Không dùng làm mô tả sản phẩm thật nếu chưa đối chiếu cấu hình cabin thực tế.** Ghi rõ là ảnh dựng ý tưởng.

## 5. Phi hành đoàn / con người
Dùng nguyên mẫu ở `SKILL.md` mục 4.2. Các biến thể tư thế được phép:
- `assisting a passenger with overhead luggage`
- `greeting passengers at the cabin door`
- `conducting a pre-flight cabin check`
- `explaining safety information to a passenger`
- `serving refreshments in the aisle`
- `ground crew coordinating at the aircraft stand`

Không thêm biến thể ngoài danh sách này mà chưa qua duyệt.

## 6. Negative prompt chuẩn — dùng cho mọi KV có người
```
--no sexualized posing, revealing clothing, low camera angle, body-focused framing,
cropped body parts, swimwear, unrealistic body proportions, celebrity likeness,
unaccompanied children, distorted aircraft livery, incorrect aircraft type
```

<!-- check-output: rules-doc -->
