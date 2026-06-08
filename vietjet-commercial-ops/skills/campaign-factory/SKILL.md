---
name: campaign-factory
description: "Generate end-to-end campaign packs from a brief: insight, target audience, offer architecture, route angle, messaging hierarchy, social/email/app push assets, approval checklist, and performance dashboard spec. Works for seasonal, route-launch, promo, and brand campaigns."
---

# campaign-factory

Before starting, read and apply [Operating Governance](../../references/operating-governance.md).

## Purpose
Turn a campaign brief into a complete, agency-quality campaign pack — insight-driven, audience-specific, channel-ready, and compliance-checked — in one skill run. Produces output that a marketing team can execute, a revenue team can approve, and a CCO can review in 10 minutes.

## Input Required
Provide a campaign brief containing:
- Campaign objective (awareness / bookings / ancillary / route launch / seasonal)
- Route(s) or product(s) being promoted
- Target travel window and booking window
- Primary audience (leisure / family / business / international / lapsed)
- Offer type: fare discount / bundle / ancillary / partner deal / content
- Budget tier (for channel priority calibration): large / medium / small / organic-only
- Brand or compliance constraints (if any)
- Yield floor (or "confirm with Revenue team")

Optional: competitor context, existing creative direction, past campaign performance.

## Connected Tools Needed
| Tool | Used For | Required? |
|---|---|---|
| Google Drive | Read existing briefs, brand guides, past campaign docs | Recommended |
| Google Docs | Output campaign pack as shareable document | Recommended |
| Google Sheets | Output performance dashboard spec and budget tracker | Optional |
| Gmail | Read stakeholder brief threads for context | Optional |

## Step-by-Step Workflow

**Step 1 — Insight foundation**
Identify the single human truth that makes this campaign worth paying attention to. Not the offer — the insight that makes the offer relevant.
Format: "People feel [X]. VJ gives them [Y]. This campaign connects those."

**Step 2 — Audience definition**
Primary segment: who, what motivates them, what barrier does this campaign overcome.
Secondary segment (if any).
Audience brief: 1 paragraph per segment (insight → offer fit → channel → message tone).

**Step 3 — Offer architecture**
- Hero offer: the main proposition (fare, bundle, destination, experience)
- Supporting offers: ancillary, partner, upsell opportunities
- Offer governance check: yield floor confirmed? Promo checklist attached?

**Step 4 — Route/destination angle**
For each route: what is the unique travel reason? (beach, city break, family visit, business corridor, event)
Route headline formula: [Emotion/benefit] + [Destination] + [Urgency or timing]

**Step 5 — Messaging hierarchy**
- Campaign headline (hero line)
- Sub-headline (offer/benefit clarity)
- Body copy direction (tone, key proof points, CTA)
- Tagline or closing line
- Vietjet brand voice check (see `/brand-voice` guardrails)

**Step 6 — Channel plan**
For each channel, produce:
- Message adaptation (same insight, right format)
- Copy direction (headline + body + CTA)
- Timing (relative to booking window open)
- Creative brief notes (visual direction, do's and don'ts)

Support every channel requested in the brief, including offline placements such as airport screens. For each channel, state its format constraints, safe-area/read-time needs, CTA behavior, and required terms treatment.

Before using a timely premise such as a heatwave, event, travel restriction, or trend as a factual claim, verify it from an authorized/current source. Otherwise frame it as a creative scenario and mark `VERIFY BEFORE PUBLISHING`.

**Step 7 — Approval checklist**
Revenue governance check + Brand compliance check + Legal/regulatory flag (if needed) + Sign-off block.

**Step 8 — Performance dashboard spec**
Define: primary KPI, secondary KPIs, measurement period, attribution method, reporting cadence.

## Output Format

```
CAMPAIGN PACK — [Campaign Name] | DRAFT | [Date]
=================================================

SECTION 1: Campaign Insight & Brief (1 page)
  - Insight
  - Audience
  - Offer summary
  - Timeline

SECTION 2: Offer Architecture
  - Hero offer + governance status
  - Supporting offers
  - Yield floor: [CONFIRMED / PENDING REVENUE TEAM SIGN-OFF]

SECTION 3: Route/Destination Angles (per route)
  - Travel reason
  - Headline options (3 variants)

SECTION 4: Messaging Hierarchy
  - Campaign headline
  - Sub-headline
  - Body copy direction
  - CTA

SECTION 5: Channel Execution Pack
  [Per requested channel: format constraints + copy direction + timing + creative brief + terms treatment]

SECTION 6: Approval Checklist
  [ ] Revenue governance: yield floor confirmed
  [ ] Brand voice check passed
  [ ] Legal review (international routes / prize/giveaway)
  [ ] Designated revenue approver sign-off [POLICY TO CONFIRM]
  [ ] Final commercial approver sign-off [POLICY TO CONFIRM]

SECTION 7: Performance Dashboard Spec
  - Primary KPI + formula
  - Secondary KPIs
  - Attribution window
  - Report owner + cadence

[DRAFT — HUMAN APPROVAL REQUIRED before any assets go to production or any campaign goes live]
```

## Human Approval Checkpoint
> **Two gates required:**
> 1. **Revenue gate:** the designated revenue approver confirms yield floor is maintained and the promo governance checklist is complete before creative goes to production.
> 2. **Brand/commercial gate:** the designated final approver confirms campaign direction and messaging before external publishing.
> Codex produces drafts only. Confirm the actual approvers from the authority matrix; neither gate can be bypassed.

## Example Command
```
/campaign-factory

Objective: Drive bookings on SGN-BKK for the August school holiday period.
Audience: Families with children, based in Ho Chi Minh City. Past VJ flyers.
Offer: SMART bundle (20kg bag + seat) at 15% discount. Travel 1-31 Aug.
Booking window: Opens June 1, closes July 15.
Budget: Medium (paid social + email + app push).
Yield floor: To be confirmed with Revenue team.
Constraint: No competitor comparison allowed in copy.
```

## Risks and Guardrails
- **Yield floor is not optional** — output will include a warning if yield floor is not confirmed: [REVENUE GOVERNANCE INCOMPLETE — do not launch until yield floor is approved].
- **No competitor naming** — do not reference competitor names or fares in any copy unless user explicitly instructs and legal review is confirmed.
- **Prize promotions** — if campaign includes a prize, competition, or giveaway, flag: [LEGAL REVIEW REQUIRED — prize promotions require regulatory compliance in Vietnam and destination countries].
- **Sensitive destinations** — for routes involving geopolitical sensitivity, flag for PR/Legal review.
- **Creative assets are direction, not final copy** — all copy must be reviewed by Brand/Marketing team before production. Output is a brief, not a finished asset.
