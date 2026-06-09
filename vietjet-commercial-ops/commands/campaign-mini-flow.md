---
description: Coordinate a governed mini campaign from commercial truth through creative handoff, QA, measurement, and human review.
argument-hint: [campaign brief, requested deliverables, and evidence references]
---

# Governed Campaign Mini Flow

## Arguments

The campaign brief, requested deliverables, and evidence references are in `$ARGUMENTS`.

## Workflow

1. Read `skills/campaign-factory/SKILL.md` and `references/operating-governance.md`.
2. Establish the commercial brief: objective, facts, claims, assumptions, missing data, audience
   hypotheses, message hierarchy, channels, and measurement outline.
3. Do not invent offers, fares, booking periods, inventory, market data, revenue, targets, or
   approvals.
4. Hand the governed brief to sibling plugin `vietjet-creative-factory` for requested creative
   prompts. Require its creative-governance rules, applicable locks, manual typography, and visual
   QA.
5. Return every route, date, fare, offer, eligibility, inventory, terms, or CTA claim appearing in
   creative work to `vietjet-commercial-ops` for verification.
6. Finish with a consolidated missing-data list and human review gates.

## Required Output

- Governed campaign strategy and message hierarchy
- Requested channel-copy drafts
- Creative handoff brief and requested prompt packages
- Visual QA and commercial-claim handoff
- Measurement outline
- Human approval needs

If `vietjet-creative-factory` is unavailable, complete the commercial brief and mark the creative
handoff blocked rather than improvising creative-plugin policy. End with the operating-governance
end-of-run block.
