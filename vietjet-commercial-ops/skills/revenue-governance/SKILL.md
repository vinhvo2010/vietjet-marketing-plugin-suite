---
name: revenue-governance
description: Create promotional campaign governance, fare/ancillary approval matrix, compliance checklists, risk reviews, and audit controls for airline commercial decisions. Use before any promotion is launched or any significant fare change is made.
---

# revenue-governance

Before starting, read and apply [Operating Governance](../../references/operating-governance.md).

## Purpose
Design and apply the control framework that ensures every commercial decision — fare change, promotional campaign, ancillary repricing, bundle restructure — is made by the right person, with the right data, at the right level of authority, with a full audit trail. Produces governance documents ready for sign-off.

## Input Required
Provide ONE or MORE of:
- A promotional campaign brief (paste or link)
- A fare change proposal
- A governance gap to close ("we need an approval matrix for ancillary pricing")
- An existing checklist or policy to review and improve
- Route/product context: which routes, which BU, what magnitude of change

## Connected Tools Needed
| Tool | Used For | Required? |
|---|---|---|
| Google Drive | Read existing policy docs, governance templates | Optional |
| Google Docs | Output governance documents as shareable drafts | Optional |
| Google Sheets | Output approval matrix tables | Optional |

## Step-by-Step Workflow

**Step 1 — Identify the governance need**
Determine: Is this a new governance document, a checklist for a specific campaign, or an audit of an existing process?

**Step 2 — Define authority levels**
If an approved authority matrix is supplied, map decision types to it. Otherwise present the following only as a proposed structure marked `POLICY TO CONFIRM`:
- RM Analyst → Head of RM → VP Revenue → CCO → CFO
- Ancillary: Head of Ancillary → VP Revenue → CCO
- Campaigns: Campaign Manager → Head of Digital → VP Revenue → CCO

**Step 3 — Build the appropriate document**
Choose based on input:
- Authority Matrix: fare magnitude × lead time × approver
- Promo Governance Checklist: yield floor, demand rationale, ancillary target, channel, cannibalisation, sign-off
- Fare Change Memo (FCM): structured template for individual fare decisions
- Risk Review: top risks, likelihood, impact, mitigation, owner
- Audit Log Schema: what to record, where, who reviews

**Step 4 — Apply to specific input**
If a campaign brief is provided: run the checklist against it and produce a go/no-go recommendation with a risk score (Green/Amber/Red).

**Step 5 — Produce the governance output**
Include: approval signature block, version number, effective date, review date.

## Output Format

```
GOVERNANCE OUTPUT — [Document Type]
=====================================
Prepared by: [AI draft]  |  Date: [date]  |  Version: DRAFT 1.0
Review date: [6 months from date]

[CONTENT — matrix / checklist / memo / risk review / audit schema]

RISK SCORE (for campaign reviews): Green / Amber / Red
RECOMMENDATION: [Go / No-Go / Go with conditions]
CONDITIONS (if any): [list]

APPROVAL REQUIRED:
[ ] Head of [function]: _______________ Date: ___
[ ] Designated revenue approver [POLICY TO CONFIRM]: _______________ Date: ___
[ ] Additional approver required by confirmed authority matrix: _______________ Date: ___

[DRAFT — HUMAN APPROVAL REQUIRED before this governance document is used operationally]
```

## Human Approval Checkpoint
> Every governance document must be reviewed and signed by the designated authority before it is used to approve or reject a commercial decision. A draft checklist is not an approved checklist. If no approved authority matrix is supplied, mark the approver `POLICY TO CONFIRM`.

## Example Command
```
/revenue-governance

Task: Review this promo brief and tell me if it passes governance.

Brief: Flash sale on HAN-SGN. 50% discount. Booking window: 3 days.
Travel window: 2 weeks from now. No minimum stay. All channels including OTA.
Expected volume: 5,000 bookings.
```

## Risks and Guardrails
- **Never issue a Go recommendation** on a campaign without a yield floor confirmation. If CASK data is not provided, output: [YIELD FLOOR UNCONFIRMED — cannot approve without Finance input].
- **Never approve a campaign** — you draft the recommendation; a human approves it.
- **Do not assume current policy** — if user says "our current authority matrix says X," ask them to paste it or confirm; do not invent policy details.
- **Cannibalisation is always a risk** — flag it in every promo review, even if the user does not mention it.
- **Regulatory note** — for international routes, flag that any promotional fare must comply with the tariff filing requirements of each country. [LEGAL REVIEW RECOMMENDED for international promos.]
