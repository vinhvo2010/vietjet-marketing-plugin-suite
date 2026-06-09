# Vietjet AI Plugin Suite Source-Alignment Audit

**Audit date:** June 8, 2026  
**Source baseline:** [Anthropic knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)  
**Local scope:** root README, `vietjet-commercial-ops`, and `vietjet-creative-factory`  
**Audit constraint:** report only; no plugin source files changed

## Summary

The Vietjet AI Plugin Suite is strongly aligned with the architectural intent of Anthropic's
`knowledge-work-plugins` repository: one repository contains multiple self-contained,
role/workflow-oriented plugins; each plugin packages reusable skills and documentation; and the
content is customized for company terminology, processes, and risks.

The suite intentionally diverges at the runtime-packaging layer. It is currently a repo-local
Codex suite using `.codex-plugin/plugin.json`, with no Claude manifests, root Claude marketplace
manifest, or bundled MCP configuration. After pilot usage confirmed repeated orchestration needs,
the suite added a limited command set that delegates to existing skills. It is not currently
installable as a Claude Code/Cowork plugin suite without additional packaging.

The local skills are more governed and operationally specific than the generic Anthropic marketing
baseline. All 16 skills have YAML frontmatter, focused descriptions, required inputs, workflows,
output contracts, and shared-governance references. They encode airline-specific SOPs rather than
acting as generic prompts.

**Alignment score: 87/100**

This score measures architectural and convention alignment with the source model, not cross-runtime
installability. Claude Code/Cowork compatibility is lower because Claude-specific manifests and
marketplace packaging are absent.

## Audit Basis

The audit compared the local suite with these source patterns:

- The source repository describes plugins as role/team/company specialists that bundle skills,
  connectors, slash commands, and optional sub-agents.
- The source repository contains multiple job-function plugins in one marketplace repository.
- Its common plugin layout uses `.claude-plugin/plugin.json`, `.mcp.json`, `commands/`, and
  `skills/`.
- Its marketing plugin exposes explicit commands and automatically relevant domain skills.
- Anthropic's broader Claude plugin standard treats commands, agents, skills, and `.mcp.json` as
  optional plugin components; the Claude manifest is required for Claude plugin installation.

Primary source references:

- [Knowledge Work Plugins README](https://github.com/anthropics/knowledge-work-plugins)
- [Knowledge Work Plugins marketplace manifest](https://github.com/anthropics/knowledge-work-plugins/blob/main/.claude-plugin/marketplace.json)
- [Marketing plugin manifest](https://github.com/anthropics/knowledge-work-plugins/blob/main/marketing/.claude-plugin/plugin.json)
- [Marketing plugin README](https://github.com/anthropics/knowledge-work-plugins/blob/main/marketing/README.md)
- [Marketing campaign-plan command](https://github.com/anthropics/knowledge-work-plugins/blob/main/marketing/commands/campaign-plan.md)
- [Marketing campaign-planning skill](https://github.com/anthropics/knowledge-work-plugins/blob/main/marketing/skills/campaign-planning/SKILL.md)
- [Anthropic Claude plugin structure](https://github.com/anthropics/claude-plugins-official)

## 1. Repository-Level Pattern

### Finding

The root suite follows the source repository model well:

- One repository contains multiple specialized plugins.
- `vietjet-commercial-ops` and `vietjet-creative-factory` have distinct ownership boundaries.
- Each plugin is self-contained and has its own README, manifest, skills, references, tests, release
  checklist, pilot runbook, and changelog.
- The plugins are customized for Vietjet terminology, airline commercial processes, creative locks,
  and human approval workflows.
- The root README explains how the plugins work together.

### Alignment

**Aligned.** The local suite is narrower and more company-specific than Anthropic's general
job-function marketplace, which is appropriate for an internal suite.

### Recommendation

Keep the two-plugin repository model. Do not split the plugins into separate repositories unless
ownership, access control, or release cadence becomes materially different.

## 2. Plugin Manifest Comparison

### Anthropic Pattern

- Claude package manifest: `.claude-plugin/plugin.json`
- Marketplace repository manifest: root `.claude-plugin/marketplace.json`
- Source plugin manifests are intentionally small and commonly contain `name`, `version`,
  `description`, and `author`.

### Vietjet Pattern

- Codex package manifest: `.codex-plugin/plugin.json`
- Both manifests include Codex-specific discovery and interface metadata.
- There is no root Claude marketplace manifest.

### Finding

This is intentionally Codex-local and valid for the current runtime. It is a packaging divergence,
not a skill-content defect.

For Claude Code/Cowork compatibility, each plugin would need a separately validated
`.claude-plugin/plugin.json`. A Claude marketplace installation would also need a root
`.claude-plugin/marketplace.json` that registers both plugin folders.

Do not blindly copy the Codex manifest into the Claude location. Build a Claude-specific minimal
manifest and validate its schema because Codex-only fields may not be accepted or used by Claude.

### Recommendation

Keep Codex-only packaging during the controlled internal pilot. Add Claude mirror packaging only
after Claude Code/Cowork becomes an approved runtime target.

## 3. Skills Structure Comparison

### Inventory

| Plugin | Skills | Shared references |
|---|---:|---:|
| `vietjet-commercial-ops` | 8 | 6 |
| `vietjet-creative-factory` | 8 | 4 |

### Findings

- Every skill uses `skills/<skill-name>/SKILL.md`.
- Every skill has clear `name` and `description` frontmatter.
- Descriptions are specific enough to support automatic triggering.
- Skills contain domain expertise, SOPs, workflows, checks, required inputs, and output structures.
- Skills are not generic prompt wrappers.
- Every commercial skill links to shared operating governance.
- Every creative skill links to shared creative governance and relevant lock/handoff references.
- Progressive disclosure exists: common rules live in shared references and skill files link to them.
- Creative skills use progressive disclosure especially well.
- Commercial skills remain reasonably sized but contain more embedded domain guidance; this is
  acceptable and does not currently require refactoring.

### Alignment

**Aligned.** The local skills are at least as operationally useful as the source pattern and are
more specific about data boundaries and approval gates.

### Recommendation

No skill changes are required. If skills grow materially, move detailed tables or policy material
into linked references while retaining the trigger, workflow, and output contract in `SKILL.md`.

## 4. Commands Comparison

### Finding

The Anthropic knowledge-work plugins commonly include `commands/` so users can invoke repeatable
workflows explicitly. The Vietjet plugins remain skill-first, but now include six thin commands for
pilot-confirmed high-risk or multi-skill workflows.

Commands are not required for the current Codex runtime or for the skills to trigger. Commands are
also optional in the broader Claude plugin standard. The current commands improve repeatability
without duplicating skill policy.

### Current Command Set

| Plugin | Commands |
|---|---|
| `vietjet-commercial-ops` | `promo-qa`, `route-launch`, `planning-scenario`, `campaign-mini-flow` |
| `vietjet-creative-factory` | `creative-kv`, `visual-qa` |

Each command is a thin explicit workflow entry point that delegates to existing skills and
governance. Add more only after pilot evidence confirms a repeated need.

## 5. MCP / Connector Comparison

### Finding

The Anthropic repository commonly uses `.mcp.json` and connector documentation to connect job
functions to company tools. The Vietjet suite is connector-light and explicitly degrades to pasted
or authorized local inputs.

Connector-light is acceptable and safer for an MVP because:

- The pilot focuses on governed drafting and QA rather than live execution.
- Missing evidence is explicitly marked instead of silently invented.
- No connector can accidentally publish, activate, approve, or expose sensitive data.

### Optional Future Connectors

| Connector category | Potential use | Required control |
|---|---|---|
| Figma / Canva | Creative references, design handoff, visual QA context | Read/draft scope; no unauthorized publishing |
| Google Drive / Notion | Approved briefs, governance, brand references | Source traceability and access control |
| Slack | Workflow handoff and review requests | Human confirmation before sending |
| Analytics / CRM tools | Aggregate campaign and CRM measurement | Aggregate/anonymized access; no PII or activation |

### Recommendation

Do not add connectors until there is an approved data-access model, owner, and connector-specific
test plan. An empty `.mcp.json` is not needed for Codex-only use.

## 6. Documentation Comparison

### Stronger Than Source Baseline

The suite includes documentation not normally present in each source plugin:

- `SKILL_INDEX.md`
- `TEST_PROMPTS.md`
- `RELEASE_CHECKLIST.md`
- `PILOT_RUNBOOK.md`
- `ACCEPTANCE_TEST_REPORT.md`
- `CHANGELOG.md`
- Commercial pilot report and implementation review

This gives the suite unusually strong release evidence and operational guidance.

### Documentation Gaps

| Documentation area | Status | Gap |
|---|---|---|
| Purpose | Present | None |
| Target personas | Present across README/runbooks | Creative README does not surface personas directly |
| Available skills | Present | None |
| Examples | Present | None |
| Installation instructions | Present | Repo-local Codex usage and optional command fallback documented |
| Quick start | Present | Copy-paste governed first-run examples available |
| Commands and command examples | Present | Six pilot-confirmed thin commands plus suite command guide |
| Connector setup | Partial | Fallback rules exist; no setup instructions because connectors are not bundled |
| Customization notes | Present | Safe skill, reference, governance, lock, and command evolution documented |

### Recommendation

Keep commands limited to pilot-confirmed repeated workflows. Add connector setup only when
connectors are actually introduced.

## 7. Governance Comparison

### Finding

The Anthropic plugins provide role-based productivity workflows and include practical safeguards.
The Vietjet suite intentionally adds stricter airline commercial, measurement, identity, and
approval governance.

Intentionally stronger controls include:

- Explicit data-boundary rules and unsupported-data blocking
- Evidence-and-approval intake
- Audit-log schema and deterministic output IDs
- Post-campaign and CRM measurement worksheets
- Separation of gross revenue from incremental revenue
- No public-figure implication, impersonation framing, or voice cloning
- Commercial-claim handoff from creative production to commercial governance
- Booking-period and promo-date verification/blocking
- `0Đ`, free, universal-claim, inventory, eligibility, fee, and cross-channel parity controls
- Aircraft, mascot, face, typography, and no-text/no-subtitle/no-logo locks
- Mandatory human review before external use

### Alignment

**Divergent by design, positively.** These additions preserve the source model's company
customization principle while making the suite suitable for a higher-risk airline context.

### Recommendation

Retain all current governance additions. They are a differentiating safety layer, not unnecessary
scope expansion.

## 8. Compatibility Matrix

| Area | Anthropic repo pattern | Vietjet implementation | Alignment status | Recommendation | Priority |
|---|---|---|---|---|---|
| Repository model | One marketplace repo with multiple role plugins | One repo with two governed Vietjet workflow plugins | Aligned | Keep current structure | P2 |
| Plugin self-containment | Plugin owns manifest, README, skills, commands/connectors as needed | Each plugin owns manifest, README, skills, references, tests, and runbook | Aligned | Keep ownership boundaries | P2 |
| Runtime manifest | `.claude-plugin/plugin.json` | `.codex-plugin/plugin.json` | Divergent by design | Keep Codex-only now; add validated Claude mirror only for approved target | P0 only for Claude target |
| Marketplace registration | Root `.claude-plugin/marketplace.json` | None | Gap for Claude marketplace only | Add only with Claude marketplace packaging | P0 only for Claude target |
| Skill layout | `skills/<name>/SKILL.md` | Same | Aligned | No change | P2 |
| Skill quality | Domain expertise, best practices, workflows | Airline/creative SOPs, checks, outputs, governance | Aligned | No change | P2 |
| Progressive disclosure | Skill core plus supporting resources as needed | Shared references linked from skills | Aligned | Preserve; move detail only when files grow | P2 |
| Slash commands | Common explicit workflow entry points | No commands; skill-first | Divergent by design | Add thin commands only for Claude/discoverability need | P1 |
| MCP connectors | Common tool connections through `.mcp.json` | Connector-light with documented fallback | Divergent by design | Keep for MVP; add only with access governance | P1 |
| Plugin README | Installation, commands, skills, examples, configuration/connectors | Strong purpose, skills, examples, governance, limitations; no installation/quick start | Gap | Add Codex install, quick start, customization notes | P1 |
| Company customization | Adapt tools, terminology, and processes | Deep Vietjet airline and creative customization | Aligned | Keep | P2 |
| Governance | General role/workflow safeguards | Strong airline evidence, approval, measurement, and identity controls | Divergent by design | Retain stronger controls | P2 |
| Testing/release evidence | Not consistently packaged per plugin | Acceptance reports, test prompts, checklists, runbooks, changelogs | Divergent by design | Retain | P2 |

## 9. If We Want This Suite To Be Claude Code/Cowork Compatible

Use a controlled mirror-packaging approach:

1. Add a separately validated `.claude-plugin/plugin.json` alongside each
   `.codex-plugin/plugin.json`.
2. Add a root `.claude-plugin/marketplace.json` if the two plugins will be installed from this
   repository as a Claude marketplace.
3. Add `commands/` with thin slash-command Markdown files mapped to the existing skills.
4. Add `.mcp.json` only for approved optional servers. Prefer documented optional connectors over an
   empty placeholder file.
5. Keep existing skills and references unchanged wherever possible.
6. Update README installation notes to distinguish Codex-local use from Claude Code/Cowork use.
7. Validate both packaging formats independently and test that shared relative reference links work
   in both runtimes.

This migration should add packaging and discoverability, not new business capabilities.

## 10. Final Recommendation

### Decision: A. Keep Codex-only for now

This is the safest next step for an internal Vietjet pilot.

Reasons:

- The current suite is already well aligned with the source architecture and company-customization
  model.
- The stricter governance layer is appropriate and should remain stable during pilot learning.
- Claude mirror packaging, commands, and connectors would increase test surface without improving
  the current Codex pilot's core governed outputs.
- Cross-runtime packaging should be undertaken only when there is an approved Claude Code/Cowork
  use case, owner, installation path, and connector/data-access model.

Do not split the repository or convert fully to the Anthropic marketplace style at this stage.

## Prioritized Actions

### P0 Gaps

- **Current Codex-only target:** None identified.
- **If Claude Code/Cowork becomes a required target:** Claude manifests and root marketplace
  registration become P0 compatibility blockers.

### P1 Improvements

- Add Codex-local installation instructions and a concise quick start.
- Add safe customization notes for company terminology, references, processes, and governance.
- Decide whether explicit commands are valuable after the controlled pilot.
- Define connector ownership, access scope, data boundaries, and testing before adding MCP servers.

### Recommended Next Action

Complete the controlled Codex pilot with the existing packages. After pilot feedback, make a
documented runtime decision: remain Codex-only or open a packaging-only Claude compatibility work
item. Do not modify skills or add connectors before that decision.

## Validation Note

Read-only Codex plugin and skill validator runs were attempted during this audit. They could not
start because the local Python environment does not provide the `yaml` module
(`ModuleNotFoundError: No module named 'yaml'`). No dependencies were installed and no plugin files
were changed. This environment issue is not evidence of a plugin compatibility defect.
