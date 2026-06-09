# Human Visual QA Review Instructions

## Purpose

Human visual QA determines whether technically valid draft stills are suitable for further internal workflow. Deterministic preflight confirms MIME, extension, dimensions, and aspect ratio only. It cannot grant human QA or release approval.

## Open The Review Index

Open:

`campaigns/football-summer-2026/review/ASSET_REVIEW_INDEX.html`

The page is local-only, has no external dependencies, and loads images only from `../html-preview/assets/draft/`.

## Review Process

1. Inspect every asset at full size where possible.
2. Complete every section in `HUMAN_VISUAL_QA_CHECKLIST.md`.
3. Record reviewer name, review date, one decision, issues found, notes, and final action in `HUMAN_VISUAL_QA_REVIEW_TABLE.md`.
4. Do not treat technical preflight as visual approval.
5. Do not place any asset into `release/` through this review.

## Human Decision Options

- `APPROVE_FOR_APPROVED_FOLDER`
- `REJECT_TO_REJECTED_FOLDER`
- `REVISION_REQUIRED`
- `NEEDS_LEGAL_IP_REVIEW`
- `NEEDS_BRAND_REVIEW`

Only a human reviewer may choose `APPROVE_FOR_APPROVED_FOLDER`.

## Movement Rules After Human Decision

- If approved by a human, copy from `html-preview/assets/draft/` to `html-preview/assets/approved/`.
- If rejected, copy or move to `html-preview/assets/rejected/`.
- Do not put anything into `release/` until the final release gate is complete.
- Do not delete draft assets.
- Update `audit/ASSET_MANIFEST.md` after any human-authorized movement.
- Re-run preflight.

Command examples only; do not execute without a recorded human decision:

```bash
cp html-preview/assets/draft/<file>.jpg html-preview/assets/approved/<file>.jpg
python3 scripts/preflight/run_preflight.py campaigns/football-summer-2026
```

The eight-second video remains a separate P0 blocker and is outside this still-image review package.
