# AI Image Asset Standard

## Required Controls

- Every generated visual, audio, and video asset must be listed in the campaign `audit/ASSET_MANIFEST.md`.
- Actual MIME type must match the filename extension.
- Pixel dimensions and aspect ratio must match the intended channel use.
- Assets must use the controlled lifecycle folders:
  - `assets/draft/`
  - `assets/rejected/`
  - `assets/approved/`
  - `assets/release/`
- Missing promised video deliverables are P0 release blockers.
- Deterministic preflight does not replace human creative QA.

## Lifecycle

1. New AI output enters `draft/`.
2. Deterministic preflight checks MIME, extension, dimensions, aspect ratio, and expected deliverables.
3. Failed assets enter `rejected/` only after an authorized human move.
4. Human-reviewed assets enter `approved/` only after evidence is logged.
5. Only release-authorized assets enter `release/`.

AI must never move an asset into `approved/` or `release/` based only on its own assessment.
