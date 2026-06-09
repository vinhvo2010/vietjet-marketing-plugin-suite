# Vietjet Creative Factory

Repo-local Codex plugin for governed Vietjet AI creative production workflows.

**Version:** `v0.1.0`  
**Status:** Ready for controlled internal pilot  
**Operating model:** Codex creates prompts, specifications, and QA drafts. Authorized humans approve campaign facts, Brand usage, Legal requirements, and final assets.

## Purpose

Support campaign visuals, video prompts, carousel series, aircraft visuals, mascot visuals, authorized face identity locks, typography/text safety, and visual QA while preserving supplied Vietjet identity and commercial facts.

## Plugin Suite Positioning

- `vietjet-commercial-ops` controls commercial truth and governance: routes, dates, fares, offers, inventory, eligibility, terms, commercial claims, and approval requirements.
- `vietjet-creative-factory` controls creative prompt and visual production: creative direction, prompts, visual systems, identity locks, text safety, and visual QA.

Creative work may continue with placeholders or non-commercial concepts, but unresolved commercial facts must be handed to `vietjet-commercial-ops`.

## Available Skills

| Skill | Use |
|---|---|
| `image-prompt-factory` | Create governed prompts for campaign images, key visuals, and adaptations |
| `video-prompt-factory` | Create shot plans and video prompts with continuity and strict prohibition rules |
| `carousel-series` | Build consistent multi-panel creative systems |
| `visual-qa` | Review assets and prompts for lock, fact, text, artifact, and channel compliance |
| `aircraft-lock` | Preserve supplied aircraft model and livery constraints |
| `mascot-lock` | Preserve an approved mascot identity across assets |
| `face-identity-lock` | Preserve an authorized face identity within confirmed consent scope |
| `typography-and-text-safety` | Plan safe manual typography, exact copy, text-free footage, logos, and subtitles |

See [SKILL_INDEX.md](SKILL_INDEX.md) for required inputs, outputs, controlled risks, and commercial-handoff rules.

## Optional Pilot Commands

| Command | Coordinated workflow |
|---|---|
| `creative-kv` | Image prompt, applicable identity locks, text safety, and visual QA |
| `visual-qa` | Blocking brand, IP, text, artifact, lock, and commercial-claim review |

Commands are thin entry points into existing skills and governance. They do not create approval,
publish assets, or add creative capabilities.

## Example Prompts

```text
Create a premium 4:5 Facebook KV prompt for Hà Nội ⇄ Praha.
Use the supplied red-yellow reference, reserve a manual text-safe zone,
and do not invent fares or offers.
```

```text
Create an 8-second 9:16 summer-travel video prompt.
Strict rules: no text, no subtitles, no captions, and no logo overlay.
```

```text
Build an A330-300 aircraft lock from the supplied model and livery references.
Block model substitution, wrong livery, invented registration, and misspelled logos.
```

```text
Review this generated visual for factual claims, red-yellow identity,
lock compliance, malformed text, and commercial-handoff requirements.
```

More prompts are available in [TEST_PROMPTS.md](TEST_PROMPTS.md).

## Governance

Every skill applies [Creative Governance](references/creative-governance.md).

- Separate factual campaign requirements from creative assumptions.
- Do not invent campaign facts, routes, dates, fares, offers, inventory, eligibility, or approved claims.
- Preserve supplied Vietjet red-yellow identity and approved reference assets.
- Flag when text, logo, fare, date, CTA, or legal lines should be added manually in design software.
- Enforce requested no-text, no-subtitle, and no-logo rules.
- Enforce supplied aircraft model, livery, mascot, face, typography, and text locks.
- Do not claim Brand, Legal, Commercial, or operational approval.
- Hand unresolved commercial claims to `vietjet-commercial-ops`.

## Shared References

- [Creative Governance](references/creative-governance.md)
- [Campaign Fact Handoff](references/campaign-fact-handoff.md)
- [Visual Lock Brief](references/visual-lock-brief.md)
- [Prompt and QA Template](references/prompt-and-qa-template.md)

## Typical Workflow

```text
Creative brief
  → campaign-fact separation
  → applicable identity locks
  → prompt / series / shot plan
  → visual QA
  → manual design handoff
  → human Brand / Commercial / Legal review
```

## Commercial Handoff

Use `vietjet-commercial-ops` when a creative request requires validation or approval of:

- Route, flight, schedule, or launch facts
- Fare, offer, booking/travel dates, inventory, eligibility, or terms
- Commercial claims, compliance review, or approval workflow

This plugin may use approved commercial facts supplied by the user. It must not approve or invent them.

## Commercial Handoff Rules

- Hand off unresolved route, flight, schedule, launch, fare, offer, inventory, eligibility, CTA, terms, and compliance claims to `vietjet-commercial-ops`.
- Use placeholders or omit unresolved claims while creative development continues.
- Do not treat a commercial handoff request as approval.
- Re-run visual QA after approved commercial copy is inserted.

## Known Limitations

- No approved Vietjet brand assets, exact palettes, fonts, aircraft livery files, mascot references, face references, or campaign facts are bundled.
- Prompt compliance does not guarantee model output compliance; visual QA and human review remain required.
- Generated text and logos may be malformed; final external typography and logos should normally be added manually.
- This plugin does not replace Brand, Legal, Commercial, operational, or talent/consent approval.

## Testing

Use [TEST_PROMPTS.md](TEST_PROMPTS.md) for internal forward tests, [ACCEPTANCE_TEST_REPORT.md](ACCEPTANCE_TEST_REPORT.md) for the validated 8/8 acceptance result, [PILOT_RUNBOOK.md](PILOT_RUNBOOK.md) for controlled usage, and [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md) for package readiness.
