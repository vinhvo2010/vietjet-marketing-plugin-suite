---
name: carousel-series
description: Design governed, visually consistent Vietjet carousel and multi-asset series systems with panel roles, narrative progression, lock continuity, text-safe zones, and channel-ready prompt packages.
---

# Carousel Series

Before starting, read [Creative Governance](../../references/creative-governance.md), [Campaign Fact Handoff](../../references/campaign-fact-handoff.md), and [Prompt and QA Template](../../references/prompt-and-qa-template.md).

## Use When

- Designing social carousels, sequential campaign tiles, multi-image stories, or asset families
- Maintaining one campaign concept across multiple panels and sizes
- Separating image generation from final manual typography and commercial copy

## Required Inputs

- Series objective, panel count, channel, aspect ratio, audience, and CTA behavior
- Approved or supplied campaign facts
- Visual system and applicable locks
- Exact approved copy, or instruction to reserve manual text-safe zones

## Workflow

1. Define the series narrative: hook, development, proof/experience, and CTA panel.
2. Separate factual campaign requirements from creative assumptions for every panel.
3. Define fixed series anchors: palette, composition grid, subject treatment, camera logic, spacing, and text-safe zones.
4. Create one prompt per panel plus a global consistency prompt and negative prompt.
5. Keep commercial claims as approved copy or placeholders; hand off unresolved claims to `vietjet-commercial-ops`.
6. Specify final manual design and QA actions.

## Output

```text
CAROUSEL SERIES — [Name] | CREATIVE DRAFT

SERIES SYSTEM:
- Narrative arc
- Fixed visual anchors
- Typography/text policy

PANEL PLAN:
Panel | Role | Factual requirements | Creative direction | Manual text | Locks

GLOBAL NEGATIVE PROMPT:
- ...

SERIES QA:
- Continuity, hierarchy, crop safety, text safety, and claim checks
```

## Guardrails

- Do not allow panel-to-panel drift in aircraft, livery, mascot, face, wardrobe, or core palette.
- Do not invent panel copy, offers, dates, fares, or terms.
- Flag generated text and final copy insertion for manual design when appropriate.
