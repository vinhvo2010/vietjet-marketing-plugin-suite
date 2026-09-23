⚠️ BẢN NHÁP — CHƯA PHÁT HÀNH — CẦN NGƯỜI PHÊ DUYỆT

# Vietjet Group Marketing Operating Model v5

## Kết luận điều hành

Mô hình phù hợp nhất cho Vietjet không phải là một “siêu-agent CMO” và cũng không phải một bộ prompt theo phòng ban. Đề xuất là **VJ-GMOM**: Group Marketing Hub + các Capability Chapter + Market Pod địa phương, vận hành bằng work object có cấu trúc, dependency rõ, reviewer độc lập và cổng phê duyệt người thật.

North Star là **incremental group contribution** trong ràng buộc của customer value, future demand và operating trust. ROAS, load factor, doanh thu, lượt xem hay giá vé chỉ là chỉ số chẩn đoán.

## Vì sao mô hình này

HBS đặt nền tảng cho kế hoạch marketing bằng mục tiêu, đối tượng, value proposition và measurement; 3C giúp làm rõ customer–competitor–company. Value-based strategy nối willingness to pay với price, cost và willingness to sell. JTBD bổ sung câu hỏi khách hàng muốn tạo “tiến bộ” gì trong hoàn cảnh du lịch của họ. Vì vậy mission phải bắt đầu bằng quyết định và giá trị khách hàng, không bắt đầu bằng danh sách kênh. ([HBS Digital Marketing Plan](https://online.hbs.edu/blog/post/digital-marketing-plan), [HBS Value-Based Strategy](https://online.hbs.edu/blog/post/value-based-strategy), [HBR Jobs to Be Done](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done))

Khoa học marketing yêu cầu cân bằng tạo nhu cầu dài hạn và kích hoạt ngắn hạn, nhưng không hợp thức hóa một tỷ lệ ngân sách cố định cho mọi thị trường. Category Entry Points giúp biến brand building thành các tình huống mua cụ thể. ([IPA Binet & Field](https://ipa.co.uk/knowledge/effectiveness-research-analysis/les-binet-peter-field), [Ehrenberg-Bass CEPs](https://www.marketingscience.info/wp-content/uploads/2022/01/Identifying-and-Prioritising-CEPs.pdf))

Trong hàng không, marketing phải gắn với retailing: offer, pricing/bundling, distribution, payment, order, fulfillment và service. IATA mô tả NDC/Dynamic Offers theo logic relevant offers và dynamic bundling/continuous pricing; điều này đòi hỏi Marketing làm việc cùng RM, Distribution, Payment, Ops và CX thay vì tối ưu media độc lập. ([IATA Modern Airline Retailing](https://www.iata.org/en/programs/airline-distribution/retailing/), [IATA NDC](https://www.iata.org/en/programs/airline-distribution/retailing/ndc/), [IATA Dynamic Offers](https://www.iata.org/en/programs/airline-distribution/retailing/dynamic-offers/))

gstack chứng minh giá trị của chuỗi specialist có artifact chuyển tiếp, review độc lập và một quy trình end-to-end. VJ-GMOM chuyển logic `Think → Plan → Build → Review → Test → Ship → Reflect` sang `Sense → Choose → Design Offer → Create → Activate → Service → Measure → Learn`; đây là chuyển thể phương pháp, không phải “tiêu chuẩn chính thức của YC”. ([gstack](https://github.com/garrytan/gstack))

NIST AI RMF bổ sung vòng Govern–Map–Measure–Manage, vai trò người/AI, kiểm thử, provenance và xử lý sự cố. Vì vậy agent chỉ chuẩn bị quyết định và artifact; quyền chi tiền, đổi giá, dùng PII, phát hành và phát ngôn khủng hoảng vẫn nằm ở người và tầng quyền kỹ thuật. ([NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), [NIST GenAI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf))

## Kiến trúc tổ chức đề xuất

```
                         GROUP GROWTH COUNCIL
                     CMO + Commercial + CX + Data
                                │
         ┌──────────────────────┼──────────────────────┐
         │                      │                      │
     GROUP HUB            CAPABILITY CHAPTERS       MARKET PODS
 Portfolio & brand        Growth / Creative         Vietnam
 Standards & capital      CRM / Content / CX        Thailand entity
 AI governance            Science / BI / MarTech    Australia POS/source
 Measurement system       RM / Trade / Network      India POS/source
 Decision rights          Legal / Finance           China POS/source
                                                    Route corridors
```

Market pod không đồng nghĩa pháp nhân. Mỗi mission phải ghi một trong bốn scope: `operating_entity`, `point_of_sale`, `source_market`, `route_corridor`. Điều này quan trọng vì ngay trên nội dung thương mại Vietjet hiện hành, Australia, India và China có cách hiển thị thuế/phí và phương thức thanh toán khác nhau. ([Ví dụ chính thức Vietjet](https://www.vietjetair.com/en/pages/a-whole-new-world-a-whole-new-me-lets-vietjet-1719819814788))

## Team 18 vai trò

| Nhóm | Vai trò | Accountable output |
|---|---|---|
| Control | CMO Orchestrator | Mission brief, decision record, BOD packet |
| Strategy | Group Brand & Portfolio | Brand architecture, value proposition, portfolio choice |
| Local | Market Pod Lead | Local context, source/POS/corridor plan, native/legal gates |
| Insight | Market Intelligence | Evidence ledger, competitors, demand signals |
| Measurement | BI Data Analyst | Metrics, data contract, reporting |
| Measurement | Marketing Science & Experimentation | Incrementality, experiment card, MMM calibration |
| Retail | Revenue Management | Fare/inventory decision input |
| Retail | Trade, Distribution & Sales | Channel economics and partner plan |
| Economics | Finance & Cost Control | Contribution and sensitivity |
| Operations | Flight Ops & Network | Operational feasibility |
| Experience | Customer Journey & Experience | Promise-to-delivery journey and recovery |
| Activation | Performance & Growth | Paid demand capture draft/configuration |
| Activation | Creative Studio | Asset concepts and production brief |
| Activation | CRM, SkyJoy & Ancillary | Lifecycle and transparent ancillary journeys |
| Activation | Content & Organic Discovery | SEO/GEO/AEO and reusable knowledge assets |
| Trust | PR, Social & Crisis | Reputation and crisis drafts |
| Trust | Legal & Regulatory | Preliminary current-law review |
| Enablement | MarTech & AI Operations | Tool rights, audit, router, release and kill-switch controls |

## Hệ đo lường

| Cấp | Câu hỏi | Phương pháp ưu tiên |
|---|---|---|
| Enterprise | Marketing có tạo đóng góp tăng thêm không? | Contribution, customer profitability, calibrated MMM |
| Market/corridor | Nhu cầu tương lai và hiện tại thay đổi ra sao? | Brand/CEP tracker, geo/holdout tests, search/direct demand |
| Journey | Promise có được giao đúng không? | Conversion, disruption contacts, refund/recovery, repeat |
| Channel | Kênh nào tạo giá trị tăng thêm? | Experiments + attribution chẩn đoán + channel cost |
| Agent | Team có đáng tin và nhanh hơn không? | Cycle time, rework, unsupported claims, gate escapes, human override |

MMM là mô hình quan sát; experiment tốt hơn cho causal question hẹp và attribution chủ yếu dùng cho tối ưu chẩn đoán. Meridian hỗ trợ MMM tổng hợp và hiệu chỉnh bằng experiment nhưng vẫn yêu cầu giả định nhân quả minh bạch. ([Google Meridian](https://github.com/google/meridian), [Causal methodology](https://developers.google.com/meridian/docs/causal-inference/about-mmm-causal-inference-methodology))

## Lộ trình 90 ngày

### Ngày 0–30 — Khóa mô hình và quyền

- Điền RACI và người duyệt thật cho spend, pricing, publication, PII, crisis và route claims.
- Chọn hai mission mẫu: một route corridor và một lifecycle/ancillary journey.
- Chuẩn hóa Mission Brief, Evidence Ledger, Experiment Card, Release Packet và Learning Record.
- Baseline cycle time, cost, error/rework và business KPI; không đặt uplift giả.

### Ngày 31–60 — Pilot coordinated team

- Chạy router v5 cho hai mission ở chế độ draft-only.
- Bật source registry, current-law check, reviewer độc lập và artifact store.
- Thử nghiệm tăng thêm có control/holdout; không dùng platform ROAS làm causal proof.
- Diễn tập kill-switch và kiểm tra quyền tối thiểu.

### Ngày 61–90 — Closed-loop có giới hạn

- Kết nối dữ liệu aggregate đã allow-list và audit log.
- Nối result vào Learning Record rồi cập nhật brief/decision tiếp theo.
- Chỉ tự động hóa Two-Way Door có rollback; mọi One-Way Door dùng approval token người thật.
- Hội đồng review go/no-go cho mở rộng thị trường và connector.

## Điều chưa thể tuyên bố

Bản v5 đạt bằng chứng cục bộ cho **Level 2 — Coordinated Team**: 18 role contracts, router, dependency waves, typed mission/handoff, research ledger và tests. Chưa có bằng chứng để tuyên bố Level 3/4 vì chưa kết nối dữ liệu thật, quyền người dùng thật, hệ thống phát hành, spend controls và production experiment.

Phần pháp lý là checklist vận hành, không phải tư vấn pháp lý. Đặc biệt, Việt Nam đã có Luật 91/2025/QH15 hiệu lực từ 2026-01-01; Australia có APP 7/Spam Act; India dùng DPDP Rules 2025 theo lộ trình; Thailand và China cần kiểm tra bản địa/current-law trước mỗi release. ([Việt Nam](https://vanban.chinhphu.vn/?classid=1&docid=214590&orggroupid=1&pageid=27160), [OAIC](https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/organisations/direct-marketing), [India MeitY](https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa?pageTitle=Digital-Personal-Data-Protection-Rules-2025), [Thailand CAAT](https://www.caat.or.th/aviation/passenger/consumer-protection/law-regulation/), [China PIPL](https://www.npc.gov.cn/npc/c2597/c5854/bfflywwb/202311/t20231117_433007.html))
