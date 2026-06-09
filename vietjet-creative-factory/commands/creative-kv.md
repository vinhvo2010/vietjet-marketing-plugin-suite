---
description: Create a governed key-visual prompt with applicable identity locks, text safety, negative prompts, and visual QA.
argument-hint: [governed campaign brief, channel, ratio, and approved visual references]
---

# Governed Creative KV

## Arguments

The governed campaign brief, intended channel, aspect ratio, and approved visual references are in
`$ARGUMENTS`.

## Workflow

1. Read `skills/image-prompt-factory/SKILL.md`, `skills/visual-qa/SKILL.md`, and
   `references/creative-governance.md`.
2. Read only the identity-lock skills that apply to supplied approved references, such as
   `skills/aircraft-lock/SKILL.md`. Mark absent references `LOCK NOT VERIFIED`.
3. Separate factual campaign requirements from creative assumptions.
4. Hand unresolved route, date, fare, offer, inventory, eligibility, terms, and CTA claims to
   `vietjet-commercial-ops`.
5. Create the master prompt, negative prompt, format notes, safe zones, manual typography actions,
   and a visual QA checklist.
6. Do not generate or claim approval for a final asset.

## Required Output

- Factual campaign requirements and creative assumptions
- Master prompt and negative prompt
- Applied and unverified locks
- Format, composition, and manual design actions
- Visual QA checklist
- Commercial claims for `vietjet-commercial-ops`
- Human review needs

End with the creative-governance end-of-run block. The result is a creative draft requiring human
review.
