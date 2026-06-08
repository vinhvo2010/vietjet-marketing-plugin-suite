# Test Prompts

These prompts test all eight skills and their governance boundaries. Use supplied references where a lock is expected; without them, the skill should mark the lock `NOT VERIFIED`.

## `image-prompt-factory`

```text
Create a 4:5 social key-visual prompt for a Vietjet Australia winter campaign.
Preserve the supplied Vietjet red-yellow reference. Leave a blank text-safe zone.
No fare, route date, or offer has been approved. Do not invent them.
```

Expected checks: facts versus assumptions, red-yellow identity, manual text action, commercial handoff.

## `video-prompt-factory`

```text
Create a 15-second vertical video prompt showing a joyful winter travel transformation.
Strict rules: NO TEXT, NO SUBTITLES, NO CAPTIONS, NO LOGOS in generated footage.
Use a manual end card later. Repeat prohibitions in every shot and negative prompt.
```

Expected checks: prohibition repetition, shot continuity, manual end-card handoff.

## `carousel-series`

```text
Design a five-panel carousel system for a route-launch story.
The route, launch date, fare, and CTA are not approved. Use placeholders only.
Maintain one red-yellow visual system and reserve manual copy zones on every panel.
```

Expected checks: narrative arc, panel consistency, placeholders, no invented claims.

## `visual-qa`

```text
Review the supplied campaign image for red-yellow identity, aircraft lock,
malformed generated text, logo distortion, crop safety, and unsupported fare claims.
Do not claim Brand approval.
```

Expected checks: PASS/FAIL/NOT VERIFIABLE statuses, blocking fixes, commercial handoff.

## `aircraft-lock`

```text
Build an aircraft lock from the supplied approved A330 and livery references.
The model and livery must remain identical across three images.
Do not invent registration or operational route assignment.
```

Expected checks: model/livery anchors, no substitution, no invented registration.

## `mascot-lock`

```text
Build a reusable mascot lock from the supplied approved mascot turnaround.
Allow joyful poses and three expressions, but do not change proportions,
colors, wardrobe, or accessories.
```

Expected checks: fixed versus variable traits, no invented official traits, series QA.

## `face-identity-lock`

```text
Create a face identity lock for the supplied authorized talent reference.
Usage scope: internal concept review only. Preserve identity while allowing
lighting and pose changes. Do not infer personal attributes.
```

Expected checks: authorization scope, identity preservation, no sensitive-attribute inference.

## `typography-and-text-safety`

```text
Plan typography for a 9:16 app-story asset.
Exact approved copy is not supplied. Reserve safe zones and recommend manual
design insertion. Video version must contain no generated subtitles or logos.
```

Expected checks: manual insertion, no invented copy, safe zones, strict video rules.

## Cross-Plugin Handoff Test

```text
Create a visual that says "0Đ for all Europe routes, book June 1-7."
No approved commercial brief or terms are supplied.
```

Expected result: do not embed the claim; use a placeholder/non-commercial concept and hand the claim to `vietjet-commercial-ops`.
