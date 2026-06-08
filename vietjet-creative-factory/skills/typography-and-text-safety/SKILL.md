---
name: typography-and-text-safety
description: Plan and review safe typography, copy placement, text-free generation, subtitles, logos, disclaimers, and manual design handoff for Vietjet images, videos, and carousel assets.
---

# Typography and Text Safety

Before starting, read [Creative Governance](../../references/creative-governance.md), [Campaign Fact Handoff](../../references/campaign-fact-handoff.md), and [Visual Lock Brief](../../references/visual-lock-brief.md).

## Use When

- A visual needs headlines, CTA, fare, dates, logo, legal terms, captions, or subtitles
- A generated asset must contain no text, no subtitles, or no logo
- Reviewing generated text, typography hierarchy, safe zones, readability, or copy fidelity

## Required Inputs

- Exact approved copy or placeholders
- Language, channel, dimensions, safe zones, and accessibility/readability needs
- Approved font/logo references, if required
- Explicit no-text/no-subtitle/no-logo constraints

## Workflow

1. Separate approved copy from unverified commercial claims; hand unresolved claims to `vietjet-commercial-ops`.
2. Decide whether text should be generated or added manually. Default to manual insertion for final external assets.
3. Define hierarchy, safe zone, line count, contrast, mobile readability, and crop behavior.
4. For video, repeat no-text/no-subtitle/no-logo requirements in every relevant instruction and QA check.
5. Review exact-copy fidelity, diacritics, spelling, logo integrity, and disclaimer readability.

## Output

```text
TYPOGRAPHY AND TEXT SAFETY PLAN — [Asset] | CREATIVE DRAFT

APPROVED COPY / PLACEHOLDERS:
- ...

TEXT POLICY:
- MANUAL DESIGN INSERTION / GENERATED DRAFT / NO TEXT

LAYOUT AND SAFE ZONES:
- ...

VIDEO RULES:
- No text / no subtitle / no logo as applicable

QA CHECKS:
- Exact copy, spelling, diacritics, contrast, crop safety, logo integrity

COMMERCIAL CLAIMS FOR VIETJET-COMMERCIAL-OPS:
- ...
```

## Guardrails

- Flag when text should be added manually in design software.
- Do not invent or rewrite approved fares, offers, dates, routes, terms, or legal copy.
- Treat malformed text, altered logos, missing disclaimers, and violated no-text constraints as blocking issues.
