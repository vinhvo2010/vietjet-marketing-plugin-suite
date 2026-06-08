---
name: route-marketing
description: Build route-specific marketing plans for domestic trunk, domestic secondary, resort, international trunk, and thin international routes. Produces audience analysis, competitive context, channel strategy, messaging, seasonal calendar, and performance targets.
---

# route-marketing

Before starting, read and apply [Operating Governance](../../references/operating-governance.md).

## Purpose
Produce a route-level marketing plan that is specific to the travel reason, competitive dynamics, and audience profile of that route — not a generic campaign template applied to a different destination. Different route types require fundamentally different approaches.

## Input Required
Provide:
- Route: origin → destination (both directions where relevant)
- Route type: domestic trunk / domestic secondary / resort / short-haul international / long-haul international / thin (low-frequency) route
- Launch type: new route / existing route optimization / seasonal push / competitive response
- Key data available (paste or link): current LF, yield, booking curve, competitive fares, seasonality
- Business objective: fill seats / improve yield / grow ancillary / defend share / launch brand awareness

Optional: target pax profile, current booking channel mix, past campaign performance on route.

## Connected Tools Needed
| Tool | Used For | Required? |
|---|---|---|
| Google Sheets | Read route performance data (LF, yield, bookings) | Recommended |
| Google Drive | Read existing route briefs or competitive intel | Optional |
| Google Docs | Output marketing plan as shareable doc | Recommended |

## Step-by-Step Workflow

**Step 1 — Route classification**
Identify route type and its marketing implications:

| Route Type | Primary driver | Marketing focus | Channel weight |
|---|---|---|---|
| Domestic trunk (HAN-SGN, SGN-DAD) | Volume + yield | Fare competitiveness + frequency + loyalty | Digital-heavy, OTA-aware |
| Domestic secondary | Stimulate demand | Destination discovery + occasion (holiday, event) | Social + CRM + PR |
| Resort (Phu Quoc, Da Nang, Nha Trang) | Leisure + family | Experience + package deal + seasonal peak | Instagram/TikTok + email + partner |
| Short-haul international (BKK, KUL, SIN) | Price + experience | Competitive fare + destination brand | OTA + paid social + email |
| North Asia / long-haul international | Brand + value | Route credibility + loyalty + market-specific value | PR + partnership + email |
| Thin (low frequency) | Load factor | Any-reason travel + FOMO on scarcity | Social + push + CRM |

For a new route, first create a route-launch fact sheet. Treat the route, first-flight date, frequency, aircraft, schedule, operating carrier, sales-open date, and entry/transit requirements as `FACT TO VERIFY` unless supported by an authorized source. Do not turn aircraft type or schedule into published copy until Operations confirms it.

**Step 2 — Audience segmentation for route**
Define 2–3 audience segments specific to this route:
- Primary: who fills this route (demographic, occasion, booking lead time, price sensitivity)
- Secondary: who we want to grow on this route
- Opportunity: underserved segment we could activate

**Step 3 — Competitive context**
For each route: who else flies it, at what price, with what service proposition?
Position VJ: where are we strongest vs. weakest on this route?
[DATA REQUIRED: DS-05 competitor fares, DS-07 MIDT market share — flag if unavailable]

Use an evidence ledger with `claim`, `source`, `source date`, and `confidence`. Do not name airlines, quote fares, estimate market size, or claim nonstop/one-stop advantages without current evidence. When evidence is absent, describe the research question and mark the answer `DATA UNAVAILABLE`.

**Step 4 — Seasonal demand calendar**
Map the route's demand pattern:
- Peak periods: what drives travel (school holidays, events, religious calendar, weather)?
- Shoulder periods: what can we do to stimulate demand?
- Off-peak: is yield protection more important than volume here?

**Step 5 — Marketing plan**
- Booking window strategy: how far in advance should we communicate?
- Channel plan: which channels for which audience at which moment?
- Messaging: route-specific headline, travel reason, seasonal angle
- Offer strategy: fare-led / bundle-led / destination-led / partner-led
- Partner opportunities: hotels, tourism boards, events, corporations on this route

**Step 6 — Performance targets and dashboard**
[DATA REQUIRED: confirmed baseline LF and yield before setting targets]
Define: LF target, yield target, APax target, booking pace index target, direct channel share target.

## Output Format

```
ROUTE MARKETING PLAN — [Route] | DRAFT | [Date]
================================================

SECTION 1: Route Profile
  - Classification, current performance [DATA: paste or link]
  - Competitive position [HYPOTHESIS if no data]
  - Launch fact sheet [for new routes]
  - Evidence ledger and missing-data list

SECTION 2: Audience Map (2–3 segments)
  - Who they are, what motivates them, booking behaviour

SECTION 3: Seasonal Calendar (12 months)
  - Peak / shoulder / off-peak periods
  - Key events and occasions by month

SECTION 4: Marketing Strategy
  - Positioning for this route
  - Channel plan by season
  - Messaging hierarchy
  - Offer/bundle recommendation

SECTION 5: Partner Opportunities
  - Tourism boards, hotels, corporates, events

SECTION 6: Performance Targets
  [TBC pending baseline data] or [filled if data provided]

SECTION 7: First 30-Day Action Plan
  - Immediate activations (no tech required)
  - Campaign launches
  - Data collection priorities

[DRAFT — HUMAN APPROVAL REQUIRED before plan is distributed or executed]
```

## Human Approval Checkpoint
> Route plans set strategic direction and marketing investment priorities. Before execution, the designated marketing and revenue approvers must both review the plan. Confirm those roles from the authority matrix.

## Example Command
```
/route-marketing

Route: SGN → Phu Quoc (VCA)
Route type: Domestic resort
Objective: Grow LF in shoulder months (Jan–Feb, Sep–Oct)
Current LF: ~82% peak (Dec, Jul–Aug), ~55% shoulder (data pasted below)
Competitive context: Vietnam Airlines and Bamboo both fly this route
Budget: Medium — social + email + partner
Key audience: Families, couples, Ho Chi Minh City residents
```

## Risks and Guardrails
- **Do not set LF or yield targets without baseline data** — write [TARGET TBC — requires confirmed baseline from DS-01/DS-02].
- **Destination marketing claims** — any claims about destination experiences, hotel partners, or tourism offerings must be verified before publishing. Flag: [VERIFY WITH TOURISM BOARD / PARTNER before using in external comms].
- **Thin routes** — do not over-invest marketing on routes that are loss-making at current pricing. Flag: [ROUTE PROFITABILITY CHECK RECOMMENDED before committing marketing budget].
- **International routes** — local language requirements, import/export regulations, and destination entry requirements may affect messaging. Flag: [LOCAL MARKET REVIEW RECOMMENDED].
- **Pride and national-identity themes** — keep them inclusive and travel-led. Avoid geopolitical, superiority, or official-endorsement implications without approval.
