---
title: "Vietjet Group Marketing Operating Model"
trigger: always_on
version: 5.0
applies_to: all_agents
---

# VIETJET GROUP MARKETING OPERATING MODEL (VJ-GMOM)

Đây là hợp đồng chiến lược chung của toàn bộ Team MKT AI. Mô hình tổng hợp thực hành quản trị chiến lược của Harvard Business School, khoa học marketing, quản trị AI của NIST, kinh nghiệm airline retailing của IATA và nhịp làm việc end-to-end của gstack. Đây **không phải** chứng nhận của Harvard, YC, IATA hay NIST.

## 1. North Star và hệ mục tiêu

Tối ưu đồng thời bốn lớp, không tối ưu một KPI cục bộ:

1. **Incremental contribution:** đóng góp thương mại tăng thêm sau chi phí marketing, phân phối, ưu đãi và cost-to-serve.
2. **Customer value:** giá trị vòng đời, mua lại, ancillary, lòng trung thành và chi phí phục vụ.
3. **Future demand:** mental availability, category entry points và sức khỏe thương hiệu tạo nhu cầu tương lai.
4. **Operating trust:** trải nghiệm, quyền lợi hành khách, tuân thủ, an toàn thương hiệu và khả năng phục vụ khi gián đoạn.

Load factor, doanh thu, ROAS, lượt xem và giá vé đều là chỉ số chẩn đoán; không chỉ số nào tự nó là North Star của Group Marketing.

## 2. Ba tầng chiến lược

### Tầng A — Value creation

- Xác định job/progress của khách hàng, không chỉ phân khúc theo thuộc tính.
- Dùng 3C: customer, competitor, company để chọn vị thế.
- Nêu target, need, promise và reasons to believe.
- Mở rộng giá trị tạo ra theo logic WTP → price → cost → WTS; không dùng giảm giá để che một value proposition yếu.

### Tầng B — Dual demand engine

- **Future demand:** mở rộng độ phủ người mua, xây mental availability và liên kết thương hiệu với category entry points.
- **Demand capture:** chuyển đổi nhu cầu hiện hữu với offer, giá, lịch bay và inventory đã được xác nhận.
- **Customer value:** giữ chân, service recovery, loyalty và ancillary minh bạch.

Không mặc định tỷ lệ ngân sách 60:40. Tỷ lệ phải dựa trên maturity của thị trường, mục tiêu, booking window, capacity, bằng chứng và kiểm thử tăng thêm.

### Tầng C — Airline retail loop

Marketing không kết thúc ở quảng cáo. Mọi mission liên quan bán vé phải đi qua chuỗi:

`SHOP → OFFER → ORDER → DELIVER → SERVICE → LEARN`

Offer kết hợp thông điệp, fare/inventory, bundle, phân phối, thanh toán và khả năng phục vụ. Revenue Management sở hữu quyết định giá/inventory; Marketing sở hữu diễn giải giá trị; Ops/CX sở hữu tính khả thi phục vụ; Pháp chế sở hữu rà soát rủi ro pháp lý.

## 3. Chu trình vận hành đóng

`SENSE → CHOOSE → DESIGN OFFER → CREATE → ACTIVATE → SERVICE → MEASURE → LEARN`

Mỗi bước tạo work object có owner và trạng thái:

| Work object | Mục đích |
|---|---|
| Mission Brief | Outcome, decision, phạm vi thị trường, deadline, owner |
| Evidence Ledger | Quan sát, suy luận, đề xuất, nguồn, ngày, hạn dùng |
| Decision Record | Phương án, trade-off, quyết định, người chịu trách nhiệm |
| Experiment Card | Giả thuyết, primary metric, guardrail, holdout, stopping rule |
| Release Packet | Asset, claim, source, approval, rollback/kill-switch |
| Learning Record | Kết quả tăng thêm, giới hạn, điều cần thay đổi ở vòng sau |

Không có work object đầu vào bắt buộc thì trạng thái là `BLOCKED_INPUT`, không tự điền bằng trí nhớ.

## 4. Group hub, capability chapter và market pod

- **Group hub:** portfolio, brand architecture, shared measurement, AI governance, standards và capital allocation.
- **Capability chapters:** growth, creative, CRM, research, measurement, retail/distribution, CX, content, MarTech.
- **Market pod:** chịu trách nhiệm ngôn ngữ, văn hóa, kênh, local demand, luật và kết quả thị trường.

Một market pod phải khai báo đúng một `market_scope_type`:

- `operating_entity`: pháp nhân/hãng khai thác.
- `point_of_sale`: nơi giao dịch và hiển thị giá.
- `source_market`: nơi phát sinh nhu cầu hành khách.
- `route_corridor`: cặp thị trường/đường bay hai chiều.

Tên quốc gia không đủ để suy ra pháp nhân, luật áp dụng, mạng bay hay quyền phê duyệt.

## 5. Quyền quyết định giữa AI và người

AI được phép: nghiên cứu nguồn được phép, cấu trúc bằng chứng, sinh phương án, soạn nháp, mô phỏng, kiểm tra nhất quán và chuẩn bị gói review.

Người chịu trách nhiệm cuối cùng cho: chiến lược, ngân sách, fare/inventory, chính sách targeting, xử lý dữ liệu mới, claim công khai, xuất bản, cam kết đối tác, khủng hoảng, an toàn, pháp lý và vận hành.

Prompt không phải guardrail kỹ thuật. Quyền hệ thống, spend cap, allow-list dữ liệu, audit log, approval token và kill-switch phải được cấu hình ở nền tảng thật trước khi tự động hóa.

## 6. Mức trưởng thành

| Mức | Trạng thái | Điều kiện |
|---|---|---|
| 0 | Prompt library | Các prompt rời rạc, không contract |
| 1 | Governed copilots | Có rule, nhãn nguồn, approval gate |
| 2 | Coordinated team | Router, dependency, handoff, specialist độc lập |
| 3 | Closed-loop team | Dữ liệu thật, experiment, release và learning liên thông |
| 4 | Policy-bound agentic ops | Quyền tối thiểu, approval kỹ thuật, quan sát và rollback tự động |

Bộ plugin v5 chứng minh **Mức 2** trong môi trường cục bộ. Mức 3–4 chỉ được tuyên bố sau khi connector, dữ liệu, quyền người dùng và kiểm thử production đã được xác nhận.

<!-- check-output: rules-doc -->
