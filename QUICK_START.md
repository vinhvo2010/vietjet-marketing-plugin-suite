# Quick Start

Open `<REPO_ROOT>` in Codex or Antigravity, then use one of the
following copy-paste prompts. Every output remains a draft until human review.

## 1. HAN ⇄ PRG Route Launch

```text
Use the repo-local `vietjet-commercial-ops` plugin and its `route-marketing` skill.

Create a governed route-launch brief for HAN ⇄ PRG.
Supplied facts:
- Route: HAN ⇄ PRG
- First flight: October 10, 2026
- Aircraft: A330
- Objective: awareness, booking intent, and Vietnam-Europe pride

Separate facts, assumptions, and missing data. Treat schedule, frequency, aircraft
configuration, sales-open date, market demand, competitor claims, fares, targets,
and route performance as facts to verify. Apply operating governance and identify
required evidence and human approval.
```

## 2. SALE66 Post-Booking-Period Promo QA

```text
Use the repo-local `vietjet-commercial-ops` plugin and its `promo-qa` skill.

Review SALE66 after its booking period ended on June 7, 2026.
Supplied brief claims:
- 12 million promotional tickets
- Fares from 0Đ
- Booking period: June 1-7, 2026
- Applies to all routes

Perform promo QA and post-campaign governance checks. Separate gross results from
incremental results. Do not invent inventory, bookings, revenue, yield, route
eligibility, terms, or performance. Flag missing evidence, expired-date risks,
cross-channel consistency requirements, and human approvals.
```

## 3. Deluxe Upsell CRM Sequence

```text
Use the repo-local `vietjet-commercial-ops` plugin and its `crm-personalization`
skill.

Design a governed Deluxe fare upsell sequence for eligible economy passengers
across email, app push, and the web booking flow.

Goal: increase upgrade conversion.
Separate facts, assumptions, and missing data. Do not invent Deluxe benefits,
prices, eligibility, audience size, conversion rates, revenue, frequency caps,
or approval thresholds. Include control/holdout measurement, incremental-revenue
logic, suppression rules, no-dark-pattern checks, and human approval needs.
```

## 4. A330-300 Campaign KV Prompt

```text
Use the repo-local `vietjet-creative-factory` plugin with the
`image-prompt-factory` and `aircraft-lock` skills.

Create a premium 4:5 campaign KV prompt featuring a Vietjet Airbus A330-300.
Use only supplied or approved aircraft and livery references. Preserve Vietjet
red-yellow identity, reserve a manual typography safe zone, and block wrong
aircraft proportions, wrong livery, invented registration, malformed text, and
misspelled logos.

Separate factual requirements from creative assumptions. Mark unsupported
aircraft details as not verifiable. Do not invent fares, offers, route facts, or
approvals.
```

## 5. Eight-Second No-Text Video Prompt

```text
Use the repo-local `vietjet-creative-factory` plugin and its
`video-prompt-factory` skill.

Create an 8-second 9:16 Vietjet summer-travel video prompt with joyful premium
travel energy and a red-yellow mood.

Strict rules for every shot and QA check:
- NO TEXT
- NO SUBTITLES
- NO CAPTIONS
- NO LOGO OVERLAY

Separate factual requirements from creative assumptions. Do not invent campaign
claims, fares, offers, routes, dates, or approvals. Include continuity anchors,
negative prompts, visual QA checks, and human creative review requirements.
```

## 6. End-To-End Commercial And Creative Workflow

```text
Use both repo-local plugins in this order:
1. `vietjet-commercial-ops` for commercial truth and route/campaign governance.
2. `vietjet-creative-factory` for creative prompt production and visual QA.
3. `vietjet-commercial-ops` again for any fares, dates, offers, eligibility,
   inventory, or commercial claims appearing in the creative.

Case: Build a HAN ⇄ PRG route-launch campaign and creative package.
Supplied facts:
- Route: HAN ⇄ PRG
- First flight: October 10, 2026
- Objective: awareness, booking intent, and Vietnam-Europe pride

Produce:
- Governed route-launch message hierarchy
- 4:5 KV prompt
- 9:16 no-text video prompt
- Visual QA checklist
- Commercial handoff list
- Human approval requirements

Clearly separate facts, assumptions, and missing data. Do not invent fares,
booking periods, market data, inventory, route performance, approval thresholds,
or approvers. Treat every output as a draft until human approval.
```
