# Implementation Plan Review

## Verdict

The researched plan is a strong domain blueprint, but it was not directly implementable as a Codex plugin. The eight workflow drafts are useful and have clear approval guardrails. The main gaps were packaging, connector behavior, and an internal governance contradiction.

## Findings

### High: Approval policy was presented as both fixed and unknown

The plan and several skills named specific approval chains and a `>5% revenue impact` CCO threshold, while `revenue-governance` also instructed the agent not to assume current policy. An AI-generated threshold could be mistaken for an approved Vietjet policy.

Resolution: all role names and thresholds are now treated as proposed defaults until an approved authority matrix is supplied. The shared operating-governance reference prohibits inventing policy.

### Medium: Drafts were not installable plugin skills

The source used flat `skills/*.md` files and had no `.codex-plugin/plugin.json`. Codex expects each skill at `skills/<skill-name>/SKILL.md`.

Resolution: created the plugin manifest and converted all eight workflows to the required directory structure.

### Medium: Connector instructions lacked runtime fallback rules

The plan assumed Google Drive, Docs, Sheets, Gmail, Calendar, Slack, and Teams would be connected. A skill could otherwise imply it had read a source it could not access.

Resolution: shared governance now requires availability checks, successful tool calls before source claims, and pasted/local input fallback.

### Medium: Governance was duplicated across skills

Human approval, data boundaries, and draft labeling were repeated with slightly different wording, increasing the risk of drift.

Resolution: added `references/operating-governance.md` as the shared baseline. Skill-specific controls remain in each workflow.

## Recommended Deployment Sequence

1. Validate and pilot `brand-voice` and `promo-qa` using pasted, non-sensitive inputs.
2. Confirm the approved authority matrix, business-unit boundaries, and audit-log owner.
3. Pilot `executive-reporter` and `revenue-governance` with authorized local or connected files.
4. Pilot `revenue-pmo` and `route-marketing` after baseline data sources are confirmed.
5. Enable `campaign-factory` and `crm-personalization` only after revenue, legal, privacy, and connector scopes are approved.

## Acceptance Criteria

- Plugin validator passes.
- Every skill is discoverable from its description.
- No skill claims connector access without a successful tool call.
- No skill invents approval policy, targets, revenue values, or source facts.
- Outputs clearly distinguish facts, estimates, hypotheses, and missing data.
- All external or operational actions remain behind human approval.
