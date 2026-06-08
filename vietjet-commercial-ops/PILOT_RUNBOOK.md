# Vietjet Commercial Ops Controlled Internal Pilot Runbook

**Plugin:** `vietjet-commercial-ops`  
**Current release:** `v0.1.0`  
**Pilot model:** Governed internal drafting and review only

## 1. Purpose

`vietjet-commercial-ops` supports governed commercial, route, promotional, CRM, revenue, PMO, and executive-reporting workflows. It helps internal teams turn approved inputs and incomplete briefs into structured drafts, evidence requests, risk reviews, measurement plans, and human decision gates.

The plugin recommends and drafts. It does not authorize, publish, activate, or execute.

## 2. Who Can Use It

- Commercial strategy
- Marketing
- CRM
- Revenue / PMO
- Executive reporting support

Users must work within their authorized data access and the applicable human review process.

## 3. What It Can Be Used For

- Route launch brief
- Promo QA
- Campaign planning
- CRM personalization
- Revenue governance
- Executive brief
- Post-campaign recap

## 4. What It Must Not Be Used For

- Final legal approval
- Final fare filing approval
- Inventory decisioning
- Revenue-management automation
- Publishing, sending, posting, or activating without human approval
- Making market, revenue, inventory, route-performance, or competitive claims without evidence
- Assigning or inventing approval owners, thresholds, policies, or signatories

## 5. Required Intake Before Every Run

Before selecting or running a skill:

1. Complete [Evidence and Approval Intake](references/evidence-and-approval-intake.md).
2. Assign an output ID using [Output ID Convention](references/output-id-convention.md), or use `PENDING-ID` until the audit-log owner assigns one.
3. Record the request owner, objective, intended usage channel, time sensitivity, risk level, source facts, assumptions, missing data, evidence references, and approval status.
4. Confirm that all supplied or connected data is authorized for the requested use.

If a required input is unavailable, record `DATA UNAVAILABLE` or `POLICY TO CONFIRM`; do not infer it.

## 6. Required Governance After Every Run

After producing a draft:

1. Apply [Operating Governance](references/operating-governance.md).
2. Create or update the output record using [Audit Log Schema](references/audit-log-schema.md).
3. Record governance flags, missing evidence, approval status, human owner, output file/link, version, and change reason.
4. Preserve the output ID across revisions.
5. Record only evidence-backed human approvals and final decisions.

Every substantive output must end with:

```text
STATUS: DRAFT - HUMAN APPROVAL REQUIRED
FACTS TO VERIFY:
- ...
POLICY / APPROVALS TO CONFIRM:
- ...
NEXT HUMAN DECISION:
- ...
```

## 7. Measurement Workflows

- Use [Post-Campaign Measurement Worksheet](references/post-campaign-measurement-worksheet.md) for post-campaign reporting and recap work.
- Use [CRM Measurement Worksheet](references/crm-measurement-worksheet.md) for CRM journeys and ancillary-upsell measurement.
- Always report gross and incremental outcomes separately.
- If there is no valid control or comparable baseline, mark incrementality `NOT MEASURABLE`.
- State confounders, confidence level, what can be claimed, and what cannot be claimed.

## 8. Standard Operating Flow

```text
Intake
  → Skill selection
  → Draft output
  → Governance check
  → Human review
  → Measurement / audit log
  → Final handoff
```

### Flow Gates

| Stage | Required result before continuing |
|---|---|
| Intake | Output ID assigned or pending; facts, assumptions, missing data, risk, and intended use recorded |
| Skill selection | Correct skill selected for the requested workflow |
| Draft output | Output clearly marked draft and limited to supplied or verified evidence |
| Governance check | Data boundaries, claims, approvals, and missing evidence reviewed |
| Human review | Designated human owner reviews the draft and records a decision |
| Measurement / audit log | Required worksheet completed and audit record updated |
| Final handoff | Approved output and conditions handed to the authorized human execution owner |

## 9. Pilot Use Cases

### HAN ⇄ PRG Route Launch

- Primary skill: `route-marketing`
- Expected output: route-launch fact sheet, audience hypotheses, evidence ledger, positioning direction, missing-data list, and first actions
- Required controls: do not invent schedule, frequency, aircraft configuration, demand, competitor data, route performance, targets, or approval workflow

### SALE66 Post-Campaign Recap

- Primary skill: `executive-reporter`
- Supporting skill: `promo-qa`
- Expected output: post-campaign recap, retrospective control review, required data pack, claim boundaries, and leadership decisions
- Required controls: do not infer campaign success; separate gross from incremental outcomes; validate `0Đ`, universal, inventory, and cross-channel claims

### Deluxe Upsell CRM Sequence

- Primary skill: `crm-personalization`
- Supporting skills: `brand-voice`; `revenue-governance` if a discount is proposed
- Expected output: eligible segment, journey map, suppressions, transparent copy framework, and controlled measurement plan
- Required controls: do not invent benefits, prices, eligibility, conversion, or revenue; use no dark patterns; require aggregate authorized data

See [PILOT_RUN_REPORT.md](PILOT_RUN_REPORT.md) for the completed governed simulations.

## 10. Human Approval Gates

- The plugin may recommend which approval domains are needed, such as Revenue, Legal, Privacy, Brand, Operations, or Commercial.
- The plugin must not invent or assign approvers, approval thresholds, policies, or signatories unless they are supplied from an approved authority matrix.
- Unknown approval owners or thresholds must be marked `POLICY TO CONFIRM`.
- A plugin recommendation, including `GO`, means ready to enter the human approval process. It never authorizes execution.
- External use requires recorded human review and approval.

## 11. Data-Boundary Rules

- Do not invent market data.
- Do not invent revenue data.
- Do not invent inventory data.
- Do not invent route performance.
- Do not invent approval thresholds.
- Clearly separate facts, assumptions, and missing data.
- Do not expose customer-level PII, PNR data, credentials, payroll data, or unrelated business-unit data.
- Use authorized aggregate or anonymized CRM data only.
- Never claim a connector or source was accessed unless the access succeeded.

Use these labels consistently:

| Label | Meaning |
|---|---|
| `FACT` | Supported by authorized evidence |
| `BRIEF FACT` | Supplied in the request but still requires owner verification before external use |
| `ESTIMATE` | Calculated or supplied estimate with method/source stated |
| `HYPOTHESIS` | Unverified idea requiring validation |
| `DATA UNAVAILABLE` | Required evidence was not supplied or accessed |
| `POLICY TO CONFIRM` | Approval owner, threshold, or policy was not supplied |

## 12. Output ID Examples

```text
VJ-COMOPS-PROMOQA-20260608-001
VJ-COMOPS-ROUTEMKT-20260608-001
VJ-COMOPS-CRM-20260608-001
```

Use the primary skill code for multi-skill outputs and record supporting skills in the audit log.

## 13. Pilot Success Criteria

- [ ] 100% of outputs include facts, assumptions, and missing-data separation
- [ ] 100% of outputs include governance flags
- [ ] 100% of outputs include an output ID
- [ ] No invented unsupported data
- [ ] Human review is required before external use

Any failure against these criteria must be logged, reviewed, and corrected before continuing the pilot.
