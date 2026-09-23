---
name: vietjet-brand-mastery
description: "Soạn và review Key Visual demo, poster, banner hoặc prompt hình ảnh Vietjet; đối chiếu brandbook do người dùng cung cấp và đánh dấu phần chưa xác minh. Bao gồm quy tắc thể hiện con người và điều kiện duyệt trước phát hành; không chứng nhận thiết kế đạt chuẩn thương hiệu."
---

# 🎨 VIETJET BRAND MASTERY & KEY VISUAL GENERATION

## 0. NẠP TRƯỚC — BẮT BUỘC
`../../rules/vietjet-brand-safety.md` — đặc biệt **mục 2: Chuẩn thể hiện con người**.
`../../rules/vietjet-source-and-expiry.md` mục 3 — đội tàu (nguồn sự thật duy nhất).

Không nạp được → nói rõ và không sinh ảnh có người.

---

## 1. NHẬN DIỆN THƯƠNG HIỆU

**Màu tham chiếu chưa xác nhận brandbook:** Đỏ `#E30613` · Vàng `#FFD100` · Trắng `#FFFFFF`.
**Slogan tham chiếu chưa xác nhận phạm vi sử dụng:** "Bay là thích ngay!" — EN: "Enjoy Flying!".

Trước khi kết luận "đúng nhận diện", cần brandbook/asset gốc có phiên bản và chủ sở hữu xác nhận. Nếu thiếu, chỉ tạo demo và liệt kê thành phần đang dùng theo giả định.

**Tàu bay:** đối chiếu ảnh/asset chính thức của đúng hãng khai thác và loại tàu; không dùng mô tả màu sơn chung để xác nhận cấu hình thật.
⚠️ **Loại tàu phải khớp với loại thực khai thác trên đường bay được quảng cáo.** Không tự chọn — tra `../../rules/vietjet-source-and-expiry.md`, hỏi Flight Ops khi không chắc.

**Đồng phục phi hành đoàn:** theo bộ nhận diện chính thức của hãng. Thể hiện **đúng, đầy đủ, chỉnh tề**, không biến thể.

---

## 2. ⚠️ CHUẨN THỂ HIỆN CON NGƯỜI — ĐỌC TRƯỚC KHI VIẾT PROMPT

Áp dụng đầy đủ `../../rules/vietjet-brand-safety.md` mục 2. Tóm tắt điều kiện cứng:

✅ **Bắt buộc có**
- Phi hành đoàn trong **tư thế nghề nghiệp**: đang làm việc, phục vụ, hướng dẫn khách
- Góc máy **ngang tầm mắt**; khung hình toàn thân hoặc từ ngực trở lên
- Nam và nữ cùng mức độ trang phục, cùng loại tư thế, cùng vai trò nghề nghiệp
- Biểu cảm tự nhiên, chuyên nghiệp, thân thiện

❌ **Cấm trong prompt**
`bikini` · `swimsuit` · `sexy` · `seductive` · `alluring` · `curvy` · `revealing` · `low angle` với chủ thể người · mọi từ mô tả cơ thể hoặc độ hở · đồng phục trong bối cảnh không phải làm việc · khuôn mặt người thật/người nổi tiếng/nhân vật có bản quyền · trẻ em không có người lớn trong khung hình

**Phép thử đối xứng:** đổi giới tính nhân vật trong đầu — nếu bức ảnh trở nên bất thường, bức ảnh đó sai.

**Mọi KV có hình người là One-Way Door.** Sinh xong phải gắn cờ chờ duyệt trước khi rời phạm vi nội bộ.

---

## 3. ĐỊNH DẠNG XUẤT

| Tỷ lệ | Dùng cho |
|---|---|
| 16:9 | Website banner, YouTube thumbnail, Facebook cover, billboard LED |
| 9:16 | Story, Reels, TikTok |
| 1:1 / 4:3 | Instagram feed, Facebook carousel |

---

## 4. CÔNG THỨC PROMPT

### 4.1 KV không có người (mặc định — dùng khi được)
```
Commercial advertising photograph of a Vietjet Air airliner
([LOẠI TÀU — tra nguồn sự thật, khớp đường bay])
with [LIVERY FROM VERIFIED AIRCRAFT REFERENCE; OTHERWISE CONCEPT ONLY],
flying over [MÔ TẢ CẢNH QUAN CHUNG — bờ biển nhiệt đới / dãy núi tuyết /
phố cổ mái ngói — KHÔNG nêu đích danh công trình khi chưa có clearance].
Golden hour warm lighting, cinematic travel poster style,
ultra-detailed, photorealistic, vibrant tourism aesthetic, 8k resolution.
```

### 4.2 KV có phi hành đoàn (cần duyệt trước khi rời nội bộ)
```
Professional commercial photograph of Vietjet Air cabin crew
in full standard uniform, at work in an aircraft cabin,
[assisting a passenger with overhead luggage / greeting passengers at
the cabin door / conducting a pre-flight cabin check].
Eye-level camera angle, full or three-quarter body framing,
natural professional expression, warm cabin lighting,
brand colors [FROM VERSIONED BRAND ASSETS; OTHERWISE UNVERIFIED CONCEPT],
photorealistic, respectful documentary advertising style, 8k resolution.
```

### 4.3 Quy tắc địa danh
Mọi công trình/địa danh nêu đích danh trong KV thương mại phải qua kiểm tra quyền sử dụng hình ảnh — `[CẦN XÁC MINH — Pháp chế]` cho từng chiến dịch. Mặc định dùng mô tả cảnh quan chung.

---

## 5. GIÁ TRONG KEY VISUAL

Mọi KV có giá phải hiển thị **giá đã gồm thuế và phí bắt buộc**, hoặc nêu điều kiện **ngay trong cùng khung hình** — không đẩy xuống chữ nhỏ chân trang.

Vé "0đ" phải ghi rõ: chưa gồm thuế phí · số lượng ghế · điều kiện · thời gian bay áp dụng.

Yêu cầu pháp lý cứng ở Úc (all-in pricing, ACL s48; bait advertising, ACL s35) và có quy định tương ứng ở nhiều thị trường. Chuyển agent 12 trước khi chạy.

---

## 6. TRẠNG THÁI ẢNH — BẮT BUỘC PHÂN BIỆT

Luôn nêu rõ ảnh nào **đã thực sự sinh** bằng `generate_image` trong phiên này, và ảnh nào mới chỉ là **prompt chưa chạy**. Không mô tả ảnh bằng lời rồi trình bày như đã có ảnh.

Nếu tool không khả dụng: *"Chưa sinh được ảnh demo do tool generate_image không khả dụng trong phiên này. Dưới đây là prompt để chạy."*

**Ảnh AI không được dùng làm hình ảnh sản phẩm thật** (cấu hình cabin, ghế, suất ăn) nếu chưa đối chiếu sản phẩm thực tế.

---

## 7. THAM CHIẾU
- `references/prompt-library.md` — thư viện prompt theo mùa vụ & loại chiến dịch
- `references/kv-checklist.md` — checklist duyệt trước khi ship
- `../../rules/vietjet-brand-safety.md` — chuẩn đầy đủ

<!-- check-output: rules-doc -->
