# VJ-GMOM implementation roadmap

## Definition of done by maturity

| Level | Evidence required | Current v5 package |
|---|---|---|
| 1 Governed copilots | rules, evidence labels, human gates, role boundaries | Implemented and locally validated |
| 2 Coordinated team | mission schema, router, dependencies, handoffs, independent review | Implemented and locally validated |
| 3 Closed-loop team | approved aggregate data, experiment execution, release events, learning loop | Not connected; pilot required |
| 4 Policy-bound autonomy | platform-enforced permissions, approval tokens, observability, rollback | Not connected; production program required |

## 0–30 days

| Deliverable | Accountable human | Exit test |
|---|---|---|
| Group Growth Council charter | Group CMO / Commercial | Decision rights signed |
| Market-scope registry | Commercial + Legal | Entity/POS/source/corridor separated |
| Source and metric registry | Data + Marketing Science | Owners, refresh SLA, lineage present |
| Approval matrix | Legal + Finance + Ops + CMO | Named primary and backup approvers |
| Two pilot mission briefs | Mission owners | Schemas valid and no invented baseline |

## 31–60 days

| Deliverable | Accountable human | Exit test |
|---|---|---|
| Route-corridor pilot | Commercial owner | Router/handovers completed, claims reviewed |
| Lifecycle pilot | CRM/CX owner | Consent/preference/experience gates passed |
| Incrementality test | Marketing Science | Control, primary metric, guardrails pre-registered |
| Kill-switch rehearsal | PR + MarTech | Human can pause scoped activity within approved SLA |

## 61–90 days

| Deliverable | Accountable human | Exit test |
|---|---|---|
| Aggregate data connection | Data owner | Read-only, allow-list, no PII, audit log |
| Release event integration | MarTech owner | Approval identity and rollback evidence stored |
| Learning loop | Group CMO | Result changes a subsequent decision record |
| Scale decision | Group Growth Council | Go/revise/stop with evidence and owner |

## Anti-goals

- Không tự động chi tiền hoặc phát hành để chứng minh “agentic”.
- Không mua thêm connector trước khi có mission và owner cụ thể.
- Không dùng một dashboard thay cho causal measurement.
- Không nhân bản market pod theo quốc gia nếu chưa tách pháp nhân, POS, source market và corridor.
- Không tuyên bố Harvard/YC certification; các nguồn chỉ là cơ sở thiết kế.

