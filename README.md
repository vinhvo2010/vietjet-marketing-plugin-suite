# Vietjet AI Plugin Suite

## Beta: 18 specialist roles / 24 skills (v5.0.4)

[Vietjet AI Marketing Suite](plugins/vietjet-ai-marketing-suite/README.md) is available through the `vietjet-team` Git marketplace for Codex users. The 18 roles are skill-based specialists, not autonomous agents. Human review remains mandatory before publication, spending, fare changes, personal-data use, or safety-related communications. This beta is **not** an OpenAI Plugins Directory listing, and its development App/MCP attachment may not be available to other accounts.

Install once:

```bash
codex plugin marketplace add vinhvo2010/vietjet-marketing-plugin-suite
codex plugin add vietjet-ai-marketing-suite@vietjet-team
```

For later plugin updates, refresh the marketplace and start a new Codex task:

```bash
codex plugin marketplace upgrade vietjet-team
```

Use `$vietjet-ai-marketing-suite:vietjet-marketing-squad` or `/vietjet-ai-marketing-suite:vietjet-marketing-squad` in a new task. See the [Vietnamese team guide](TEAM_PLUGIN_RELEASE_2026-09-23.md) for caveats and testing steps.

## Suite Purpose

This repository contains a repo-local Codex plugin suite for governed Vietjet commercial and creative workflows. The suite helps internal teams move from verified commercial inputs to controlled creative production while preserving clear data boundaries, governance checks, and human approval gates.

## Included Plugins

### [`vietjet-commercial-ops`](vietjet-commercial-ops/README.md)

Controls commercial truth, route facts, promo governance, CRM and revenue measurement, and executive reporting.

Use it for:

- Route launch briefs
- Campaign planning
- Promo QA
- CRM personalization
- Revenue governance
- Revenue PMO
- Executive reporting
- Brand voice and commercial copy governance

### [`vietjet-creative-factory`](vietjet-creative-factory/README.md)

Controls AI creative production, prompt generation, visual QA, and identity locks.

Use it for:

- Image prompts
- Video prompts
- Carousel concepts
- Visual QA
- Aircraft identity locks
- Mascot identity locks
- Face identity locks
- Typography and text-safety rules

## How The Plugins Work Together

Standard flow:

`Commercial truth → Creative execution → Visual QA → Commercial handoff if claims/offers appear → Human approval`

Example:

1. Use `vietjet-commercial-ops` to verify HAN ⇄ PRG route facts and the campaign message.
2. Use `vietjet-creative-factory` to generate 4:5 key-visual and 9:16 video prompts.
3. Use `vietjet-commercial-ops` again if the creative contains fares, dates, claims, or offer wording.
4. Require human review before publishing or external use.

## Non-Negotiable Governance Rules

- Do not invent fares.
- Do not invent booking periods.
- Do not invent route performance.
- Do not invent market data.
- Do not invent approval thresholds.
- Do not publish without human review.
- Do not use public-figure implication, impersonation framing, or voice cloning.
- Do not rely on AI-generated image text for mission-critical typography.

## Recommended Pilot Cases

- HAN ⇄ PRG route launch
- SALE66 post-campaign recap
- Deluxe upsell CRM sequence
- Vietjet A330-300 campaign KV
- Chào Châu Âu cùng Vietjet carousel
- 8-second no-text summer travel video prompt

## Suite Documentation

- [Optional Pilot Commands](COMMANDS.md) — six thin, repeatable entry points added only for
  pilot-confirmed high-risk or multi-skill workflows.
- [Codex Installation And Usage](CODEX_INSTALLATION.md) — open the workspace, reference plugins and
  skills, run governed tasks, and troubleshoot context.
- [Quick Start](QUICK_START.md) — six copy-paste governed pilot prompts.
- [Customization Guide](CUSTOMIZATION_GUIDE.md) — safely evolve skills, references, facts, locks,
  and governance boundaries.
- [Source-Alignment Audit](SOURCE_ALIGNMENT_AUDIT.md) — comparison with Anthropic's
  `knowledge-work-plugins` architecture and conventions.

## Repository Structure

```text
Vietjet-marketing/
├── CODEX_INSTALLATION.md
├── COMMANDS.md
├── CUSTOMIZATION_GUIDE.md
├── QUICK_START.md
├── README.md
├── SOURCE_ALIGNMENT_AUDIT.md
├── vietjet-commercial-ops/
│   └── commands/
└── vietjet-creative-factory/
    └── commands/
```

## Version Status

- `vietjet-commercial-ops`: v0.1.0 pilot-ready; v0.1.1 governance refinements unreleased
- `vietjet-creative-factory`: v0.1.0 pilot-ready

## Commit And Tag Guidance

Review all changes and validator results before committing or tagging. Suggested commands:

```bash
git add README.md vietjet-commercial-ops vietjet-creative-factory
git commit -m "release: prepare Vietjet AI Plugin Suite pilot"

git tag -a vietjet-commercial-ops-v0.1.0 -m "vietjet-commercial-ops v0.1.0"
git tag -a vietjet-creative-factory-v0.1.0 -m "vietjet-creative-factory v0.1.0"

git push origin HEAD
git push origin vietjet-commercial-ops-v0.1.0 vietjet-creative-factory-v0.1.0
```

Do not create a `vietjet-commercial-ops-v0.1.1` tag until its unreleased governance refinements have completed review and release approval.
