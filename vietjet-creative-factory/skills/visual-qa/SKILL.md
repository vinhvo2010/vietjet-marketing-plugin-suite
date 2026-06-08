---
name: visual-qa
description: Review Vietjet creative images, videos, carousel series, and prompt packages for factual consistency, brand identity, lock compliance, text safety, artifacts, channel fit, and commercial-claim handoff.
---

# Visual QA

Before starting, read [Creative Governance](../../references/creative-governance.md), [Visual Lock Brief](../../references/visual-lock-brief.md), and [Prompt and QA Template](../../references/prompt-and-qa-template.md).

## Use When

- Reviewing generated or designed visuals before human Brand/Commercial review
- Checking a prompt package for missing constraints
- Comparing an asset against approved aircraft, mascot, face, typography, or brand references

## Required Inputs

- Asset or prompt package to review
- Intended channel and format
- Supplied factual campaign requirements
- Approved references and lock brief, when available

## Workflow

1. Confirm what is verifiable from supplied references; mark absent references `NOT VERIFIABLE`.
2. Review factual campaign representation and route unresolved claims to `vietjet-commercial-ops`.
3. Review red-yellow identity, composition, channel fit, and visual quality.
4. Review all applicable locks and no-text/no-subtitle/no-logo constraints.
5. Check generated text, logo distortion, artifacts, anatomy, continuity, cropping, and safe zones.
6. Produce prioritized fixes and a draft readiness status.

## Output

```text
VISUAL QA REVIEW — [Asset] | DRAFT

OVERALL STATUS: PASS / FAIL / NOT VERIFIABLE

Dimension | Status | Evidence / finding | Required fix

BLOCKING FIXES:
1. ...

MANUAL DESIGN ACTIONS:
- ...

COMMERCIAL CLAIMS FOR VIETJET-COMMERCIAL-OPS:
- ...
```

## Guardrails

- A QA `PASS` means the supplied checks passed; it is not Brand, Legal, or Commercial approval.
- Do not claim a lock passed without the approved reference needed to compare it.
- Treat malformed or unverified text as a blocking issue for external use.
