---
name: mascot-lock
description: Build and enforce a consistent approved mascot identity lock across Vietjet creative prompts, poses, expressions, scenes, videos, and carousel series without redesigning or inventing mascot traits.
---

# Mascot Lock

Before starting, read [Creative Governance](../../references/creative-governance.md) and [Visual Lock Brief](../../references/visual-lock-brief.md).

## Use When

- An approved mascot must remain consistent across assets
- Creating pose/expression variations without identity drift
- Reviewing mascot proportions, colors, wardrobe, accessories, or continuity

## Required Inputs

- Approved mascot reference images or written specification
- Allowed pose, expression, wardrobe, and accessory range
- Prohibited changes and usage context

## Workflow

1. Confirm an approved reference or written identity specification is supplied. A name or style label such as `Amy-style` is not sufficient to verify an official mascot identity.
2. Extract only visible/supplied lock traits: silhouette, proportions, palette, face, wardrobe, accessories, and signature details.
3. Separate fixed identity traits from allowed creative variation.
4. Build reusable positive lock language and negative prompts.
5. Apply the same identity anchors across every asset or shot.
6. Mark the lock `NOT VERIFIABLE` if no approved reference is supplied.

## Output

```text
MASCOT LOCK — [Mascot] | CREATIVE DRAFT

FIXED IDENTITY TRAITS:
- ...

ALLOWED VARIATION:
- ...

PROHIBITED CHANGES:
- No redesign, generic mascot transformation, or substitution
- No wrong body color, facial features, outfit, or signature details

REUSABLE PROMPT BLOCK:
- ...

QA CHECKS:
- ...
```

## Guardrails

- Do not invent mascot history, name, personality, colors, wardrobe, or official status.
- Do not redesign the mascot or claim Brand approval.
- Do not transform the mascot into a generic airline mascot or a merely similar character.
- Keep commercial claims outside the mascot lock.
