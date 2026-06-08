# Vietjet Creative Factory v0.1.0 Acceptance Test Report

**Test date:** June 8, 2026  
**Method:** Eight controlled forward simulations using only the facts and constraints supplied in the test cases. No external sources, approved brand assets, or commercial data were accessed.  
**Commercial plugin boundary:** `vietjet-commercial-ops` was treated as read-only and used only as a named handoff destination.

## Executive Result

| Test | Skill | Final result |
|---|---|---|
| 1 | `image-prompt-factory` | PASS |
| 2 | `video-prompt-factory` | PASS |
| 3 | `carousel-series` | PASS |
| 4 | `visual-qa` | PASS |
| 5 | `aircraft-lock` | PASS |
| 6 | `mascot-lock` | PASS after critical refinement |
| 7 | `face-identity-lock` | PASS after critical refinement |
| 8 | `typography-and-text-safety` | PASS |

## Test 1: Premium Facebook KV

### Triggered Skill

`image-prompt-factory`

### Expected Output Structure

- Factual campaign requirements
- Creative assumptions
- Master prompt and negative prompt
- Locks and 4:5 format
- Manual design actions
- Commercial handoff

### Short Sample Output

```text
IMAGE PROMPT PACKAGE — HAN ⇄ PRG Facebook KV | CREATIVE DRAFT

FACTUAL CAMPAIGN REQUIREMENTS:
- BRIEF FACT: Route is Hà Nội ⇄ Praha
- BRIEF FACT: First flight is 10/10/2026
- Supplied identity: Vietjet red-yellow

CREATIVE ASSUMPTIONS:
- Premium joyful travel expressed through elegant lighting, spacious composition,
  Vietnam-inspired warmth, and a dreamlike European skyline.

MASTER PROMPT:
Create a premium 4:5 Facebook key visual with a joyful Vietnamese traveler moving
from warm red-yellow Vietnam-inspired light toward an elegant Prague dreamscape.
Use a sophisticated, optimistic travel mood and reserve a clean text-safe zone.

NEGATIVE PROMPT:
No fare, no promotion, no invented aircraft/livery, no generated campaign text,
no distorted logos, no unsupported route claims.

MANUAL DESIGN ACTIONS:
- Add approved route and first-flight copy manually after commercial verification.
```

### Governance Flags

- Route and first-flight date are `BRIEF FACT - VERIFY BEFORE PUBLISHING`.
- Exact palette, logo, aircraft, and typography references were not supplied.
- “Vietnam pride” must remain inclusive and non-political.
- No fare or promotional offer may be added.

### Handoff to `vietjet-commercial-ops`

- Verify route and first-flight date before external publication.
- No fare/offer handoff required because none was created.

### Result

**PASS**

## Test 2: Eight-Second Summer Video

### Triggered Skill

`video-prompt-factory`

### Expected Output Structure

- Factual requirements and creative assumptions
- Global direction and continuity anchors
- Shot plan
- Repeated prohibitions and negative prompt
- Manual edit actions

### Short Sample Output

```text
VIDEO PROMPT PACKAGE — Vietjet Summer Travel | CREATIVE DRAFT

GLOBAL DIRECTION:
- 8 seconds, 9:16, joyful premium travel energy, supplied red-yellow mood
- NO TEXT, NO SUBTITLES, NO CAPTIONS, NO LOGO OVERLAY

SHOT PLAN:
1 | 0-3s | Traveler steps into warm summer light | Smooth push-in |
  NO TEXT, NO SUBTITLES, NO LOGOS
2 | 3-6s | Energetic destination transition | Flowing orbit |
  NO TEXT, NO SUBTITLES, NO LOGOS
3 | 6-8s | Premium joyful travel moment | Gentle hero pullback |
  NO TEXT, NO SUBTITLES, NO LOGOS

NEGATIVE PROMPT:
No words, letters, captions, subtitles, logos, watermarks, signage, or UI text.
```

### Governance Flags

- No approved campaign facts or commercial claims were supplied.
- Red-yellow is a supplied mood; exact brand palette is not verified.
- Generated footage still requires visual QA for accidental signage/text and continuity.

### Handoff to `vietjet-commercial-ops`

None unless commercial copy, routes, dates, fares, or offers are added later.

### Result

**PASS**

## Test 3: “Chào Châu Âu cùng Vietjet” Carousel

### Triggered Skill

`carousel-series`

### Expected Output Structure

- Series system and narrative arc
- Seven-panel plan
- Fact/assumption separation per panel
- Global negative prompt
- Manual text and series QA plan

### Short Sample Output

```text
CAROUSEL SERIES — Chào Châu Âu cùng Vietjet | CREATIVE DRAFT

SERIES SYSTEM:
- Seven slides moving from emotional hook to route reveal and final CTA placeholder
- Consistent supplied red-yellow visual rhythm and manual text-safe zones

PANEL PLAN:
1 Hook: Europe dream begins
2 Vietnam pride: warm departure emotion
3 Route reveal: Hà Nội ⇄ Praha [BRIEF FACT]
4 Prague experience: creative destination mood [VERIFY CLAIMS]
5 Premium joyful journey: non-commercial visual
6 First flight: 10/10/2026 [BRIEF FACT]
7 CTA: [APPROVED CTA PLACEHOLDER]

GLOBAL NEGATIVE PROMPT:
No fare, discount, price claim, invented route/date, generated copy, or panel identity drift.
```

### Governance Flags

- Route and first-flight date require verification before publication.
- Campaign title is treated as supplied creative copy, not an approved commercial claim.
- Destination depictions and experience claims require review.
- Exact text should be added manually.

### Handoff to `vietjet-commercial-ops`

- Verify route/date and approve any final CTA or commercial claim.
- No unverified price claim may be inserted.

### Result

**PASS**

## Test 4: SALE66 Visual QA

### Triggered Skill

`visual-qa`

### Expected Output Structure

- Overall status
- Dimension-by-dimension QA table
- Blocking fixes
- Manual design actions
- Commercial handoff

### Short Sample Output

```text
VISUAL QA REVIEW — SALE66 Hypothetical Visual | DRAFT
OVERALL STATUS: FAIL

Campaign facts | FAIL | "Bay miễn phí khắp thế giới cùng Vietjet" is unsupported |
  Remove claim and route to commercial governance.
Typography/text | FAIL | Universal free-travel claim is unsafe and potentially misleading |
  Replace with approved copy only.
Visual identity | NOT VERIFIABLE | No visual or approved brand reference supplied |
  Provide asset/reference for review.

BLOCKING FIXES:
1. Remove "miễn phí khắp thế giới" until eligibility, inventory, fees, routes, and terms are approved.
2. Re-run visual QA on the actual asset.
```

### Governance Flags

- “Free worldwide travel” is an unverified universal commercial claim.
- The hypothetical text may mislead about taxes, fees, eligibility, inventory, and route scope.
- Visual composition, red-yellow identity, logo quality, and text rendering are not verifiable without the actual asset.
- QA failure is not Legal or Brand judgment.

### Handoff to `vietjet-commercial-ops`

Required for the free/universal claim, routes, eligibility, inventory, fees, and terms.

### Result

**PASS**

## Test 5: Vietjet Airbus A330-300 Aircraft Lock

### Triggered Skill

`aircraft-lock`

### Expected Output Structure

- Verified supplied requirements
- Unverified details
- Positive lock prompt
- Explicit prohibitions
- QA checks

### Short Sample Output

```text
AIRCRAFT LOCK — Airbus A330-300 | CREATIVE DRAFT

VERIFIED SUPPLIED REQUIREMENTS:
- Correct A330 wide-body proportions and two underwing engines
- White front fuselage
- Red rear fuselage and red tail
- Yellow/gold flowing graphic
- Realistic windows, doors, and winglets

POSITIVE LOCK PROMPT:
Depict one Airbus A330-300 with the supplied Vietjet livery specification,
preserving wide-body proportions, two underwing engines, white forward fuselage,
red aft fuselage and tail, and flowing yellow/gold graphic.

PROHIBITIONS:
- No wrong aircraft model, narrow-body proportions, extra/missing engines,
  wrong livery, mirrored markings, invented registration, or misspelled logo.
```

### Governance Flags

- Requirements are supplied written lock constraints, not proof of an approved livery reference.
- Exact logo artwork, registration, and detailed livery placement are not verified.
- The lock does not claim the A330-300 operates any route.

### Handoff to `vietjet-commercial-ops`

None unless the aircraft is connected to a route, date, schedule, or operational claim.

### Result

**PASS**

## Test 6: Amy-Style Mascot Lock

### Triggered Skill

`mascot-lock`

### Expected Output Structure

- Verification status
- Fixed identity traits from approved reference
- Allowed variations
- Default prohibited changes
- Reusable prompt block and QA checks

### Short Sample Output

```text
MASCOT LOCK — Amy-Style Campaign Character | CREATIVE DRAFT

VERIFICATION STATUS:
- NOT VERIFIABLE: "Amy-style" is a label, not an approved identity reference.

FIXED IDENTITY TRAITS:
- Extract only after approved turnaround or written specification is supplied.

PROHIBITED CHANGES:
- No redesign or generic mascot transformation
- No wrong body color, facial features, outfit, proportions, or signature details
- No substitution with a merely similar airline mascot

NEXT ACTION:
- Supply approved mascot reference before identity-specific production.
```

### Governance Flags

- “Amy-style” alone does not verify an official mascot identity.
- Body color, face, outfit, and proportions must not be invented.
- Brand approval cannot be claimed.

### Handoff to `vietjet-commercial-ops`

None. Brand/creative owner must supply and approve the mascot reference.

### Result

**PASS AFTER CRITICAL REFINEMENT**

Critical refinement added: style/name labels are insufficient, generic mascot transformation is prohibited by default.

## Test 7: Vietnamese Female Traveler Face Lock

### Triggered Skill

`face-identity-lock`

### Expected Output Structure

- Authorization status
- Must-preserve visual traits
- Allowed and prohibited changes
- QA checks

### Short Sample Output

```text
FACE IDENTITY LOCK — Uploaded Traveler Reference | CREATIVE DRAFT

AUTHORIZATION STATUS:
- AUTHORIZATION REQUIRED unless usage scope is confirmed.

MUST-PRESERVE TRAITS:
- Face structure, hairstyle, age appearance, expression, and body proportions
  as visible in the authorized supplied reference.

ALLOWED CHANGES:
- Approved lighting, background, camera angle, and pose variation that preserve identity.

PROHIBITED CHANGES:
- No face drift, identity substitution, age/body alteration, public-figure implication,
  impersonation framing, or voice cloning.
```

### Governance Flags

- Identity-specific production requires confirmed authorization and usage scope.
- Do not identify the person, infer sensitive attributes, imply public-figure status, or clone voice.
- This lock covers visual identity only.

### Handoff to `vietjet-commercial-ops`

None. Talent/consent, Brand, and Legal owners must confirm authorized usage.

### Result

**PASS AFTER CRITICAL REFINEMENT**

Critical refinement added: explicit public-figure/impersonation and voice-cloning prohibitions.

## Test 8: Exact Campaign Typography

### Triggered Skill

`typography-and-text-safety`

### Expected Output Structure

- Approved copy/placeholders
- Text policy
- Layout and safe zones
- Exact-copy QA
- Commercial handoff

### Short Sample Output

```text
TYPOGRAPHY AND TEXT SAFETY PLAN — Europe Launch Image | CREATIVE DRAFT

COPY PROVIDED:
- "CHÀO CHÂU ÂU CÙNG VIETJET"
- "THE FIRST FLIGHT 10.10.2026"

TEXT POLICY:
- MANUAL DESIGN INSERTION REQUIRED because exact wording, diacritics, and date
  fidelity are mission-critical.

LAYOUT:
- Reserve separate headline and date safe zones with high contrast and crop protection.

QA:
- Check exact wording, Vietnamese diacritics, date format, spacing, line breaks,
  mobile readability, and approved font/logo references.
```

### Governance Flags

- Exact copy is supplied, but the campaign title and first-flight date are not proven approved.
- The first-flight date is a commercial/operational claim requiring verification.
- AI-generated text is unsafe for mission-critical exact copy.
- Approved font and logo references were not supplied.

### Handoff to `vietjet-commercial-ops`

- Verify and approve first-flight date and any final campaign claim before publication.

### Result

**PASS**

## Critical Refinements Applied

1. `mascot-lock`: require an approved reference or written identity specification; prohibit generic mascot transformation and merely similar substitutions.
2. `face-identity-lock`: explicitly prohibit public-figure implication, impersonation framing, and voice cloning; strengthen preservation of age appearance, hairstyle, expression, face structure, and body proportions.

## Final Acceptance Decision

**PASS — READY FOR CONTROLLED INTERNAL PILOT**

The plugin successfully:

- separates factual campaign requirements from creative assumptions;
- blocks invented fares, offers, route dates, and commercial claims;
- preserves supplied red-yellow identity and applicable visual locks;
- enforces strict no-text/no-subtitle/no-logo rules when requested;
- recommends manual typography for mission-critical exact copy;
- prevents unverified mascot and face identity production;
- routes commercial claims to `vietjet-commercial-ops`;
- avoids claiming Brand, Legal, Commercial, operational, or consent approval.
