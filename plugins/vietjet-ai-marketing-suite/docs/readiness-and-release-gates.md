# Vietjet AI Marketing Suite v5.1 — Offline readiness and release-review gates

**Status:** pre-production / developer preview. These are read-only, offline checks. They do not certify data accuracy, privacy, airline safety, compliance, approval signatures, provider connectivity, or external release.

## Decision boundary

- `team-plan` and `team-prompts` select specialists; they do not execute them.
- `connector-status` inspects the presence of environment variables declared in JSON blueprints. It does not contact providers, inspect secret values, or verify permissions.
- `evidence-check` checks `VERIFIED` evidence references for provenance metadata and expiry. It cannot verify that a cited source is true.
- `release-check` checks the exact artifact's SHA-256, cited evidence, and the presence of approval references. Success means `READY_FOR_HUMAN_REVIEW`, **never permission to publish**.
- Any publication, advertising spend, fare/inventory edit, customer-data processing, or aviation safety statement requires independent human and platform enforcement.

## Commands

```bash
cd plugins/vietjet-ai-marketing-suite
python3 runtime/vietjet_runtime.py doctor
python3 runtime/vietjet_runtime.py connector-status
python3 runtime/vietjet_runtime.py evidence-check /path/to/evidence-ledger.json
python3 runtime/vietjet_runtime.py release-check /path/to/release-packet.json /path/to/evidence-ledger.json --artifact /path/to/exact-asset.pdf
python3 tests/test_readiness.py
python3 scripts/validate_suite.py
```

## Contract

Each evidence entry must have a unique `claim_id`, valid `claim_type` and `data_label`. A `VERIFIED` claim requires a source reference, owner, and time-zone-aware ISO-8601 `checked_at` and `expires_at`; expiry or invalid metadata fails closed. Illustrative/unverified entries remain in the ledger, but cannot substantiate a claim in a release packet.

A release check requires matching mission IDs, verified fresh evidence for every cited claim, exactly matching artifact bytes, a named owner and target, a rollback plan, and nonempty approval references. These approval references are **unverified assertions**; an external authorization system must check identity, scope, target, immutable digest, expiry and revocation.

Outputs omit full claim text and secret values. `CONFIGURED_UNVERIFIED` only indicates local environment variables are populated, not that the provider works.

## Production gates still open

1. Secure, scoped provider identities and real connector contract tests.
2. PII-free aggregate airline retail, booking funnel, measurement, paid-media and CRM data.
3. An approved human authority matrix, cryptographic approval tied to immutable artifact hash and target, revocation and audit log.
4. Platform-enforced prevention of unauthorised spend, publication, price, PII and operational changes.
5. Independent-account UAT, safety/legal/privacy/brand review, and publication-channel approvals.

**Level 2 locally coordinated pilot only.** Neither this CLI nor the status field of a release packet authorizes external actions.

Recommended integration priority: Airline Commerce → Marketing Measurement → Paid Media → CDP (proposal, not a completed integration).
All handoffs preserve `STATUS / DECISION / EVIDENCE / OUTPUT / APPROVALS / NEXT`.
