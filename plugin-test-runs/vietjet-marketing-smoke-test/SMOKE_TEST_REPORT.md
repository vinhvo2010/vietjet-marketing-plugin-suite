# Vietjet Marketing Plugin Suite — Smoke Test Report

Test type: lightweight functional simulation  
Plugins: `vietjet-commercial-ops`, `vietjet-creative-factory`  
Purpose: assess usefulness for common governed marketing work, not production readiness

## Test 1 — Promo QA

**User input:** SALE66; 12 million promotional tickets; fares from 0Đ; booking period 01–07/06/2026; today 08/06/2026; “Đặt ngay vé 0Đ SALE66 hôm nay, bay khắp mọi nơi cùng Vietjet!”

**Plugin/skill used:** `vietjet-commercial-ops` / `promo-qa`

**Output summary:** Blocks activation because the booking period ended before the supplied current date. Flags the 12-million inventory claim, universal route wording, 0Đ taxes/fees/exclusions, and missing yield/fare-rule evidence. Safer draft: “SALE66 đã kết thúc thời gian đặt vé ngày 07/06/2026. Theo dõi các chương trình tiếp theo của Vietjet.”  
**Governance behavior:** Human Commercial/Revenue and Legal review required; expired CTA blocked.  
**Useful output?** YES  
**Issues found:** Skill output template still uses operational labels such as PASS/GO, although its guardrails make clear they are recommendations only.  
**Score:** 5/5  
**Notes:** Strong, immediately useful promo gate.

## Test 2 — Route Launch Brief

**User input:** Hà Nội ⇄ Praha; first flight 10/10/2026; A330; Vietnam pride + Europe dream.

**Plugin/skills used:** `vietjet-commercial-ops` / `route-marketing`, `campaign-factory`

**Output summary:** Produces a route-launch fact sheet, positioning around proud modern Vietnamese travel and European discovery, audience hypotheses, messaging hierarchy, channel plan, and missing-data list. Route, date, and aircraft remain `FACT TO VERIFY`; fare, frequency, demand, and revenue are omitted.  
**Governance behavior:** Requires authorized route/Ops evidence and human Marketing/Revenue approval.  
**Useful output?** YES  
**Issues found:** Audience and channel recommendations remain hypotheses until route research is supplied.  
**Score:** 5/5  
**Notes:** Good balance of useful strategy and factual restraint.

## Test 3 — Creative Prompt For A330 KV

**User input:** Create a 4:5 Facebook key visual prompt for a Vietjet A330 campaign.

**Plugin/skills used:** `vietjet-creative-factory` / `aircraft-lock`, `image-prompt-factory`, `visual-qa`

**Output summary:** Produces a 4:5 composition prompt, aircraft-lock block covering silhouette, engines, winglets, doors, windows, tail, livery placement, registration, and negative prompt. Generated text/logo are prohibited; manual logo placement recommended.  
**Governance behavior:** Marks exact aircraft/livery details `NOT VERIFIABLE` until an approved reference is supplied; external use blocked pending reference and human QA.  
**Useful output?** YES  
**Issues found:** Cannot provide an exact Vietjet A330 identity lock without an approved aircraft/livery reference.  
**Score:** 4/5  
**Notes:** Correctly refuses to guess; useful as a reference-requesting draft.

## Test 4 — Football Campaign IP Safety

**User input:** Create a summer-football 2026 campaign that feels like World Cup.

**Plugin/skills used:** Both plugins; commercial campaign governance plus creative prompt/visual governance.

**Output summary:** Reframes the idea as “mùa hè bóng đá”, “football fever”, and “trái bóng lăn”; proposes a travel-first campaign using generic football energy, fan rituals, luggage, and red-yellow motion.  
**Governance behavior:** Blocks FIFA logo, trophy, mascot, official slogan, sponsor/partner implication, team assets, and official match-ball design; Legal/IP review required.  
**Useful output?** YES  
**Issues found:** Cross-plugin handoff is conceptually clear but relies on the user/agent to sequence the two plugins.  
**Score:** 4/5  
**Notes:** Safe alternative remains creatively usable.

## Test 5 — CRM Push Campaign

**User input:** Five app pushes for summer travel; no audience, consent, or frequency-cap data.

**Plugin/skill used:** `vietjet-commercial-ops` / `crm-personalization`

**Output summary:** Produces five short generic draft pushes without claiming personalization, for example: “Mùa hè gọi, mình lên đường thôi” and “Mở app, khám phá chuyến đi hè của bạn.”  
**Governance behavior:** Flags missing opt-in/consent, audience eligibility, suppression logic, privacy confirmation, and frequency cap. Requires opted-out and complaint/refund suppression.  
**Useful output?** YES  
**Issues found:** Copy remains broad until audience and campaign proposition are supplied.  
**Score:** 5/5  
**Notes:** Strong CRM guardrails without blocking useful drafting.

## Test 6 — Visual QA

**User input:** Generated image has fake Vietjet logo, distorted Vietnamese text, official-looking jersey, trophy-like object, and 0Đ fare text.

**Plugin/skill used:** `vietjet-creative-factory` / `visual-qa`

**Output summary:** Returns a blocking review: remove fake logo and distorted text, replace jersey with generic clothing, remove trophy-like object, and hand off 0Đ wording to Commercial Ops for evidence and terms review. Recommendation: reject or revise.  
**Governance behavior:** Does not approve the asset; separates visual, IP, brand, and commercial issues.  
**Useful output?** YES  
**Issues found:** Final determination still requires approved references and human Brand/Legal/Commercial review.  
**Score:** 5/5  
**Notes:** Clear and actionable.

## Test 7 — Business Scenario Planning

**User input:** Create a business case with no budget, baseline, CTR, conversion, or ABV.

**Plugin/skills used:** `vietjet-commercial-ops` / `revenue-governance`, `revenue-pmo`

**Output summary:** Refuses a final business case; creates a planning-scenario template with required inputs, assumptions register, validation backlog, gross-versus-incremental boundary, and measurement dependencies. No ROI claim.  
**Governance behavior:** Requires baseline, cost, conversion, ABV, control/holdout, and human Finance/Revenue validation.  
**Useful output?** YES  
**Issues found:** `revenue-pmo` tends toward a 12-week execution plan and is heavier than needed for a quick scenario worksheet.  
**Score:** 4/5  
**Notes:** Governed result is correct; workflow could be lighter.

## Test 8 — End-to-End Campaign Mini Flow

**User input:** “Bay Là Thích Ngay Mùa Hè”; awareness objective; no offer/fare; strategy, 4:5 KV prompt, 9:16 video prompt, five captions, and measurement outline required.

**Plugin/skills used:** Both plugins; `campaign-factory`, creative prompt skills, and commercial handoff.

**Output summary:** Produces an awareness strategy, audience hypotheses, travel-first message platform, five safe captions, 4:5 KV prompt with blank typography zone, 9:16 no-claim video prompt, and awareness measurement outline. No fare or offer is invented.  
**Governance behavior:** Clearly hands commercial claims back to Commercial Ops and requires Brand, Commercial, Creative, and Measurement human review.  
**Useful output?** YES  
**Issues found:** Multi-skill orchestration is manual and could be more discoverable.  
**Score:** 4/5  
**Notes:** Useful mini campaign pack with appropriate boundaries.

## Overall Result

- **Total tests run:** 8
- **Passed:** 6
- **Partially passed:** 2
- **Failed:** 0
- **Average score:** 4.5/5

### Main Strengths

- Strong protection against invented fares, route facts, performance, and approval.
- Commercial-to-creative handoff works logically.
- Outputs remain useful even when data is missing.
- Promo, CRM, visual QA, and route-launch workflows are practical.

### Main Weaknesses

- Cross-plugin orchestration depends on the user or agent choosing the right sequence.
- Some templates use PASS/GO-style language that needs careful interpretation as draft recommendation.
- Revenue PMO is too heavy for quick planning-scenario requests.
- Aircraft creative cannot progress far without approved visual references.

### Top 5 Improvements Needed

1. Add clearer examples showing commercial-to-creative handoff sequencing.
2. Make draft-recommendation wording more consistent across skill output templates.
3. Provide a lightweight business-scenario path before invoking full Revenue PMO.
4. Add a standard “missing approved reference” response for aircraft and identity locks.
5. Improve suite-level skill selection guidance for end-to-end campaign requests.

## Recommendation

**Keep and improve.**

The suite is useful for real internal Vietjet marketing drafting and governance. It does not need a rebuild or split. Add commands only if the team needs simpler repeatable orchestration after pilot usage confirms the most common flows.
