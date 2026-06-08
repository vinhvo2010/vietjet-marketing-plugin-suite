# Vietjet Commercial Ops Acceptance Test Report

**Test date:** 2026-06-08  
**Plugin:** `vietjet-commercial-ops`  
**Method:** Eight forward simulations using only supplied case facts. No external or connected data was accessed.

## Executive Result

| Test | Primary Skill | Result After Refinement |
|---|---|---|
| 1. Route Launch Brief | `route-marketing` | PASS |
| 2. Promo QA | `promo-qa` | PASS |
| 3. Campaign Plan | `campaign-factory` | PASS |
| 4. Ancillary Upsell | `crm-personalization` | PASS |
| 5. CRM Incremental Revenue | `crm-personalization` | PASS |
| 6. Competitive / Route Intelligence | `route-marketing` | PASS |
| 7. Executive Brief | `executive-reporter` | PASS |
| 8. Asset / Copy Governance | `brand-voice` + `promo-qa` | PASS |

The initial plugin passed core routing and governance behavior. Acceptance testing identified six refinement areas: route-launch fact sheets, zero-fare disclosure and channel parity, arbitrary requested channels, transparent upsell UX, controlled-experiment validity, and evidence-led competitive intelligence. These were fixed before the final pass.

## Test 1: Route Launch Brief

**Case:** HAN ⇄ PRG; first flight October 10, 2026; A330; awareness + booking intent + Vietnam-Europe pride.

**Triggered skill:** `route-marketing`

**Expected output structure:**

1. Route profile and launch fact sheet
2. Audience map
3. Competitive evidence ledger
4. Seasonal calendar
5. Positioning, channel, and messaging strategy
6. Performance targets marked TBC where baselines are missing
7. First 30-day action plan

**Short simulated output:**

```text
ROUTE MARKETING PLAN — HAN ⇄ PRG | DRAFT

CONFIRMED FROM BRIEF:
- Route: HAN ⇄ PRG
- First flight: October 10, 2026
- Aircraft: A330

FACTS TO VERIFY BEFORE PUBLISHING:
- Operating frequency, schedule, sales-open date, operating carrier, and A330 configuration

POSITIONING DIRECTION:
"A new bridge between Vietnam and Europe" combines booking intent with inclusive national pride.
Avoid unsupported claims such as "the only nonstop route" or "Europe's best-value flight."

TARGETS: [DATA UNAVAILABLE — require booking curve, capacity, yield floor, and awareness baseline]
```

**Hallucination / data-boundary risks:**

- Inventing frequency, schedule, aircraft configuration, nonstop status, fares, demand, or competitor facts.
- Turning “Vietnam-Europe pride” into an official endorsement or superiority claim.

**Verdict:** Needed refinement, then PASS. Added route-launch fact sheet, Operations confirmation, evidence ledger, and pride-theme guardrails.

## Test 2: Promo QA

**Case:** SALE66; 12 million promotional tickets; fares from 0Đ; booking period June 1-7, 2026; all routes.

**Triggered skill:** `promo-qa`

**Expected output structure:**

1. Six-dimension QA review
2. Channel-parity matrix
3. Risk score
4. Mandatory fix list
5. Human approval gate

**Short simulated output:**

```text
PROMO QA REVIEW — SALE66 | DRAFT
RISK SCORE: RED

TIMING:
- Booking period ended June 7, 2026. As of June 8, 2026, do not publish active-booking CTAs.

FARE RULE CLARITY — BLOCK
- "From 0Đ" does not state taxes, fees, fare class, seat quota, travel dates, or exclusions.
- "All routes" and "12 million tickets" are unverified universal/inventory claims.

CHANNEL EXECUTION — BLOCK
- Require one approved terms version and parity across every ad, push, OTA placement, and landing page.

RECOMMENDATION: NO-GO until claims, inventory, terms, dates, and channel parity are verified.
```

**Hallucination / data-boundary risks:**

- Assuming 12 million seats exist or all routes participate.
- Treating 0Đ as the total payable price.
- Missing that the booking window is already over.

**Verdict:** Needed refinement, then PASS. Added zero-fare disclosure checks, inventory validation, automatic RED rules, and a channel-parity matrix.

## Test 3: Campaign Plan

**Case:** Australia winter campaign; angle: Hanoi heatwave → Australian winter flex; TikTok, Facebook, app push, airport screen.

**Triggered skill:** `campaign-factory`

**Expected output structure:**

1. Insight and audience brief
2. Offer architecture
3. Destination angles
4. Messaging hierarchy
5. Execution pack for all four requested channels
6. Approval checklist
7. Performance dashboard specification

**Short simulated output:**

```text
CAMPAIGN INSIGHT:
When Hanoi feels hottest, an Australian winter becomes a refreshing travel flex.

VERIFY BEFORE PUBLISHING:
- Do not state that Hanoi is in a heatwave without a current authorized source.

CHANNEL ADAPTATIONS:
- TikTok: fast temperature-contrast reveal; travel-first CTA.
- Facebook: destination carousel with booking proposition.
- App push: "Đổi nắng nóng lấy mùa đông Úc" [offer/date required].
- Airport screen: 6-second visual, minimal copy, no QR without readability test.
```

**Hallucination / data-boundary risks:**

- Claiming a current Hanoi heatwave without verification.
- Inventing Australian weather, prices, travel dates, or entry requirements.
- Omitting airport-screen constraints because it was not in the original channel list.

**Verdict:** Needed refinement, then PASS. Added support for every requested channel, offline-format constraints, and timely-claim verification.

## Test 4: Ancillary Upsell

**Case:** Deluxe fare upsell for economy passengers; email, app push, web booking flow; increase upgrade conversion.

**Triggered skill:** `crm-personalization`

**Expected output structure:**

1. Eligible segment and suppressions
2. Cross-channel journey map
3. Verified Deluxe benefit and price logic
4. Copy variants
5. Experiment and measurement plan

**Short simulated output:**

```text
SEGMENT:
Economy shoppers/bookers eligible for Deluxe [eligibility rules DATA REQUIRED].

WEB BOOKING FLOW:
- Show verified Deluxe benefits and true incremental price.
- Provide equally clear "Continue with Economy" action.
- Do not preselect Deluxe or use false scarcity.

SUPPRESS:
- Already-Deluxe passengers, disrupted itineraries, refund/complaint cases, opted-out CRM users.

PRIMARY METRIC:
Incremental upgrade conversion versus randomized holdout.
```

**Hallucination / data-boundary risks:**

- Inventing Deluxe benefits or upgrade prices.
- Using customer-level PII.
- Dark patterns that inflate conversion but create complaints.

**Verdict:** Needed refinement, then PASS. Added booking-flow surfaces, transparent incremental pricing, verified benefits, and no-dark-pattern rules.

## Test 5: CRM Incremental Revenue

**Case:** Compare campaign holdout versus exposed users without confusing gross and incremental revenue.

**Triggered skill:** `crm-personalization`

**Expected output structure:**

1. Experiment definition and assignment method
2. Eligible population and group sizes
3. Gross revenue by group
4. Per-eligible-customer revenue
5. Incremental revenue calculation
6. Bias and uncertainty notes

**Short simulated output using illustrative values only:**

```text
[ILLUSTRATIVE — NOT VIETJET DATA]
Exposed: 90,000 eligible users; gross revenue VND 13.5B; VND 150k/user
Holdout: 10,000 eligible users; gross revenue VND 1.4B; VND 140k/user

Incremental revenue per exposed user = VND 150k - VND 140k = VND 10k
Estimated incremental revenue = VND 10k × 90,000 = VND 900M

Do not report VND 13.5B exposed gross revenue as incremental revenue.
Claim requires randomized/comparable groups, aligned windows, and uncertainty review.
```

**Hallucination / data-boundary risks:**

- Calling exposed gross or attributed revenue “incremental.”
- Comparing unequal groups by total revenue rather than revenue per eligible customer.
- Ignoring selection bias, group size, or measurement-window differences.

**Verdict:** Core formula passed; experiment-validity detail needed refinement, then PASS.

## Test 6: Competitive / Route Intelligence

**Case:** Vietnam ⇄ Europe travel demand; route positioning, audience opportunity, competitor messaging risks; no invented market data.

**Triggered skill:** `route-marketing`

**Expected output structure:**

1. Scope and route classification
2. Evidence ledger
3. Missing-data list
4. Audience hypotheses
5. Positioning options
6. Competitor messaging risk review
7. Research plan

**Short simulated output:**

```text
DATA UNAVAILABLE:
- Vietnam-Europe O&D demand, market share, fares, booking lead time, and competitor capacity.

AUDIENCE HYPOTHESES TO VALIDATE:
- Leisure travelers, VFR travelers, students, and business travelers.

POSITIONING OPTION:
- Lead with direct travel value and Vietnam-Europe connection only after schedule and competitive evidence are verified.

COMPETITOR MESSAGING RISKS:
- Do not claim "cheapest," "fastest," "only nonstop," or superior network coverage without dated evidence.
```

**Hallucination / data-boundary risks:**

- Naming competitors, market shares, fares, or audience sizes without sources.
- Presenting plausible audience ideas as facts.

**Verdict:** Needed refinement, then PASS. Added evidence ledger, source dates/confidence, and explicit `DATA UNAVAILABLE` behavior.

## Test 7: Executive Brief

**Case:** One-page leadership brief for the HAN ⇄ PRG campaign decision.

**Triggered skill:** `executive-reporter`

**Expected output structure:**

1. Decision requested
2. Situation and confirmed facts
3. Options and trade-offs
4. Risks and missing evidence
5. Decisions and next steps

**Short simulated output:**

```text
HAN ⇄ PRG CAMPAIGN DECISION | DRAFT

DECISION REQUESTED:
Approve campaign development with conditions, or defer pending launch evidence.

CONFIRMED:
- Brief states first flight October 10, 2026, using A330.

RECOMMENDATION:
Approve with conditions: verify schedule/aircraft facts, confirm commercial targets and budget,
complete local-market/legal review, and approve the authority matrix.

COMMERCIAL CASE:
[DATA UNAVAILABLE — no budget, capacity, booking curve, yield floor, or forecast supplied]
```

**Hallucination / data-boundary risks:**

- Inventing budget, revenue, demand, forecast, or campaign ROI.
- Treating the supplied route facts as operationally verified.

**Verdict:** Needed minor refinement, then PASS. Added decision options, trade-offs, assumptions, and gating evidence.

## Test 8: Asset / Copy Governance

**Case:** “Bay châu Âu miễn phí cùng Vietjet, vé 0Đ cho mọi người, đặt ngay hôm nay!”

**Triggered skills:** `brand-voice` for diagnosis/rewrite, then `promo-qa` for promotional approval gate.

**Expected output structure:**

1. Original-copy diagnosis
2. Legal/commercial/brand flags
3. Safer rewrite variants
4. Facts and terms to verify
5. Promo QA routing and approval gate

**Short simulated output:**

```text
RISK: RED

FLAGS:
- "miễn phí" may be misleading if taxes, fees, or ancillaries remain payable.
- "vé 0Đ cho mọi người" is an unsupported universal claim.
- "đặt ngay hôm nay" is invalid unless booking is currently open.

SAFER DRAFT:
"Chạm tới châu Âu cùng Vietjet, săn vé từ 0Đ*."

REQUIRED NEARBY TERMS:
*Taxes, fees, eligible routes/dates, seat quota, booking period, and fare conditions to be verified.

Route through promo-qa before publishing.
```

**Hallucination / data-boundary risks:**

- Preserving a misleading “free” claim.
- Inventing availability, eligibility, or terms.
- Treating rewritten copy as approved legal language.

**Verdict:** Needed refinement, then PASS. Added explicit free/universal-language controls and mandatory `promo-qa` routing.

## Fixes Applied

- `route-marketing`: route-launch fact sheets, evidence ledger, no unsupported competitive claims, inclusive pride-theme rule.
- `promo-qa`: zero-fare disclosures, inventory verification, universal-claim RED rule, channel-parity matrix.
- `campaign-factory`: arbitrary requested channels, offline constraints, timely premise verification.
- `crm-personalization`: booking-flow surfaces, transparent upsells, gross-versus-incremental reporting, experiment-validity requirements.
- `executive-reporter`: decision options, trade-offs, and gating evidence.
- `brand-voice`: explicit free/universal promotional-language checks and `promo-qa` handoff.

## Final Acceptance Decision

**PASS WITH GOVERNANCE CONDITIONS**

The plugin is ready for controlled pilot use with pasted or authorized data. Before operational rollout, Vietjet should provide the approved authority matrix, data-source ownership, legal terms templates, fare-family benefit definitions, and connector access scopes.
