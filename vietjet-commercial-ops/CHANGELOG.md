# Changelog

## Unreleased - v0.1.1

### Planned

- Add a standard evidence-and-approval intake template for every substantive output.
- Add deterministic post-campaign and CRM measurement worksheets.
- Add explicit claim boundaries, confounder checks, confidence levels, and gross-versus-incremental separation.
- Add a lightweight audit-log schema for output tracking and human approval evidence.
- Add deterministic output IDs using `VJ-{PLUGIN}-{SKILL}-{YYYYMMDD}-{NNN}`.
- Link all governance and measurement support references from shared operating governance.
- Add a controlled internal pilot runbook covering required intake, operating flow, governance, measurement, approval gates, data boundaries, and pilot success criteria.

### Scope

- No new skills.
- No plugin scope expansion.
- Governance and measurement support files only.

## v0.1.0 - 2026-06-08

### Added

- Initial repo-local Codex plugin for Vietjet commercial operations.
- Eight validated skills:
  - `brand-voice`
  - `campaign-factory`
  - `crm-personalization`
  - `executive-reporter`
  - `promo-qa`
  - `revenue-governance`
  - `revenue-pmo`
  - `route-marketing`
- Shared operating governance applied by every skill.
- Connector availability checks and pasted/local-input fallback rules.
- Data-boundary controls for PII, PNR data, credentials, sensitive revenue data, and cross-BU access.
- Route-launch fact sheets and competitive evidence ledgers.
- Promo QA controls for `0Đ`, free/universal claims, inventory verification, and cross-channel parity.
- Transparent ancillary upsell and no-dark-pattern rules.
- Gross-versus-incremental CRM revenue correction and controlled-experiment checks.
- Executive decision options, trade-offs, and gating-evidence requirements.
- Acceptance test report covering eight realistic Vietjet commercial and marketing scenarios.

### Validation

- Plugin validator: PASS
- Eight skill validators: PASS
- Acceptance test: **8/8 PASS**
- Final review: no blocking issues
