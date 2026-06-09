# Codex Installation And Usage

## Purpose

This guide explains how to use the repo-local Vietjet AI Plugin Suite in Codex or Antigravity for
the current controlled MVP. The suite is Codex-local and does not require external connectors.

## Prerequisites

- Access to Codex or Antigravity with permission to open a local workspace
- Read access to this repository
- Write access only when the requested task requires file changes
- A human owner who can review any output intended for operational or external use
- Authorized source facts or local files for claims that must be verified

No Python dependencies, external connectors, Claude manifests, or slash commands are required for
the current MVP.

## Workspace Location

Open this folder as the workspace root:

```text
<REPO_ROOT>
```

The repo-local plugins are:

```text
<REPO_ROOT>/vietjet-commercial-ops
<REPO_ROOT>/vietjet-creative-factory
```

## Open The Repo In Codex Or Antigravity

1. Start Codex or Antigravity.
2. Choose the option to open a folder or workspace.
3. Open `<REPO_ROOT>`.
4. Start a new task from the repository root.
5. Name the plugin and skill you want used in the prompt when deterministic routing matters.

Opening the repository root gives the agent access to both plugin packages and their shared suite
documentation.

## Reference A Repo-Local Plugin

Use the plugin name and local path explicitly:

```text
Use the repo-local `vietjet-commercial-ops` plugin at
`<REPO_ROOT>/vietjet-commercial-ops`.
```

```text
Use the repo-local `vietjet-creative-factory` plugin at
`<REPO_ROOT>/vietjet-creative-factory`.
```

For cross-plugin work, state the order and boundary:

```text
Use `vietjet-commercial-ops` to establish commercial truth, then use
`vietjet-creative-factory` for creative execution. Return unresolved claims to
`vietjet-commercial-ops` before human approval.
```

## Ask The Agent To Use A Specific Skill

Name the plugin, skill, source inputs, and required governance behavior:

```text
Use the `promo-qa` skill from `vietjet-commercial-ops`.
Review the supplied SALE66 recap. Separate facts, assumptions, and missing data.
Apply operating governance and do not invent inventory, revenue, or approvals.
```

```text
Use the `aircraft-lock` skill from `vietjet-creative-factory`.
Build an A330-300 lock using only the supplied approved references.
Mark unsupported details as not verifiable.
```

## Run A Task With Governance

Use this prompt pattern:

```text
Use [plugin] and its [skill] skill.

Objective:
[Describe the requested output.]

Source facts:
[List supplied facts and authorized file references.]

Required governance:
- Separate facts, assumptions, and missing data.
- Do not invent fares, dates, market data, revenue, inventory, route performance,
  approval thresholds, or approvers.
- Apply the plugin's shared governance references.
- Flag required evidence and human approval.
- Treat the output as a draft until human review.
```

For commercial work, follow
[`vietjet-commercial-ops/PILOT_RUNBOOK.md`](vietjet-commercial-ops/PILOT_RUNBOOK.md). For creative
work, follow
[`vietjet-creative-factory/PILOT_RUNBOOK.md`](vietjet-creative-factory/PILOT_RUNBOOK.md).

## Troubleshooting Plugin Context

If the agent ignores or incompletely applies plugin context:

1. Confirm the workspace root is `<REPO_ROOT>`.
2. Name the required plugin and skill explicitly.
3. Include the full plugin path in the request.
4. Ask the agent to read the plugin README, the selected `SKILL.md`, and its linked governance
   references before drafting.
5. Restate the required facts, missing data, assumptions, and human approval boundary.
6. Ask the agent to report which skill and governance references it applied.
7. Start a fresh task after reopening the workspace if context from an earlier task is interfering.

Do not work around missing plugin context by allowing unsupported claims or skipping human review.

## Connector Policy

No external connector is required for the current MVP. Use pasted inputs and authorized local files.
If required evidence is unavailable, mark it as missing rather than inventing it. Do not claim that
a source, connector, or system was checked unless it was actually accessed successfully.
