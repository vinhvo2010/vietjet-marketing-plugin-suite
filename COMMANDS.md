# Vietjet Marketing Suite Commands

## Purpose

Commands are optional, repeatable entry points for pilot workflows that are either high-risk or
require coordination across multiple skills. They delegate to existing skills and references; they
do not add new capabilities, policy, approval authority, connectors, or publishing actions.

Use the commands when the runtime exposes repo-local plugin commands. Otherwise, use the equivalent
copy-paste prompts in [QUICK_START.md](QUICK_START.md).

## Pilot-Confirmed Commands

| Plugin | Command | Why It Exists |
|---|---|---|
| `vietjet-commercial-ops` | `promo-qa` | Standardizes a high-risk promotion review, including current-date and claim checks. |
| `vietjet-commercial-ops` | `route-launch` | Coordinates route facts, positioning, campaign planning, and governance. |
| `vietjet-commercial-ops` | `planning-scenario` | Provides a lightweight governed scenario before any full Revenue PMO workflow. |
| `vietjet-commercial-ops` | `campaign-mini-flow` | Coordinates commercial truth, creative handoff, measurement, and human review. |
| `vietjet-creative-factory` | `creative-kv` | Coordinates image prompting, applicable identity locks, text safety, and QA. |
| `vietjet-creative-factory` | `visual-qa` | Standardizes a blocking visual, IP, brand, and commercial-claim review. |

## Invocation

Select the command from the installed plugin command list, or ask the agent explicitly:

```text
Use the `route-launch` command from `vietjet-commercial-ops`.
Input: [paste the route brief and authorized evidence references]
```

```text
Use the `creative-kv` command from `vietjet-creative-factory`.
Input: [paste the governed campaign brief and approved visual references]
```

For `campaign-mini-flow`, both repo-local plugins must be available. Commercial facts and claims
remain controlled by `vietjet-commercial-ops`; creative prompts and visual QA remain controlled by
`vietjet-creative-factory`.

## Command Boundary

- Commands must read and apply the named skills and shared governance references.
- Commands must separate facts, assumptions, and missing data.
- Commands produce drafts and recommendations only.
- Commands must not approve, publish, activate, send, or execute.
- Commands must not invent fares, offers, route facts, inventory, market data, revenue, targets,
  approval thresholds, approvers, or approved identity details.
- Commands must hand unresolved commercial claims from creative work to
  `vietjet-commercial-ops`.

## Why Other Skills Do Not Have Commands Yet

Single-skill flows such as CRM push drafting, video prompting, carousel creation, brand rewrites,
and leadership briefs remain easy to invoke with direct prompts. Add another command only after
pilot usage shows a repeated routing problem, a recurring governance omission, or a meaningful
multi-skill sequence.
