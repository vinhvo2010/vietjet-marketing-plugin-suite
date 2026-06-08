---
name: promo-qa
description: Review promotional campaigns for yield leakage, unclear fare rules, weak ancillary attach, compliance risk, and brand quality before launch. Produces a structured risk score and go/no-go recommendation with required fixes.
---

# promo-qa

Before starting, read and apply [Operating Governance](../../references/operating-governance.md).

## Purpose
Act as a structured quality gate before any promotional campaign goes live. Reviews a campaign brief or promo pack against six dimensions: yield integrity, fare rule clarity, ancillary opportunity, compliance/legal, brand quality, and channel execution. Produces a risk score (Green / Amber / Red) and a mandatory fix list for Amber and Red items.

## Input Required
Provide the promotional campaign brief containing:
- Offer: fare discount %, product bundle, specific price points
- Routes and dates: origin-destination, travel window, booking window
- Channels: which channels, including OTA (yes/no)
- Target audience and volume estimate
- Yield floor (or "not yet confirmed")
- Any compliance notes or constraints already known

Optional: past performance of similar promos, current LF on target routes, ancillary attach rates.

## Connected Tools Needed
| Tool | Used For | Required? |
|---|---|---|
| Google Drive | Read existing campaign brief or promo pack | Optional — can paste |
| Google Sheets | Read route LF / yield data for context | Optional |

## Step-by-Step Workflow

**Step 1 — Yield integrity check**
- Is the yield floor confirmed and above estimated CASK? If not: RED flag.
- Is the discount depth calibrated to demand gap, or is it arbitrary? Flag if arbitrary.
- Expected revenue at floor if all seats sell at promo price: calculate and state.
- Cannibalisation risk: could this promo cause full-fare pax to refund and rebook? Assess.
- Refund arbitrage window: is the booking window close to departure (higher risk)? Flag if <7 days.

**Step 2 — Fare rule clarity check**
- Are the fare rules explicitly stated? (Minimum stay? Advance purchase? Blackout dates? Non-refundable?)
- Is the promo code logic clear (if applicable)?
- Are the terms passenger-facing and unambiguous? Flag any rule that could create customer service disputes.
- For international routes: are local regulatory tariff requirements met? [LEGAL REVIEW RECOMMENDED]
- For `0Đ`, free, or from-price claims: confirm whether taxes, fees, ancillaries, route/date exclusions, seat quotas, fare class, and payment conditions are disclosed clearly and close to the claim.
- Validate large inventory claims such as ticket counts against an authorized inventory source. If not verified, mark `BLOCK`.

**Step 3 — Ancillary opportunity check**
- Does the promo include a bundle, or is it fare-only?
- If fare-only: is there a plan to drive ancillary attach during the promo period?
- Is the promo's ancillary target defined? If not: flag as MISSING.
- Does the promo messaging create a perception that all extras are free? Flag if yes — this suppresses ancillary.

**Step 4 — Compliance and legal check**
- Does the campaign make any comparative price claims (vs. competitors)? Flag: [LEGAL REVIEW REQUIRED].
- Does the campaign include a prize, competition, or giveaway? Flag: [LEGAL REVIEW REQUIRED].
- Does the campaign make destination safety or experience claims that need verification? Flag.
- Is the promo available in markets with specific advertising regulations? Flag by country.
- GDPR/PDPA: if CRM data is used to target, is the data use compliant with privacy policy?

**Step 5 — Brand quality check**
- Does the headline communicate the offer clearly within 5 seconds?
- Is the CTA specific and action-driven?
- Does the campaign feel on-brand for Vietjet: energetic, direct, travel-driven?
- Are there any claims that feel exaggerated, unverifiable, or likely to attract regulatory attention?
- Tone check: is this appropriate for the audience and channel?

**Step 6 — Channel execution check**
- Are all channels listed in the brief accounted for in the creative/copy plan?
- Build a channel-parity matrix covering headline offer, fare basis, booking/travel dates, exclusions, taxes/fees disclosure, CTA, landing-page destination, and terms version. Any material mismatch is a `BLOCK`.
- OTA inclusion: is the OTA commission impact calculated? If OTA is included at high commission, does the promo still clear the yield floor?
- Direct channel prioritisation: is there a reason to limit to direct only? Flag if OTA inclusion will erode margin without a clear strategic reason.
- Timing: is the campaign activation date realistic given approvals needed?

## Output Format

```
PROMO QA REVIEW — [Campaign Name] | DRAFT | [Date]
====================================================

RISK SCORE: [ GREEN ] / [ AMBER ] / [ RED ]

DIMENSION 1: Yield Integrity
  Status: PASS / FLAG / BLOCK
  Finding: ___
  Required fix: ___

DIMENSION 2: Fare Rule Clarity
  Status: PASS / FLAG / BLOCK
  Finding: ___
  Required fix: ___

DIMENSION 3: Ancillary Opportunity
  Status: PASS / FLAG / BLOCK
  Finding: ___
  Required fix: ___

DIMENSION 4: Compliance & Legal
  Status: PASS / FLAG / BLOCK
  Finding: ___
  Required fix: ___

DIMENSION 5: Brand Quality
  Status: PASS / FLAG / BLOCK
  Finding: ___
  Required fix: ___

DIMENSION 6: Channel Execution
  Status: PASS / FLAG / BLOCK
  Finding: ___
  Required fix: ___
  Channel-parity matrix: ___

RISK SCORE DEFINITION:
  GREEN — All 6 dimensions PASS. Proceed to approval gate.
  AMBER — 1–2 dimensions FLAG (non-blocking issues). Fix before launch.
  RED — Any dimension BLOCK. Campaign must not launch until RED items are resolved.

MANDATORY FIX LIST (for AMBER and RED):
  1. [Fix description] — Owner: ___ — Fix by: ___
  2. ___

RECOMMENDATION: [ GO ] / [ GO WITH FIXES ] / [ NO-GO ]

[DRAFT — HUMAN APPROVAL REQUIRED. This QA review is a draft recommendation.
The designated revenue approver must confirm yield floor. Legal must review flagged compliance items.
The designated final commercial approver must approve final Go/No-Go before campaign activates.]
```

## Human Approval Checkpoint
> This QA review does not authorise a campaign to launch. It is an input to the human approval decision. Confirm the revenue, commercial, and legal approvers from the approved authority matrix. Attach the QA review to the campaign approval record as evidence of pre-launch review.

## Example Command
```
/promo-qa

Campaign: Summer seat sale — SGN-BKK and SGN-KUL
Offer: 50% off base fare. Travel 1 Jul–31 Aug. Book 1–15 Jun.
Channels: Direct (web + app) + Traveloka + Agoda.
Audience: Leisure, all segments.
Volume target: 8,000 bookings.
Yield floor: Not yet confirmed.
OTA commission: 12% on these routes.
Ancillary plan: Not specified in brief.
Compliance: No specific constraints mentioned.
```

## Risks and Guardrails
- **Missing yield floor = automatic RED** — the review cannot produce a Green or Amber score without a confirmed yield floor. Output will state: [YIELD FLOOR MISSING — automatic RED. Campaign cannot proceed to approval without this].
- **Unverified universal or free-fare claims = automatic RED** — claims such as `all routes`, `for everyone`, `free`, or `0Đ` must be supported by inventory, eligibility, exclusions, and fee disclosures.
- **Do not approve the campaign** — you review and recommend; humans decide and approve.
- **Legal items are advisory** — you flag legal risks; you do not provide legal advice. Always note: [This is a commercial review, not a legal opinion. Consult Vietjet Legal for binding compliance guidance].
- **Brand quality is subjective** — flag only clear issues (misleading claims, off-tone copy, unverifiable superlatives). Do not redesign the campaign creative in this skill — use `/brand-voice` or `/campaign-factory` for that.
