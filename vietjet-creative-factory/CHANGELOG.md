# Changelog

## v0.1.0 - 2026-06-08

### Added

- Initial repo-local Codex plugin for governed Vietjet creative production.
- Eight validated creative skills:
  - `image-prompt-factory`
  - `video-prompt-factory`
  - `carousel-series`
  - `visual-qa`
  - `aircraft-lock`
  - `mascot-lock`
  - `face-identity-lock`
  - `typography-and-text-safety`
- Shared governance and lock references for campaign-fact separation, visual locks, prompt structure, and visual QA.
- Commercial-claim handoff to `vietjet-commercial-ops`.
- Image prompt factory for campaign visuals, key visuals, and adaptations.
- Video prompt factory with strict no-text, no-subtitle, and no-logo rules.
- Carousel series planning with panel-level consistency and manual copy handoff.
- Visual QA using PASS, FAIL, and NOT VERIFIABLE statuses.
- Aircraft model and livery identity locks.
- Mascot consistency locks.
- Authorized face identity preservation locks.
- Typography and text-safety planning with manual design recommendations.

### Critical Refinements

- Mascot lock blocks generic mascot transformation and requires an approved identity reference or written specification.
- Face identity lock blocks public-figure implication, impersonation framing, and voice cloning.

### Validation

- Plugin validator: PASS
- Eight skill validators: PASS
- Acceptance tests: **8/8 PASS**
- `vietjet-commercial-ops`: unchanged
- Release decision: ready for controlled internal pilot
