# Test Prompts

Use these prompts for internal smoke tests. Unless the prompt explicitly supplies verified data, the skill should mark missing facts and must not invent them.

## `brand-voice`

```text
Rewrite this consumer promo copy into safe Vietjet brand voice:
"Bay châu Âu miễn phí cùng Vietjet, vé 0Đ cho mọi người, đặt ngay hôm nay!"

Channel: Facebook
Audience: Vietnam leisure travelers
Constraints: Do not invent booking dates, eligibility, routes, inventory, taxes, or fees.
Flag commercial and legal risks, provide two safer variants, and route the result through promo-qa.
```

## `campaign-factory`

```text
Create a campaign pack for an Australia winter campaign.
Creative angle: Hanoi heatwave to Australian winter flex.
Channels: TikTok, Facebook, app push, and airport screen.
Objective: awareness and booking intent.
Offer, booking dates, budget, and yield floor are not supplied.

Treat the heatwave as a creative scenario unless verified. Include every requested channel,
format constraints, approval gates, and a performance dashboard specification.
```

## `crm-personalization`

```text
Design a transparent Deluxe fare upsell journey for eligible Economy passengers.
Channels: email, app push, and web booking flow.
Goal: increase upgrade conversion.

Do not invent Deluxe benefits or prices. Require verified benefit differences and true
incremental price. Include suppressions, an equally clear decline path, randomized holdout,
and separate gross revenue from incremental revenue.
```

## `executive-reporter`

```text
Prepare a one-page leadership decision brief for a HAN ⇄ PRG launch campaign.
Supplied brief facts: first flight October 10, 2026; aircraft A330.
No budget, forecast, capacity, yield floor, schedule confirmation, or market-demand data supplied.

Include confirmed facts versus assumptions, approve / approve-with-conditions / defer options,
trade-offs, gating evidence, decisions required, and next steps.
```

## `promo-qa`

```text
Review SALE66 for launch readiness:
- 12 million promotional tickets
- Fares from 0Đ
- Booking period: June 1-7, 2026
- Applies to all routes
- Channels: web, app, social, CRM, OTA
- Yield floor and travel dates not supplied

Check fare-condition clarity, inventory evidence, universal claims, taxes/fees disclosures,
current booking-window validity, and cross-channel parity. Produce a risk score and fix list.
```

## `revenue-governance`

```text
Draft a governance review for a proposed 0Đ all-route promotion.
The current authority matrix, yield floor, inventory evidence, and legal terms are not supplied.

Do not invent approvers or thresholds. Mark policy gaps, required evidence, approval gates,
audit-log fields, and whether the proposal may enter the human approval process.
```

## `revenue-pmo`

```text
Turn the HAN ⇄ PRG route-launch marketing initiative into a 12-week execution backlog.
Goal: prepare campaign strategy, channel assets, local-market review, launch governance,
measurement plan, and leadership decision gates before the first flight on October 10, 2026.

Use role-based owners only. Mark missing budget, data access, approval policy, and operational
confirmation as blockers. Do not invent revenue targets.
```

## `route-marketing`

```text
Create a route-launch marketing plan for HAN ⇄ PRG.
Supplied brief facts: first flight October 10, 2026; aircraft A330.
Objectives: awareness, booking intent, and inclusive Vietnam-Europe pride.

Create a route-launch fact sheet and competitive evidence ledger. Do not invent frequency,
schedule, aircraft configuration, nonstop status, fares, demand, competitors, or targets.
Clearly mark missing data and research questions.
```
