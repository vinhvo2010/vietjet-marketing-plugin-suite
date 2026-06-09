# Production Governance Standard

## 1. Purpose

This standard prevents campaign drafts, generated assets, scenarios, and AI recommendations from being mistaken for production-ready material.

## 2. Allowed Campaign States

Only these states are allowed:

- `DRAFT_ONLY`
- `INTERNAL_REVIEW_READY`
- `PREFLIGHT_REQUIRED`
- `PREFLIGHT_FAILED`
- `PREFLIGHT_PASSED`
- `HUMAN_QA_REQUIRED`
- `HUMAN_QA_PASSED`
- `APPROVED_FOR_RELEASE`
- `BLOCKED_DATA_REQUIRED`
- `BLOCKED_ASSET_QA`
- `BLOCKED_LEGAL_IP`
- `BLOCKED_COMMERCIAL`
- `BLOCKED_MEASUREMENT`

Rules:

- AI cannot assign `APPROVED_FOR_RELEASE`.
- AI cannot assign `HUMAN_QA_PASSED`.
- AI cannot use PASS, VERIFIED, APPROVED, or COMPLETED unless supporting evidence is present in the applicable register.
- Anything without evidence remains `DRAFT_ONLY`, `HUMAN_QA_REQUIRED`, or `BLOCKED_*`.

## 3. Claims Governance

Every claim must be logged in `audit/CLAIMS_REGISTER.md`.

Claim types:

- budget
- bookings
- ABV
- gross revenue
- incremental revenue
- ROI
- fare
- offer
- booking period
- travel period
- route
- schedule
- aircraft
- inventory
- sponsorship
- partnership
- IP/license
- asset approval
- measurement result

Each claim must include:

- claim
- claim type
- source
- evidence path
- owner to confirm
- status
- external use allowed?
- notes

Allowed claim statuses:

- `VERIFIED`
- `TO_VERIFY`
- `DATA_UNAVAILABLE`
- `ASSUMPTION_ONLY`
- `CALCULATION_FROM_ASSUMPTIONS`
- `DO_NOT_USE_EXTERNALLY`
- `BLOCKED`

Rules:

- Scenario numbers must be `ASSUMPTION_ONLY` or `CALCULATION_FROM_ASSUMPTIONS`.
- Scenario numbers must not appear as an approved business case.
- Gross revenue is not incremental revenue.
- ROI cannot be claimed without verified cost and verified revenue data.
- HTML copy buttons must not copy numbers as if validated.

## 4. Asset Governance

Every visual, audio, and video asset must be logged in `audit/ASSET_MANIFEST.md`.

Required fields:

- asset id
- filename
- intended use
- required format
- actual MIME type
- actual extension
- width
- height
- aspect ratio
- duration if video
- source prompt
- generator
- generated date
- preflight status
- human QA status
- release status
- rejection reason
- notes

Required asset folders:

- `html-preview/assets/draft/`
- `html-preview/assets/rejected/`
- `html-preview/assets/approved/`
- `html-preview/assets/release/`

Rules:

- Draft AI assets go to `draft/`.
- Failed assets go to `rejected/`.
- Human-reviewed assets go to `approved/`.
- Only `release/` assets may appear in release mode.
- JPEG files must not be renamed `.png`.
- Actual MIME must match extension.
- Aspect ratio must match intended use.
- Missing promised video deliverables are P0 blockers.

## 5. HTML Microsite Governance

HTML must:

- display concept/release state clearly;
- show `CONCEPT PREVIEW — NOT PRODUCTION READY` when not release-approved;
- not call assumption-only numbers a business case;
- not copy unverified bookings or revenue into clipboard summaries;
- label AI images as draft until approved;
- load release assets only from `assets/release/` in release mode;
- include governance warnings;
- include a release blocker panel.

## 6. Release Gate

A campaign can be marked `APPROVED_FOR_RELEASE` only when:

- all claims are verified or removed;
- all assets pass deterministic preflight;
- all assets pass human QA;
- videos exist and duration is validated;
- legal/IP review is logged;
- brand review is logged;
- commercial/revenue review is logged;
- measurement review is logged;
- final authorized launch owner is confirmed by policy.

Use: **Authorized final launch owner, to be confirmed by policy.**

Do not use:

- Board of Directors
- Ban Giám đốc
