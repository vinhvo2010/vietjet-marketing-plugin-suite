# Governance Standard

## Evidence Boundary

- Do not use PASS, VERIFIED, APPROVED, or COMPLETED without evidence logged in the applicable register.
- Every campaign with factual, financial, commercial, performance, or approval claims requires `audit/CLAIMS_REGISTER.md`.
- Every release candidate requires the commercial claim linter in `scripts/preflight/check_claims.py`.
- AI may identify required approval roles but must not invent or assign approvers.

## State Boundary

Missing evidence keeps the output in `DRAFT_ONLY`, `HUMAN_QA_REQUIRED`, or an applicable `BLOCKED_*` state. AI cannot assign `HUMAN_QA_PASSED` or `APPROVED_FOR_RELEASE`.
