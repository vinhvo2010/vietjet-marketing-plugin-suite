---
title: "Agent Collaboration and Handoff Contract"
trigger: always_on
version: 5.0
applies_to: all_agents
---

# HỢP ĐỒNG PHỐI HỢP TEAM MKT AI

## 1. Điều phối theo dependency, không theo phòng ban

Mỗi mission được chạy theo các wave. Chỉ chạy song song khi đầu vào không phụ thuộc nhau.

| Wave | Mục tiêu | Vai trò điển hình |
|---|---|---|
| 0 CONTROL | khóa brief, risk tier và decision owner | CMO Orchestrator, MarTech & AI Ops |
| 1 SENSE | dựng facts và customer/market context | Market Intelligence, BI, Market Pod |
| 2 CHOOSE | chọn value proposition, offer và economics | Brand Portfolio, RM, Finance, Network, Trade |
| 3 DESIGN | tạo journey, nội dung và activation | CX, Performance, Creative, CRM, Organic Discovery |
| 4 ASSURE | kiểm incrementality, claim, luật và release controls | Marketing Science, Legal, MarTech |
| 5 SYNTHESIZE | tổng hợp decision record và gói phê duyệt | CMO Orchestrator |

Mission khủng hoảng dùng luồng riêng: `CONTROL → FACTS → HUMAN CRISIS COMMAND → DRAFT/REVIEW`. Không tự kích hoạt chiến dịch thường trong luồng này.

## 2. Handoff bắt buộc

Mọi specialist trả về đúng sáu trường:

```
STATUS: READY | PARTIAL | BLOCKED_INPUT | BLOCKED_APPROVAL | ESCALATED
DECISION: quyết định mà output hỗ trợ
EVIDENCE: claim IDs và nguồn đã dùng
OUTPUT: artifact hoặc nội dung bàn giao
APPROVALS: cổng người còn thiếu
NEXT: agent/owner tiếp theo và input họ nhận
```

Không được biến `PARTIAL` thành `READY` khi tổng hợp. CMO giữ nguyên uncertainty và provenance từ specialist.

## 3. Reviewer độc lập

- Người/agent tạo output không tự xác nhận output của chính mình.
- Marketing Science review logic đo lường và tăng thêm.
- Legal review claim, giá, privacy và quyền lợi hành khách.
- Brand Portfolio review tính nhất quán hệ thương hiệu.
- CX review promise-to-delivery và service recovery.
- MarTech review quyền công cụ, auditability, rollback và kill-switch.

Review không chỉ sửa văn phong; phải kiểm claim, failure mode và điều kiện phát hành.

## 4. Dữ liệu tối thiểu để dispatch

Mission phải có: `mission_id`, `objective`, `decision_required`, `market`, `market_scope_type`, `risk_tier`. Route launch thêm `route_or_corridor`; action có thời hạn thêm `deadline`.

Router chỉ đề xuất team và dependency. Router không cấp quyền chi tiền, phát hành, dùng PII, đổi giá hay cam kết lịch bay.

## 5. Chống vòng lặp và scope creep

- Mỗi handoff có một owner tiếp theo.
- Sau hai lần trả lại cùng một thiếu sót, CMO phải đưa ra decision request cụ thể cho người thay vì tiếp tục vòng lặp agent.
- Chọn team nhỏ nhất đủ cho quyết định; không gọi đủ 18 specialist để tạo cảm giác toàn diện.
- Việc ngoài objective đi vào `NOT_NOW`, không tự mở rộng mission.

<!-- check-output: rules-doc -->
