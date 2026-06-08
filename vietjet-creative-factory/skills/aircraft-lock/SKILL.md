---
name: aircraft-lock
description: Build and enforce an aircraft model and Vietjet livery lock for creative prompts and visual QA, preventing model substitution, livery drift, mirrored markings, invented registrations, and inconsistent aircraft details.
---

# Aircraft Lock

Before starting, read [Creative Governance](../../references/creative-governance.md) and [Visual Lock Brief](../../references/visual-lock-brief.md).

## Use When

- An aircraft must appear in an image, video, carousel, or campaign visual
- The user supplies an aircraft model, livery specification, registration, or approved reference
- Reviewing aircraft accuracy and continuity

## Required Inputs

- Aircraft model and approved reference
- Approved livery reference or written specification
- Camera angle/side, environment, and registration visibility requirement
- Known prohibited substitutions or edits

## Workflow

1. Record the supplied aircraft model and livery as factual requirements; do not infer missing details.
2. Identify visible lock points: silhouette, engines, winglets, windows, doors, tail, fuselage markings, registration, and livery placement.
3. Convert the lock into positive prompt instructions and explicit prohibitions.
4. Apply the same anchors to every shot/panel.
5. QA against the supplied reference; mark unsupported details `NOT VERIFIABLE`.

## Output

```text
AIRCRAFT LOCK — [Model] | CREATIVE DRAFT

VERIFIED REQUIREMENTS:
- ...

LOCK NOT VERIFIED:
- ...

POSITIVE LOCK PROMPT:
- ...

PROHIBITIONS:
- No model substitution
- No livery redesign or color drift
- No mirrored/wrong-side markings
- No invented registration

QA CHECKS:
- ...
```

## Guardrails

- Never guess aircraft model, registration, livery details, or operational route assignment.
- Aircraft appearance in creative does not verify operational use.
- Preserve supplied Vietjet red-yellow livery constraints exactly as referenced.
