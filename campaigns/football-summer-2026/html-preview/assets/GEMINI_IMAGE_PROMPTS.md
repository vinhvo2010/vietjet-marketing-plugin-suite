# Gemini Image Generation Prompt Pack — BAY TỚI MÙA HÈ BÓNG ĐÁ

**Trạng thái tài liệu:** DỰ THẢO PHÁC THẢO QUY TRÌNH (INTERNAL WORKING DRAFT)  
**Quyết định quản trị:** Tài liệu này phục vụ phát triển nội bộ. Các hình ảnh tạo ra chỉ dùng để trình bày kịch bản (storyboard/mockup), không được sử dụng cho bất kỳ ấn phẩm truyền thông thực tế hay công bố ra bên ngoài.

---

## 1. Nguyên Tắc Quản Trị Hình Ảnh (Image Governance Rules)
Tất cả hình ảnh tạo ra bằng AI phải tuân thủ nghiêm ngặt các quy tắc loại trừ bản quyền:
*   **Không nhãn hiệu giải đấu:** Không vẽ logo FIFA, World Cup, AFC hoặc bất kỳ huy hiệu giải đấu chính thức nào.
*   **Không cúp vô địch thật:** Cấm mô phỏng hình dáng Cúp Vàng thế giới hay cúp chính thức của các giải đấu lớn.
*   **Không linh vật/khẩu hiệu:** Không vẽ mascot giải đấu hoặc khẩu hiệu chính thức.
*   **Không logo đội tuyển/áo đấu:** Mọi trang phục của nhân vật phải là trang phục thể thao hoặc du lịch generic màu đỏ-vàng, không có huy hiệu (crest) của đội tuyển quốc gia hoặc câu lạc bộ.
*   **Không gương mặt cầu thủ nổi tiếng:** Nhân vật phải là các khuôn mặt AI hư cấu ngẫu nhiên, không mô phỏng các cầu thủ bóng đá ngoài đời thực.
*   **Không chữ lồng sẵn (Typography):** Cấm AI tự động tạo văn bản, chữ viết hay logo Vietjet lên ảnh. Tất cả chữ và logo thương hiệu phải được chèn thủ công (manual placement) trong phần mềm biên tập sau khi ảnh gốc được duyệt.
*   **Không claim vé/thương mại:** Không tạo hình ảnh vé trận đấu hay có thông tin về ưu đãi thương mại.

---

## 2. Master Negative Prompt (Sử dụng cho toàn bộ các lượt sinh ảnh)
Sao chép đoạn text dưới đây vào mục Negative Prompt của Gemini ở mọi lượt tạo:
```text
no FIFA logo, no tournament branding, no official trophy, no World Cup trophy silhouette, no official mascot, no official slogan, no host city logo, no official match ball, no national team crests, no branded kits, no real player faces, no tickets, no planes, no airline livery, no distorted faces, no extra limbs, no embedded words, no generated text, no misspelled letters, no distorted logos, no clutter, no low quality, no trademarked badges, no commercial booking text, no fare information.
```

---

## 3. Danh Mục Prompt Chi Tiết (Asset-by-Asset Prompt Pack)

### A. Hero Campaign Visual
*   **Target Filename:** `hero-football-travel.png`
*   **Tỉ lệ (Aspect Ratio):** 16:9 (Wide)
*   **Vị trí hiển thị trong HTML:** Hero Banner của microsite
*   **Prompt chính:**
    ```text
    A premium commercial wide landscape key visual for an independent summer travel campaign. A joyful group of fictional young adult travelers walking forward together near a bright airport terminal boarding gate illuminated by warm morning summer sun. Abstract dynamic red and yellow motion trails uốn lượn through the air around them. A traveler holds a generic geometric football with an original custom geometric pattern. Vali, travel suitcases, and casual summer travel attire. Cinematic lighting, soft depth of field, premium travel photography style. Large safe zones at the center and top left left blank for manual text placement. --ar 16:9
    ```
*   **Typography Instruction:** Chừa trống khoảng lề trái 40% để gõ chữ tiêu đề chiến dịch và CTA.
*   **QA Checklist:** Đảm bảo không có logo giải đấu, không có chữ lỗi do AI sinh, màu đỏ-vàng chuẩn.

### B. 4:5 Social Key Visual
*   **Target Filename:** `kv-4x5-football-summer.png`
*   **Tỉ lệ (Aspect Ratio):** 4:5
*   **Vị trí hiển thị trong HTML:** Khung xem trước Key Visual
*   **Prompt chính:**
    ```text
    A high-quality 4:5 vertical commercial key visual. A close-up of a generic football with an original geometric black-and-gold design rolling across a sun-drenched airport terminal floor. Elegant abstract red and yellow ribbon trails flow smoothly around the ball, creating dynamic movement. In the background, out-of-focus silhouettes of young travelers with luggage add a sense of adventure. Editorial travel photography style, warm sun rays, clean premium composition. --ar 4:5
    ```
*   **Typography Instruction:** Logo Vietjet đặt ở góc trên bên phải, tiêu đề chiến dịch đặt ở 1/3 dưới khung hình.
*   **QA Checklist:** Họa tiết quả bóng phải generic, không có logo thương hiệu bóng đá thật.

### C. 9:16 Reels / Story Cover
*   **Target Filename:** `story-9x16-football-travel.png`
*   **Tỉ lệ (Aspect Ratio):** 9:16
*   **Vị trí hiển thị trong HTML:** Khung xem trước Reels/Story video
*   **Prompt chính:**
    ```text
    A vertical 9:16 commercial travel photo. A joyful fictional young woman in casual summer travel attire standing near an airport runway window. She is holding a generic geometric patterned football under her arm and smiling dynamically. Flowing red-yellow energy ribbons surround her, reflecting the sun. Warm summer sunlight, premium lifestyle photography, vertical composition. Safe text zones at the top and bottom. --ar 9:16
    ```
*   **Typography Instruction:** Giữ sạch chữ hoàn toàn trong khung hình gốc.
*   **QA Checklist:** Khuôn mặt nhân vật tự nhiên, tay chân đầy đủ, không có máy bay thương hiệu thật.

### D. Carousel Slide System (Tỉ lệ 4:5 từng slide)

1.  **Slide 1: Hook** (`carousel-01-hook.png`)
    *   *Prompt:* A generic custom geometric football resting on a glossy airport terminal floor, sunbeams shining through windows, red-yellow dynamic ribbons wrapping around the ball. --ar 4:5
2.  **Slide 2: Team** (`carousel-02-team.png`)
    *   *Prompt:* Fictional young adult friends high-fiving joyfully in a sun-lit airport terminal, suitcases beside them, warm summer travel mood. --ar 4:5
3.  **Slide 3: Motion** (`carousel-03-motion.png`)
    *   *Prompt:* A close-up of a suitcase wheel spinning on a runway terminal floor, red and yellow light trails uốn lượn behind it, representing speed and travel energy. --ar 4:5
4.  **Slide 4: Community** (`carousel-04-community.png`)
    *   *Prompt:* A group of young adult travelers sitting joyfully together at a beach cafe, looking at a phone screen and cheering, generic football theme, beach sunset background. --ar 4:5
5.  **Slide 5: Travel** (`carousel-05-travel.png`)
    *   *Prompt:* Fictional travelers walking down a sunny coastal road towards a beach, xách vali du lịch, red-yellow ribbon elements, joyful summer trip mood. --ar 4:5
6.  **Slide 6: Challenge** (`carousel-06-challenge.png`)
    *   *Prompt:* A creator holding a generic custom soccer ball and pointing forward in a tropical resort setting, inviting interaction, dynamic lighting. --ar 4:5
7.  **Slide 7: Closing** (`carousel-07-closing.png`)
    *   *Prompt:* Abstract red-yellow energy ribbons folding into a clean frame on a warm cream-colored textured backdrop, clear central safe zone left blank for CTA. --ar 4:5

### E. App Banner Visual
*   **Target Filename:** `app-banner-football-summer.png`
*   **Tỉ lệ (Aspect Ratio):** 3:1 (Panoramic)
*   **Vị trí hiển thị trong HTML:** In-app Banner của mobile app
*   **Prompt chính:**
    ```text
    A panoramic 3:1 banner style commercial photo. Abstract glowing red-yellow ribbon waves stretching across a warm summer sky. On the far left, a generic custom geometric football and the corner of a clean suitcase. The right 60% of the banner is a clean, blank empty space with solid cream color for manual button and text layout. Premium flat clean aesthetic. --ar 3:1
    ```
*   **Typography Instruction:** Chừa trống hoàn toàn bên phải để lập trình đặt nút "ĐẶT VÉ NGAY".

### F. Airport Screen Visual
*   **Target Filename:** `airport-screen-football-summer.png`
*   **Tỉ lệ (Aspect Ratio):** 16:9
*   **Vị trí hiển thị trong HTML:** Màn hình tại nhà ga sân bay
*   **Prompt chính:**
    ```text
    A premium 16:9 commercial landscape display photo. Fictional group of friends standing joyfully at a modern check-in counter. Bright summer sun rays filtering through the terminal glass facade. Red-yellow motion trails framing the composition. High contrast, sharp details, editorial travel photography style. Large safe zone in upper center. --ar 16:9
    ```

### G. Measurement / Dashboard Abstract Visual
*   **Target Filename:** `dashboard-funnel-abstract.png`
*   **Tỉ lệ (Aspect Ratio):** 16:9
*   **Vị trí hiển thị trong HTML:** Phần Báo cáo & Đo lường
*   **Prompt chính:**
    ```text
    A premium 16:9 abstract conceptual illustration for a commercial performance dashboard. A stylized vertical funnel represented by glowing red-yellow light beams against a clean white backdrop. Subtle abstract data charts, graphs, and percentage symbols floating in the background in clean minimal design. No text, no words, clean corporate data visualization aesthetic. --ar 16:9
    ```

---

## 4. Hướng Dẫn Kỹ Thuật (AI Generation Instructions)
1.  **Seed Consistency:** Nếu nền tảng hỗ trợ, hãy sử dụng cùng một tham số seed để giữ cho màu sắc đỏ-vàng và kiểu dáng quả bóng generic được đồng bộ qua tất cả các hình ảnh.
2.  **Độ Phân Giải:** Thiết lập độ phân giải cao nhất có thể (chọn chất lượng High-Quality / HD).
3.  **Tên File:** Khi lưu ảnh, đặt tên file chính xác theo danh sách trên (ví dụ: `hero-football-travel.png`) và lưu trực tiếp vào thư mục `/html-preview/assets/`.
