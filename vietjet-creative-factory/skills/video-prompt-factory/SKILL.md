---
name: video-prompt-factory
description: Create governed video-generation prompts and shot plans for Vietjet campaign films, social video, motion assets, and visual sequences, including strict no-text, no-subtitle, no-logo, identity-lock, and continuity constraints.
---

# Video Prompt Factory

Before starting, read [Creative Governance](../../references/creative-governance.md), [Campaign Fact Handoff](../../references/campaign-fact-handoff.md), and [Prompt and QA Template](../../references/prompt-and-qa-template.md).

## Use When

- Creating a video-generation prompt, storyboard, shot list, or motion adaptation
- Producing no-text footage for later editing
- Maintaining aircraft, mascot, face, wardrobe, environment, or color continuity across shots

## Required Inputs

- Objective, duration, aspect ratio, platform, audience, and desired narrative
- Supplied campaign facts and approved references
- Applicable identity/visual locks
- Explicit rules for text, subtitles, captions, logos, and audio

## Workflow

1. Separate factual campaign requirements from creative assumptions.
2. Define the visual story, shot sequence, camera movement, subject action, lighting, and transitions.
3. Define continuity anchors that repeat in every shot.
4. When requested, repeat `NO TEXT`, `NO SUBTITLES`, and `NO LOGOS` in the master direction, each shot, negative prompt, and QA checklist.
5. Hand off unverified commercial claims to `vietjet-commercial-ops`; do not place them in generated footage.
6. Specify manual edit actions for titles, supers, logos, CTA, fares, dates, and legal lines.

## Output

```text
VIDEO PROMPT PACKAGE — [Asset] | CREATIVE DRAFT

FACTUAL CAMPAIGN REQUIREMENTS:
- ...

CREATIVE ASSUMPTIONS:
- ...

GLOBAL DIRECTION:
- Duration / aspect ratio / style
- Text-subtitle-logo policy
- Continuity anchors

SHOT PLAN:
Shot | Duration | Visual action | Camera | Locks | Prohibitions

NEGATIVE PROMPT:
- ...

MANUAL EDIT ACTIONS:
- ...
```

## Guardrails

- Never add text, subtitles, captions, or logos when prohibited.
- Do not invent aircraft movement, airport operations, routes, schedules, or offers as factual claims.
- Flag continuity, physics, anatomy, livery, face, and logo risks for visual QA.
