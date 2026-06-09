# Production Governance Gates Implementation Plan

## Context

- Audit source: `campaigns/football-summer-2026/CAMPAIGN_AUDIT_AND_SYSTEM_UPGRADE.md`
- Audit score: **43/100**
- Finding severity: **Blocking production-readiness finding**
- Current release state: **PREFLIGHT_REQUIRED / NOT RELEASE READY**

## P0 Findings

- Unsupported budget, bookings, ABV, revenue, ROI, and performance numbers can be mistaken for an approved business case.
- Generated visual files have MIME/extension and aspect-ratio mismatches.
- A promised eight-second video deliverable is missing.
- Generated assets may contain generated text, logos, fake UI/signage, or prohibited/off-policy visual objects.
- PASS, VERIFIED, APPROVED, and COMPLETED labels are used without evidence-register support.
- Commercial claims and clipboard summaries are not deterministically tied to evidence.

## Goal

Create deterministic production gates that keep every campaign in a blocked or review-required state until claims, assets, approvals, and measurement evidence are logged and validated.

## Files To Create

- `PRODUCTION_GOVERNANCE_STANDARD.md`
- `core/AI_IMAGE_ASSET_STANDARD.md`
- `core/HTML_PREVIEW_STANDARD.md`
- `core/GOVERNANCE_STANDARD.md`
- `scripts/preflight/*`
- `campaigns/football-summer-2026/audit/*`
- `_upgrade/production-governance-gates/VALIDATION_REPORT.md`
- Required empty asset-state folders, represented by `.gitkeep` files

## Files To Modify

- `campaigns/football-summer-2026/html-preview/index.html`
- `campaigns/football-summer-2026/html-preview/styles.css`
- `campaigns/football-summer-2026/html-preview/script.js`
- `campaigns/football-summer-2026/html-preview/README.md`
- `vietjet-creative-factory/references/generated-asset-qa-standard.md`
- `vietjet-commercial-ops/references/campaign-business-case-standard.md`

## Files Not To Touch

- Any plugin manifest
- Existing generated campaign assets
- Any file outside `<REPO_ROOT>`
- Parent repository `<PARENT_DIRECTORY>`
- Existing campaign strategy/source documents except the microsite safety files listed above

## Validation Approach

1. Run standard-library claim, asset, and HTML safety checks.
2. Generate deterministic preflight and release-readiness reports.
3. Confirm invalid assets and missing video remain P0 blockers.
4. Confirm microsite visibly states concept-only status.
5. Confirm no unsupported release approval state is assigned.
6. Inspect `git status` and verify no manifest, parent-repo, commit, or push changes.

## Rollback Note

Rollback must remove only newly created governance-gate files and revert only the four listed microsite safety files. It must never delete, move, regenerate, or modify campaign assets, plugin manifests, or parent-repository content.
