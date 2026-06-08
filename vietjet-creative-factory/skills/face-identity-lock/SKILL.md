---
name: face-identity-lock
description: Build and enforce an authorized face identity lock for Vietjet creative prompts and QA, preserving supplied facial identity and consent scope while preventing identity drift, unauthorized substitution, and misleading edits.
---

# Face Identity Lock

Before starting, read [Creative Governance](../../references/creative-governance.md) and [Visual Lock Brief](../../references/visual-lock-brief.md).

## Use When

- A supplied, authorized person's face must remain consistent across generated assets
- Creating approved pose, wardrobe, lighting, or scene variations
- Reviewing face identity continuity

## Required Inputs

- Authorized identity reference
- Confirmation of consent/usage scope
- Must-preserve traits, permitted changes, prohibited changes, channel, and market

## Workflow

1. Confirm the user states the identity reference is authorized for the requested use.
2. If authorization or scope is unknown, stop identity-specific production and mark `AUTHORIZATION REQUIRED`.
3. Record must-preserve identity traits without inferring sensitive attributes.
4. Define allowed scene/pose changes and prohibited identity alterations.
5. Build a reusable lock prompt and QA checklist.

## Output

```text
FACE IDENTITY LOCK — [Reference ID] | CREATIVE DRAFT

AUTHORIZATION STATUS:
- ...

MUST-PRESERVE TRAITS:
- ...

ALLOWED CHANGES:
- ...

PROHIBITED CHANGES:
- No identity substitution or face drift
- No misleading age, face-structure, hairstyle, expression, or body-proportion transformation
- No public-figure implication, impersonation framing, or voice cloning
- No use beyond confirmed scope

QA CHECKS:
- ...
```

## Guardrails

- Do not infer sensitive personal attributes or identify an unknown person.
- Do not proceed with identity-specific generation when authorization is unknown.
- Do not imply the reference is a public figure, celebrity, spokesperson, or endorsed talent unless that status and usage are explicitly supplied.
- This skill covers visual identity only. Do not clone, synthesize, or specify the person's voice.
- Do not claim consent, talent, Brand, or Legal approval.
