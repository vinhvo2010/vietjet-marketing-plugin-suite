---
name: crm-personalization
description: Create customer lifecycle segments, behavioral trigger journeys, personalized offer logic, email/app push copy, and measurement plans. Produces ready-to-brief CRM architecture and campaign sequences for airline customer lifecycle growth.
---

# crm-personalization

Before starting, read and apply [Operating Governance](../../references/operating-governance.md).

## Purpose
Design and produce the CRM systems that grow revenue by treating each customer as an individual — right offer, right channel, right moment. Outputs include: segment definitions, trigger journey maps, copy variants, suppression logic, and measurement framework. Everything is drafted for human review before any send.

## Input Required
Provide ONE or MORE of:
- CRM audit data: current segments, active triggers, platform (paste or summarise)
- A specific journey to design: "Design the pre-departure upsell sequence for domestic routes"
- A segment to activate: "Design win-back for customers who haven't flown in 6 months"
- Campaign performance data to analyse: "This email had 8% open rate — why and what to change?"
- The goal: revenue per customer, attach rate improvement, churn reduction, win-back

**Data privacy note:** Do not paste individual customer records, PNR data, or personal information. Use aggregate data only (segment sizes, rates, averages).

## Connected Tools Needed
| Tool | Used For | Required? |
|---|---|---|
| Google Sheets | Customer segment sizes, performance rates, APax by segment | Recommended |
| Google Drive | CRM audit docs, journey maps, brand voice guides | Optional |
| Google Docs | Output journey maps and copy as shareable briefs | Recommended |

**Data Privacy Requirement:** CRM connector (if used) must be scoped to aggregate/anonymised data only. PII access requires DPO sign-off. Flag before proceeding: [CONFIRM: does this session involve individual customer PII? If yes, DPO approval required.]

## Step-by-Step Workflow

**Step 1 — Segment definition**
For each segment requested:
- Name and label
- Definition (RFM criteria or behavioural criteria — specific, not vague)
- Size estimate [DATA REQUIRED: DS-09 or CRM platform — flag if unavailable]
- Primary revenue lever (what action generates revenue from this segment)
- Channel preference (email / app push / Zalo OA / SMS)
- Suppression rules (who to exclude even if they match the segment criteria)

**Step 2 — Journey architecture**
For each journey:
- Entry trigger (exact event or time-based rule)
- Journey steps (step number, trigger, channel, message objective, timing)
- Exit conditions (when does a customer leave this journey?)
- Suppression rules (what conditions stop a step from firing?)
- Frequency cap (maximum contacts per customer per 30 days)
- Include owned-product surfaces when requested: web/app booking flow, manage-booking, check-in, or post-booking. Specify placement, trigger, eligibility, and fallback behavior.

**Step 3 — Offer logic**
For each step: what product, at what price point, with what incentive (if any)?
- If offer involves a discount: flag for Revenue governance check
- If offer is a product recommendation: base on segment's historical attach rate [DATA REQUIRED]
- Maximum 3 offers per journey step — do not overwhelm
- For fare-family or upgrade upsells, show only verified benefit differences and the true incremental price. Do not use preselected upgrades, hidden opt-outs, false scarcity, or other dark patterns.

**Step 4 — Copy production**
For each step: produce 2 copy variants (A/B test ready):
- Subject line / push title (max 50 characters)
- Preview text (max 90 characters)
- Body copy direction (2–3 sentences, benefit-led, CTA)
- CTA text (max 4 words)
- Vietjet brand voice applied (see `/brand-voice`)

**Step 5 — Measurement plan**
- Primary metric: one metric per journey (open rate / CTR / conversion / revenue)
- Holdout group: 10–15% of segment excluded from journey (true control)
- Attribution window: how many days after last touch counts as attributed?
- Incremental revenue formula: (test revenue per eligible customer − holdout revenue per eligible customer) × eligible test population
- Report gross exposed revenue separately from incremental revenue. Never label exposed-group revenue, attributed revenue, or revenue uplift without a control as incremental.
- Confirm randomized assignment or document selection bias; use comparable eligibility rules and measurement windows; report group sizes and uncertainty before claiming lift.
- Report frequency: weekly during active journey, monthly ongoing

## Output Format

```
CRM PERSONALIZATION BRIEF — [Journey Name] | DRAFT | [Date]
=============================================================

SECTION 1: Segment Definition
  [Name, criteria, size, lever, channel, suppression]

SECTION 2: Journey Map
  Step | Trigger | Channel | Message Objective | Timing | Suppression
  [Table — one row per step]

SECTION 3: Offer Logic
  [Step → product → price/offer → governance status]

SECTION 4: Copy Variants (A/B)
  Step X:
    Variant A: Subject / Body / CTA
    Variant B: Subject / Body / CTA

SECTION 5: Measurement Plan
  Primary metric: ___
  Holdout: ___% of segment
  Attribution window: ___ days
  Incremental revenue formula: ___
  Gross vs incremental revenue: ___
  Assignment method, group sizes, and uncertainty: ___
  Report owner + cadence: ___

[DRAFT — HUMAN APPROVAL REQUIRED. No journey may be activated without:
1. Designated journey owner sign-off on journey design [POLICY TO CONFIRM]
2. Designated revenue approver sign-off on any step involving a fare discount [POLICY TO CONFIRM]
3. Designated privacy approver confirmation that data use complies with privacy policy [POLICY TO CONFIRM]]
```

## Human Approval Checkpoint
> **Three gates for CRM journeys:**
> 1. **Design gate:** The designated journey owner confirms journey architecture is correct and frequency caps are respected.
> 2. **Revenue gate:** Any step with a discount or promotional fare requires the designated revenue approver's sign-off and a yield-floor check.
> 3. **Privacy gate:** If the journey uses behavioural data, the designated privacy approver must confirm compliance with applicable privacy rules and Vietjet policy.
> All three gates must be cleared before a journey is activated in the CRM platform.

## Example Command
```
/crm-personalization

Journey: Pre-departure baggage upsell
Trigger: Booking confirmed, no checked bag purchased, departure in 7 days
Segment: All pax without checked bag, domestic routes only
Channels: Email (D-7) + App push (D-5) + Email (D-3 if no purchase)
Goal: Increase baggage attach rate on domestic routes
Current attach rate: ~42% [HYPOTHESIS — validate with DS-03]
Target: +8 percentage points
Offer: 20kg bag at standard rate — no discount, urgency framing only
```

## Risks and Guardrails
- **Never paste or accept individual customer PII** — if user pastes a list of customer records, stop and request aggregate data only.
- **Frequency caps are mandatory** — output will always include a maximum contacts/month recommendation. Never design a journey without one.
- **Discount steps require Revenue governance** — if any step includes a fare or ancillary discount, the Revenue governance checklist must be run before activation.
- **Suppression is not optional** — every journey must have suppression rules for: opted-out customers, customers with disrupted flights, customers in active complaint/refund process.
- **Upsell UX must be transparent** — show the incremental price and verified benefits, provide an equally clear decline path, and do not preselect paid upgrades.
- **Zalo OA / SMS** — in Vietnam, commercial messaging via Zalo and SMS is regulated. Flag: [REGULATORY REVIEW RECOMMENDED for Zalo OA and SMS commercial sends].
