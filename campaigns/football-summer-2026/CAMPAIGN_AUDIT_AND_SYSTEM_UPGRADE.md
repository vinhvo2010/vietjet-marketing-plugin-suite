# Campaign Audit And System Upgrade Proposal

**Campaign reviewed:** `BAY TỚI MÙA HÈ BÓNG ĐÁ`  
**Review date:** June 9, 2026  
**Review scope:** Campaign package, leadership brief, working documents, microsite,
generated visual assets, commercial governance, creative governance, and measurement
framework  
**Plugins applied:** `vietjet-commercial-ops`, `vietjet-creative-factory`  
**Status:** Internal audit draft - human review required

## Executive Verdict

The campaign has a strong strategic concept, a useful IP-safe language direction,
and a well-structured internal preview. It is suitable for internal concept
discussion.

It is **not ready for production, external publication, budget approval, or
activation**.

The largest issue is systemic: governance rules are documented, but they are not
enforced as deterministic gates. As a result, later production work introduced
invented commercial figures, incorrect asset formats, visual-rule violations, and
unsupported `PASS`, `VERIFIED`, `APPROVED`, and completion claims.

**Overall readiness score: 43/100**

| Area | Score | Assessment |
|---|---:|---|
| Strategic platform | 78/100 | Clear, extensible, travel-led concept |
| IP and language intent | 75/100 | Strong rules, inconsistently enforced |
| Commercial data boundary | 25/100 | Invented planning figures violate original boundary |
| Creative governance | 42/100 | Good prompts, visual outputs fail several locks |
| Asset production readiness | 18/100 | Wrong dimensions/formats; no actual video asset |
| Measurement design | 62/100 | Gross/incremental separation is good; assumptions are hardcoded |
| Microsite/internal review UX | 60/100 | Useful preview, but exposes unsafe business figures prominently |
| Approval and audit evidence | 30/100 | Status labels exist; evidence-backed approvals do not |

## What Worked Well

1. The core platform, “mùa hè bóng đá,” is independent and does not require an
   official tournament relationship.
2. The campaign consistently states that it must not imply official sponsorship or
   partnership.
3. The prompt pack includes broad negative prompts for official tournament assets,
   ticket claims, text, logos, and commercial claims.
4. The master campaign draft clearly distinguishes gross revenue from incremental
   revenue and describes the need for a control/holdout.
5. The microsite is self-contained, responsive in intent, and visibly labeled as an
   internal draft.
6. Asset naming is organized and the carousel has a coherent narrative sequence.
7. Manual typography and human review are repeatedly recommended.

These are strong foundations worth retaining.

## P0 Findings: Must Fix Before Any Production Or External Use

### P0.1 Invented Commercial And Market Figures

The original campaign rules prohibited inventing offer, fare, booking period,
inventory, revenue, and market data. Later documents introduced specific media
budgets, reach, impressions, bookings, ABV, gross revenue, holdout percentages,
frequency caps, and complaint thresholds.

Examples:

- `BAY_TOI_MUA_HE_BONG_DA_CAMPAIGN.md` contains a new Section 13 with invented
  planning scenarios up to `90.0B VND` gross revenue.
- `BAY_TOI_MUA_HE_BONG_DA_LEADERSHIP_BRIEF.md` repeats the invented scenarios.
- `working-docs/MEDIA_PLAN_DRAFT.md` and `working-docs/MEASUREMENT_WORKSHEET.md`
  hardcode these figures.
- `html-preview/index.html` and `html-preview/script.js` expose and copy the figures.

Labeling figures as assumptions is helpful but does not satisfy the explicit
no-invention rule. The figures can anchor leadership decisions and can be separated
from their warning labels when copied or screenshotted.

**Required action:** Replace all unsupported values with `DATA UNAVAILABLE`,
`INPUT REQUIRED`, or formulas without numeric inputs. Only add scenario values from
an authorized source with owner, date, confidence, and usage restriction.

### P0.2 Generated Assets Fail Their Own Governance Rules

Visual inspection found several direct conflicts with the prompt and governance
rules:

| Asset | Finding | Status |
|---|---|---|
| `app-banner-football-summer.png` | Generated ball logo and embedded word `FOOTBALL` | `FAIL` |
| `story-9x16-football-travel.png` | Aircraft appear despite `no planes`; static square image, not 9:16 video | `FAIL` |
| `hero-football-travel.png` | Embedded airport signage text despite no-generated-text direction | `FAIL` |
| `airport-screen-football-summer.png` | Embedded signage and display text; not a 16:9 screen asset | `FAIL` |
| `carousel-02-team.png` | Embedded airport signage; visual lacks football-series continuity | `FAIL` |
| `carousel-04-community.png` | Embedded `GOAL` and `SUNSET BEACH BAR`; team-like kits; match footage shown on phone | `FAIL` |
| `carousel-06-challenge.png` | Ball contains an unverified emblem/design | `NOT VERIFIABLE` |
| Multiple ball assets | Ball patterns and symbols have no approved generic-ball lock | `NOT VERIFIABLE` |

Negative prompts reduce risk but do not prove compliance. Every generated output
must be reviewed as an artifact.

**Required action:** Mark current visuals as rejected mockups or `QA REQUIRED`.
Regenerate or manually retouch failed assets, then complete evidence-backed Visual
QA.

### P0.3 Asset Specifications Are Technically Incorrect

All 13 files named `.png` are actually JPEG files at `1024x1024`.

Therefore:

- The claimed 16:9, 4:5, 9:16, and 3:1 deliverables do not exist.
- The 8-second video deliverable does not exist; only a square static image exists.
- The app banner, airport screen, story, hero, dashboard, and carousel assets are
  not production-ready for their stated placements.
- File extensions do not match file contents.

**Required action:** Validate MIME type, extension, pixel dimensions, aspect ratio,
duration, codec, file size, safe zones, and channel specification before accepting
an asset.

### P0.4 Unsupported Completion And Approval Claims

Current materials contain claims such as:

- All assets strictly exclude prohibited content.
- Creative assets are completed and integrated.
- QA result is `PASS`.
- Music rights are `APPROVED`.
- Brand identity is `VERIFIED AGAINST APPROVED REFERENCE`.
- Mockups meet an IP-safe standard.

The inspected evidence does not support these claims. No approved references,
approval records, rights evidence, or completed visual QA records were supplied.

**Required action:** Permit `PASS`, `VERIFIED`, `APPROVED`, `COMPLETED`, and
`READY` only when an evidence link, reviewer, review date, and scope are recorded.
Otherwise use `DRAFT`, `PENDING`, `NOT VERIFIABLE`, or `FAIL`.

### P0.5 Microsite Amplifies Unsupported Business Figures

The microsite makes the invented business scenarios a prominent interactive
feature. Its copy-summary button places unsupported budgets, bookings, and revenue
figures directly on the clipboard, where warnings can easily be lost.

**Required action:** Remove numeric scenario values until authorized inputs exist.
The microsite should show an input-readiness dashboard and formulas, not invented
outputs.

## P1 Findings: High-Value Improvements

### P1.1 Source-Of-Truth Drift

The master package originally defined 12 sections but later gained a Section 13
containing unsupported scenarios. Similar content is duplicated across the master
package, leadership brief, media plan, measurement worksheet, microsite HTML, and
JavaScript.

This creates contradictory status and makes correction expensive.

**Recommendation:** Establish one campaign fact register and one approved claims
register. All other outputs must reference or derive from those sources.

### P1.2 Prompt Rules Are Not Machine-Tested

Prompts repeat negative instructions, but outputs can still contain text, logos,
aircraft, kit-like clothing, and unverified ball marks.

**Recommendation:** Add an asset preflight step that checks OCR/text, dimensions,
format, metadata, and prohibited-object findings before human Visual QA.

### P1.3 Brand References Are Assumed

The creative brief and microsite hardcode color values and present a constructed
`Vietjet Marketing Hub` logo treatment. No approved brand references were provided.

**Recommendation:** Mark exact colors, fonts, logo treatments, and livery as
`LOCK NOT VERIFIED` until approved assets are supplied.

### P1.4 Channel Specifications Conflict

Examples include:

- App banner described as both 3:1 and 16:9 in different documents.
- Story/Reels asset described as video but delivered as a static image.
- Carousel and wide-format assets delivered as identical square dimensions.

**Recommendation:** Maintain a single asset manifest with one authoritative
specification per asset ID.

### P1.5 Missing Provenance And Review Records

The asset folder lacks a deterministic record of model, generation date, prompt
version, source reference, seed, edits, reviewer, QA result, and approval evidence.

**Recommendation:** Create a media provenance manifest and one QA record per asset.

### P1.6 Archive Hygiene

`html-preview.zip` contains `__MACOSX` metadata. The campaign folder also contains
`.DS_Store`.

**Recommendation:** Package release artifacts from a clean allowlist and exclude
system metadata.

## P2 Improvements

- Use an explicit asset-ID convention across briefs, filenames, QA records, and
  measurement reports.
- Add Vietnamese-language proofreading and native-speaker review as a separate
  gate.
- Add accessibility checks for contrast, alt text, motion, keyboard behavior, and
  readable safe zones.
- Add a clear distinction between concept mockup, production master, channel
  adaptation, and published asset.
- Keep the internal microsite focused on decisions and blockers instead of
  presenting speculative dashboards.

## Recommended Universal Campaign Operating System

The following operating model should apply to every future campaign, regardless of
theme, route, offer, or channel.

### Standard Campaign Folder

```text
campaigns/<campaign-slug>/
├── 00-intake/
│   ├── evidence-and-approval-intake.md
│   ├── fact-register.md
│   └── claim-register.md
├── 01-strategy/
│   ├── campaign-brief.md
│   └── leadership-brief.md
├── 02-commercial/
│   ├── offer-and-terms.md
│   └── measurement-plan.md
├── 03-creative/
│   ├── creative-brief.md
│   ├── prompt-pack.md
│   └── asset-manifest.md
├── 04-assets/
│   ├── raw/
│   ├── review/
│   └── approved/
├── 05-qa/
│   ├── automated-preflight.md
│   ├── visual-qa.md
│   └── approval-record.md
├── 06-preview/
└── 07-release/
```

Only files in `04-assets/approved/` may enter `07-release/`.

### Mandatory Gates

| Gate | Required output | Blocking condition |
|---|---|---|
| G0 Intake | Owner, objective, scope, risk, usage | Owner/scope unavailable |
| G1 Fact Lock | Facts, assumptions, missing data, evidence | Material facts unsupported |
| G2 Strategy | Approved campaign direction | Strategy approval absent |
| G3 Commercial Lock | Offer, fare, dates, inventory, CTA, terms | Any commercial claim unresolved |
| G4 Creative Lock | Approved references, IP rules, prompt package | Brand/IP references missing |
| G5 Automated Asset Preflight | Format, dimensions, duration, OCR, metadata | Technical spec or prohibited text fails |
| G6 Human Visual QA | Artifact-by-artifact review | Any `FAIL` or `NOT VERIFIABLE` blocker |
| G7 Production Approval | Brand, Legal/IP, Commercial, channel owners | Evidence-backed approval absent |
| G8 Release Check | Approved asset allowlist and release package | Draft/review files included |
| G9 Measurement | Valid data, claim boundary, gross vs incremental | Unsupported performance claim |

### Deterministic Asset Manifest

Every asset should have:

| Field | Requirement |
|---|---|
| Asset ID | Unique and stable |
| Intended channel | One confirmed placement |
| Required format | MIME, extension, dimensions, aspect, duration |
| Prompt version | Exact prompt and negative prompt reference |
| Approved reference IDs | Brand, aircraft, mascot, face, IP references |
| Model / tool / date | Provenance |
| Source status | Raw / review / approved / rejected |
| Automated preflight | Pass/fail with evidence |
| Human Visual QA | Reviewer, date, result, required fixes |
| Commercial handoff | Required/complete/not applicable |
| Final approval | Evidence-backed status only |

### Automated Preflight Rules

Run before human Visual QA:

1. Verify extension matches MIME type.
2. Verify exact pixel dimensions and aspect ratio.
3. Verify video duration, frame size, codec, and audio policy.
4. Run OCR and block unexpected text.
5. Flag possible logos, emblems, watermarks, aircraft, faces, and prohibited
   objects for human review.
6. Confirm file size and color profile meet channel requirements.
7. Confirm filename and asset ID match the manifest.
8. Confirm prompt, source, and generation metadata exist.
9. Confirm no unsupported numeric or commercial claims appear in companion copy.
10. Prevent status transition to `APPROVED` until required human evidence exists.

### Commercial Claim Linter

Every campaign should scan copy and code for:

- Currency, percentages, quantities, dates, routes, inventory, fares, offers,
  booking periods, revenue, bookings, reach, impressions, market claims, and
  superlatives.
- Prohibited IP and partnership terms.
- `APPROVED`, `VERIFIED`, `PASS`, `READY`, and `COMPLETED` without evidence.

Each finding must link to one of:

- An authorized fact/evidence entry
- A clearly labeled formula with empty inputs
- A placeholder
- A blocker

### Status Vocabulary

Use only:

| Status | Meaning |
|---|---|
| `DRAFT` | Work in progress |
| `PENDING REVIEW` | Ready for named human review |
| `NOT VERIFIABLE` | Required evidence/reference absent |
| `FAIL` | A requirement is violated |
| `APPROVED WITH CONDITIONS` | Evidence-backed approval with recorded conditions |
| `APPROVED` | Evidence-backed approval for a defined scope |
| `REJECTED` | Must not proceed |

Do not equate file existence, generation completion, or microsite rendering with
approval.

## Proposed Upgrade Roadmap

### Phase 1: Immediate Control Upgrade

1. Quarantine unsupported business scenarios from leadership and microsite views.
2. Mark all current visual assets `QA REQUIRED`; remove unsupported `PASS` claims.
3. Introduce the fact register, claim register, and asset manifest.
4. Add technical media validation and OCR preflight.
5. Require approval evidence before status promotion.

### Phase 2: Reusable Campaign Template

1. Create the standard campaign folder structure.
2. Create reusable intake, manifest, QA, approval, and release templates.
3. Add a campaign-copy linter for unsupported numbers and prohibited terms.
4. Generate previews only from manifest-approved content.
5. Package releases from an explicit allowlist.

### Phase 3: Controlled Automation

1. Automate technical preflight and status dashboards.
2. Integrate approved reference libraries when authorized.
3. Add connector-based evidence retrieval only with access and data governance.
4. Add post-campaign measurement using authorized data and valid control design.

## Current Campaign Recommendation

**Internal strategy discussion:** `PROCEED WITH CONDITIONS`  
**Creative regeneration and QA:** `PROCEED WITH CONDITIONS`  
**Leadership budget decision:** `NO-GO`  
**External publication or activation:** `NO-GO`

### Required Next Human Decisions

1. Confirm whether all unsupported scenario figures must be removed or replaced
   with authorized inputs.
2. Assign Brand and Legal/IP reviewers for the creative system and generated
   assets.
3. Approve the authoritative asset specifications and channel placements.
4. Decide which current assets should be rejected, retouched, or regenerated.
5. Assign owners for Commercial, CRM/Privacy, measurement, and final release.

## Final Governance Block

```text
STATUS: DRAFT - HUMAN APPROVAL REQUIRED

FACTS:
- The campaign has a complete internal strategy and preview package.
- All 13 generated image files are JPEG 1024x1024 despite their .png names.
- Multiple inspected assets violate stated prompt or governance constraints.
- Unsupported commercial scenarios appear across campaign documents and microsite.

ASSUMPTIONS:
- The campaign will remain internal until blockers are resolved.
- The recommended universal operating model can be adopted for future campaigns.

MISSING DATA:
- Approved commercial inputs and evidence
- Approved Brand/IP reference assets
- Evidence-backed Visual QA and approval records
- Authorized owners and final release decision

NEXT HUMAN DECISION:
- Approve the P0 remediation plan and universal campaign operating model before
  further production or external use.
```
