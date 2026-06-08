---
name: image-prompt-factory
description: Create governed, production-ready image-generation prompts for Vietjet campaign visuals, key visuals, social assets, banners, destination imagery, and creative adaptations while preserving supplied brand and factual constraints.
---

# Image Prompt Factory

Before starting, read [Creative Governance](../../references/creative-governance.md), [Campaign Fact Handoff](../../references/campaign-fact-handoff.md), and [Prompt and QA Template](../../references/prompt-and-qa-template.md).

## Use When

- Creating a campaign key visual, social image, banner, destination visual, or adaptation prompt
- Converting a creative brief into one or more image-generation prompt variants
- Preparing prompts that must preserve aircraft, mascot, face, typography, logo, or color locks

## Required Inputs

- Creative objective, audience, channel, aspect ratio, and desired mood
- Supplied factual campaign requirements
- Approved visual references and applicable lock constraints
- Text/logo policy: generated, manual, or prohibited

## Workflow

1. Separate factual campaign requirements from creative assumptions.
2. Hand off missing/unapproved commercial claims to `vietjet-commercial-ops`; use placeholders or omit them.
3. Read [Visual Lock Brief](../../references/visual-lock-brief.md) when any identity lock applies.
4. Build a clear scene and composition with Vietjet red-yellow identity preserved from supplied references.
5. Add explicit negative prompts for wrong aircraft/livery, altered identities, invented logos, malformed text, and unwanted artifacts.
6. Specify manual design actions for final copy, logo, fare, dates, CTA, or legal terms when safer.
7. Produce a QA-ready prompt package.

## Output

```text
IMAGE PROMPT PACKAGE — [Asset] | CREATIVE DRAFT

FACTUAL CAMPAIGN REQUIREMENTS:
- ...

CREATIVE ASSUMPTIONS:
- ...

MASTER PROMPT:
...

NEGATIVE PROMPT:
...

LOCKS:
- ...

FORMAT / ADAPTATIONS:
- ...

MANUAL DESIGN ACTIONS:
- ...

COMMERCIAL CLAIMS FOR VIETJET-COMMERCIAL-OPS:
- ...
```

## Guardrails

- Do not invent fares, offers, route dates, campaign claims, brand assets, or exact visual identity details.
- Flag AI-generated text as unsafe unless the user explicitly accepts it; prefer a blank text-safe area.
- Do not claim the prompt or output is Brand- or Legal-approved.
