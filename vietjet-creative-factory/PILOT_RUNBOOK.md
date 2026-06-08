# Vietjet Creative Factory Controlled Internal Pilot Runbook

**Plugin:** `vietjet-creative-factory v0.1.0`  
**Pilot model:** Governed prompt, visual-system, lock, and QA drafting only

## Purpose

Use `vietjet-creative-factory` to create and review governed AI creative prompts and specifications for Vietjet campaign images, videos, carousel series, aircraft visuals, mascot visuals, authorized face identity, typography, and visual QA.

The plugin creates creative drafts. It does not grant Brand, Legal, Commercial, operational, or consent approval.

## Who Can Use It

- Creative and design teams
- Brand and marketing teams
- Social, content, video, and motion teams
- Campaign production and creative operations
- AI creative-production and QA teams

Users must have authorized access to any campaign facts, brand assets, aircraft/livery references, mascot references, or face identity references used.

## What It Can Be Used For

- Image-generation prompt packages and campaign KVs
- Video prompts, shot plans, continuity anchors, and text-free footage directions
- Carousel and multi-asset series systems
- Visual QA and blocking-fix reviews
- Aircraft model and livery locks
- Mascot consistency locks
- Authorized face identity preservation locks
- Typography, exact-copy, subtitle, logo, and text-safety plans

## What It Must Not Be Used For

- Inventing or approving routes, dates, fares, offers, inventory, eligibility, terms, or commercial claims
- Claiming Brand, Legal, Commercial, operational, or talent/consent approval
- Publishing final assets without human creative and required commercial review
- Inventing exact Vietjet colors, fonts, logos, liveries, mascots, uniforms, or identity references
- Producing identity-specific face work without confirmed authorization and usage scope
- Public-figure implication, impersonation framing, or voice cloning
- Treating prompt compliance as proof that generated output is compliant

## Required Creative Intake Before Every Run

Record:

- Creative objective and intended audience
- Usage channel, dimensions/aspect ratio, duration, and market
- Factual campaign requirements and their source/approval status
- Creative assumptions
- Applicable locks: brand, aircraft/livery, mascot, face, typography, text, subtitle, logo, or composition
- Approved reference assets or written specifications
- Required manual design actions
- Commercial claims requiring handoff

Use [Campaign Fact Handoff](references/campaign-fact-handoff.md) and [Visual Lock Brief](references/visual-lock-brief.md).

## Required Brand, Aircraft, Mascot, and Face Reference Checks

- Preserve only supplied approved Vietjet red-yellow identity and assets.
- Mark any missing brand reference `LOCK NOT VERIFIED`.
- Aircraft locks require a supplied model and approved livery reference or written specification.
- Mascot locks require an approved reference or written identity specification; a style/name label alone is insufficient.
- Face identity locks require confirmed authorization and usage scope.
- Do not infer missing identity details or claim a lock passed without a comparison reference.

## Text Safety Rules

- Separate approved copy from unverified commercial claims.
- Prefer blank text-safe zones and manual typography for final external assets.
- Recommend manual design-software insertion when exact wording, spelling, Vietnamese diacritics, dates, fares, CTA, logos, or disclaimers are mission-critical.
- Treat malformed text, altered logos, missing required disclaimers, or unsafe commercial copy as blocking issues.

## No-Text / No-Subtitle / No-Logo Video Rules

When requested, repeat these constraints in:

1. Global video direction
2. Every relevant shot
3. Negative prompt
4. Visual QA checklist

Use explicit wording:

```text
NO TEXT
NO SUBTITLES
NO CAPTIONS
NO LOGO OVERLAY
NO WATERMARKS OR SIGNAGE TEXT
```

Any violation blocks external use.

## Commercial Claim Handoff

Use `vietjet-commercial-ops` to validate or govern:

- Route, flight, schedule, aircraft-operation, or launch facts
- Fare, offer, booking/travel dates, inventory, eligibility, CTA, or terms
- Promotional, universal, free, or comparative claims
- Commercial approval or compliance workflow

Creative work may continue with placeholders or a non-commercial concept. This plugin must not invent or approve the claim.

## Standard Operating Flow

```text
Intake
  → Skill selection
  → Prompt generation
  → Lock check
  → Visual QA
  → Human creative review
  → Commercial handoff if needed
  → Final asset handoff
```

| Stage | Required result before continuing |
|---|---|
| Intake | Facts and assumptions separated; channel, format, references, locks, and prohibitions recorded |
| Skill selection | Correct creative skill and supporting locks selected |
| Prompt generation | Prompt/specification uses only supplied facts and marks manual actions |
| Lock check | Required references compared or marked NOT VERIFIED |
| Visual QA | Blocking artifacts, text, identity, factual, and channel issues resolved |
| Human creative review | Creative/Brand owner records decision; plugin does not self-approve |
| Commercial handoff | Unresolved claims reviewed by `vietjet-commercial-ops` where needed |
| Final asset handoff | Approved references, copy, conditions, and final files handed to authorized production owner |

## Pilot Use Cases

### 1. HAN ⇄ PRG 4:5 KV

- Primary skill: `image-prompt-factory`
- Controls: route/date remain brief facts until verified; no fare invention; red-yellow reference; manual copy zone

### 2. Vietjet Eight-Second Summer Travel Video Prompt

- Primary skill: `video-prompt-factory`
- Controls: 9:16, strict no-text/no-subtitle/no-logo rules, continuity anchors, manual end-card handoff

### 3. “Chào Châu Âu cùng Vietjet” Seven-Slide Carousel

- Primary skill: `carousel-series`
- Controls: panel continuity, route-fact preservation, no unverified price claims, manual text-safe zones

### 4. A330-300 Aircraft Identity Lock

- Primary skill: `aircraft-lock`
- Controls: correct wide-body/two-engine form and supplied livery; no wrong model, livery, logo, or registration

### 5. Mascot Amy Identity Lock

- Primary skill: `mascot-lock`
- Controls: approved identity reference required; no redesign, generic transformation, wrong body color, face, or outfit

### 6. Face Identity Lock for Uploaded Vietnamese Female Traveler Reference

- Primary skill: `face-identity-lock`
- Controls: authorization required; preserve visual identity and proportions; no public-figure implication, impersonation, or voice cloning

## Human Review Gates

- Creative/Brand review is required before final asset handoff.
- Commercial review through `vietjet-commercial-ops` is required when the asset contains unresolved commercial claims.
- Legal or consent review is required when applicable, but the plugin must not assign or claim those approvals.
- Aircraft, mascot, face, typography, and logo locks require human comparison to approved references.
- A visual QA `PASS` is not approval.

## Data-Boundary Rules

- Do not invent campaign facts, route facts, dates, fares, offers, inventory, eligibility, or terms.
- Do not invent exact brand assets, fonts, colors, logos, liveries, mascot traits, or face identity details.
- Clearly separate factual campaign requirements from creative assumptions.
- Do not expose or repurpose unauthorized identity references.
- Do not infer sensitive personal attributes or identify unknown people.
- Use placeholders or omit unresolved facts.

## Output ID Examples

```text
VJ-CREATIVE-IMAGE-20260608-001
VJ-CREATIVE-VIDEO-20260608-001
VJ-CREATIVE-VISQA-20260608-001
```

Retain the output ID across revisions and record which skills and locks were applied.

## Pilot Success Criteria

- [ ] 100% of outputs separate factual campaign requirements from creative assumptions
- [ ] 100% of outputs record applicable locks and unverified references
- [ ] 100% of outputs include manual design actions where exact text/logo/terms are risky
- [ ] 100% of no-text/no-subtitle/no-logo videos repeat prohibitions across prompt and QA
- [ ] 100% of unresolved commercial claims hand off to `vietjet-commercial-ops`
- [ ] No invented unsupported campaign, identity, aircraft, or brand details
- [ ] No unauthorized public-figure implication, impersonation framing, or voice cloning
- [ ] Human creative review required before final asset handoff

Any failed criterion must be documented and corrected before continuing the pilot.
