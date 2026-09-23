# HỒ SƠ THỊ TRƯỜNG — OPERATING BASELINE V5

Ngày nghiên cứu nguồn công khai: 2026-09-07. Đây là **baseline định tuyến**, không phải market plan hoàn chỉnh và không thay tư vấn pháp lý. Mọi route, fare, schedule, market behavior, platform và điều khoản luật phải được tra lại trong phiên sử dụng.

## 1. Phân loại scope bắt buộc

Không biến tên một quốc gia thành một “business unit” giả định. Mỗi brief chọn đúng một loại:

| `market_scope_type` | Dùng khi | Ví dụ |
|---|---|---|
| `operating_entity` | Pháp nhân/hãng khai thác có P&L và quyền phê duyệt riêng | Vietjet Air; Thai Vietjet sau khi nội bộ xác nhận |
| `point_of_sale` | Giá, thuế/phí, currency, payment và luật giao dịch phụ thuộc nơi bán | Australia POS |
| `source_market` | Nhu cầu outbound, ngôn ngữ, kênh và customer job tại nơi xuất phát | India source market |
| `route_corridor` | Hai đầu thị trường cùng tác động tới route economics/journey | Vietnam–Australia corridor |

Nếu chưa xác định được pháp nhân khai thác: ghi `[CẦN XÁC MINH — Thương mại]`; không tự suy ra từ tên thương hiệu.

## 2. Việt Nam

- Scope thường gặp: `operating_entity`, `point_of_sale`, `source_market` hoặc đầu corridor; phải chọn cụ thể.
- Privacy baseline: Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 có hiệu lực 2026-01-01. Nghị định hướng dẫn hiện hành phải được Pháp chế tra lại trước khi triển khai xử lý mới. Nguồn: [Cổng văn bản Chính phủ](https://vanban.chinhphu.vn/?classid=1&docid=214590&orggroupid=1&pageid=27160), [PDF nghị định triển khai](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/356-nd.signed.pdf).
- Commercial baseline: route, fare, schedule và promotion chỉ dùng nguồn booking/website/chính sách nội bộ còn hạn; không lấy ví dụ trong skill làm dữ liệu thật.
- Gate bắt buộc: Pháp chế Việt Nam, owner RM cho fare/inventory, Network/Ops cho lịch/tàu, người bản ngữ cho claim.
- Chưa có dữ liệu công khai đủ tin cậy trong suite để kết luận segment ưu tiên, platform mix hay budget split.

## 3. Thái Lan

- Scope: tách `operating_entity` (nếu mission thuộc Thai Vietjet) khỏi Thailand POS/source market và Thailand–Vietnam corridor.
- Privacy baseline: Personal Data Protection Act B.E. 2562 (2019); bản dịch tiếng Anh được nguồn chính thức ghi là không chính thức, văn bản tiếng Thái có hiệu lực pháp lý. Nguồn: [Thailand MDES PDF](https://www.mdes.go.th/uploads/tinymce/source/%E0%B8%AA%E0%B8%84%E0%B8%AA/%E0%B8%AB%E0%B8%99%E0%B8%B1%E0%B8%87%E0%B8%AA%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B8%8E%E0%B8%AB%E0%B8%A1%E0%B8%B2%E0%B8%A2%E0%B8%84%E0%B8%B8%E0%B9%89%E0%B8%A1%E0%B8%84%E0%B8%A3%E0%B8%AD%E0%B8%87%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%20%282%29.pdf).
- Passenger-rights/fare baseline: CAAT publishes current passenger-rights regulations and ticket-sale guidance; current rule and effective date must be captured in the release packet. Nguồn: [CAAT regulations](https://www.caat.or.th/aviation/passenger/consumer-protection/law-regulation/), [CAAT sales guidance](https://www.caat.or.th/wp-content/uploads/2025/09/Passenger-Rights-Protection-Guidance-Material.pdf).
- Gate bắt buộc: Thai legal owner, Thai native-language reviewer, entity owner, CAAT/current-rule verification.
- Không dùng profile này để suy ra đối thủ, platform, lễ hội hay route hiện hành.

## 4. Australia

- Scope mặc định an toàn: `point_of_sale`, `source_market` hoặc `route_corridor`; không coi “Vietjet Australia” là operating entity nếu nội bộ chưa xác nhận.
- Privacy/direct marketing baseline: OAIC nêu APP 7 áp dụng cho direct marketing; email/SMS còn chịu Spam Act và cần cơ chế opt-out dễ dùng. Nguồn: [OAIC direct marketing](https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/organisations/direct-marketing), [APP Guidelines](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines).
- Fare-display baseline: mọi asset phải qua checklist total-price/mandatory-charge hiện hành của Legal; không sao chép cách hiển thị của thị trường khác.
- Vietjet public observation: trang khuyến mãi hiện hành minh họa Australia bằng giá AUD đã bao gồm thuế/phí và PayID, khác một số POS khác. Đây là tín hiệu cần local rule, không phải template giá vĩnh viễn. Nguồn: [Vietjet official promotion](https://www.vietjetair.com/en/pages/a-whole-new-world-a-whole-new-me-lets-vietjet-1719819814788).
- Gate bắt buộc: Australia legal reviewer, English copy reviewer, RM/POS owner và payment owner.

## 5. India

- Scope mặc định an toàn: `point_of_sale`, `source_market` hoặc `route_corridor`; operating entity phải có xác nhận nội bộ riêng.
- Privacy baseline: Digital Personal Data Protection Rules, 2025 có triển khai theo giai đoạn. Agent phải ghi phase đang hiệu lực ở ngày phát hành và không giả định toàn bộ rule đã có hiệu lực đồng thời. Nguồn: [MeitY rules page](https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa?pageTitle=Digital-Personal-Data-Protection-Rules-2025), [official gazette PDF](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf).
- Vietjet public observation: trang promotion có routes/currency/fare treatment theo India POS; đây là dữ liệu thương mại có hạn dùng và phải re-check ngay trước release. Nguồn: [Vietjet official promotion](https://www.vietjetair.com/en/pages/a-whole-new-world-a-whole-new-me-lets-vietjet-1719819814788).
- Language/culture/channel: `[CẦN XÁC MINH — Market Pod + native reviewer]`; “India” không phải một profile ngôn ngữ duy nhất.
- Gate bắt buộc: local-current legal review, native reviewer theo audience thực, RM/POS owner, route owner.

## 6. Mainland China

- Scope mặc định an toàn: `point_of_sale`, `source_market` hoặc `route_corridor`; không suy ra operating entity.
- Privacy baseline: Personal Information Protection Law. Nội dung áp dụng, chuyển dữ liệu và consent phải được local counsel xác nhận trên văn bản tiếng Trung hiện hành. Nguồn: [NPC PIPL English page](https://www.npc.gov.cn/npc/c2597/c5854/bfflywwb/202311/t20231117_433007.html).
- Advertising baseline: claim giá, tồn kho, so sánh và khuyến mãi phải được legal reviewer kiểm trên luật/quy định hiện hành; không dùng bản dịch cũ như kết luận cuối.
- Vietjet public observation: trang promotion minh họa China POS bằng CNY, fare treatment và Alipay; tất cả đều là dữ liệu có hạn dùng. Nguồn: [Vietjet official promotion](https://www.vietjetair.com/en/pages/a-whole-new-world-a-whole-new-me-lets-vietjet-1719819814788).
- Map, địa danh, biểu tượng và ngôn ngữ: high-risk localization; cần native reviewer + Legal trước khi asset rời nội bộ.
- Gate bắt buộc: local counsel/current Chinese text, native reviewer, RM/POS owner, payment/distribution owner.

## 7. Checklist dùng profile

Trước khi Market Pod trả `READY`, phải điền:

```
Market scope type:
Operating entity (nếu áp dụng):
Point of sale:
Source market:
Route corridor:
Applicable language/audience:
Current route/fare/schedule source + timestamp:
Current legal sources + retrieval date:
Native reviewer:
Legal reviewer:
RM/Inventory owner:
Approval status:
```

Thiếu một trường làm thay đổi giá, claim, luật hoặc quyền phát hành → `BLOCKED_INPUT` hoặc `BLOCKED_APPROVAL`.

<!-- check-output: rules-doc -->
