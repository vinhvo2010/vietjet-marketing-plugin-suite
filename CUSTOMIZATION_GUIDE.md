# Customization Guide

## Purpose

This guide explains how to customize the Vietjet AI Plugin Suite without weakening its ownership
boundaries, factual controls, or human approval model. Customize only when a validated workflow need
cannot be handled by existing skills or references.

## Decide Where A Change Belongs

Use `vietjet-commercial-ops` when the change controls commercial truth or decisions:

- Routes, schedules, launch facts, fares, offers, eligibility, inventory, or terms
- Campaign planning, promo QA, CRM measurement, revenue governance, or executive reporting
- Commercial copy claims, evidence, approvals, or audit requirements

Use `vietjet-creative-factory` when the change controls creative production:

- Image, video, or carousel prompt structure
- Visual QA and creative handoff
- Aircraft, mascot, face, typography, logo, or no-text locks
- Creative assumptions and production constraints

When a creative rule contains a commercial claim, keep the creative production rule in
`vietjet-creative-factory` and hand the claim to `vietjet-commercial-ops` for verification. Do not
duplicate commercial truth inside creative references.

## Add A New Skill Safely

Before adding a skill:

1. Confirm the workflow is materially different from all existing skills.
2. Confirm it belongs within the existing plugin scope.
3. Prefer extending a shared reference when the change is governance or reusable supporting detail.
4. Define the skill owner, trigger, required inputs, output contract, risks, and human approval gate.
5. Create `skills/<skill-name>/SKILL.md` with clear `name` and `description` frontmatter.
6. Link the plugin's shared governance and only the references needed for the task.
7. Include facts/assumptions/missing-data separation and prohibit unsupported claims.
8. Add test prompts, acceptance cases, documentation, and release evidence.
9. Run the plugin and skill validators when their dependencies are available.

Do not add a skill merely to create another prompt alias. A skill should encode reusable expertise,
an SOP, or a distinct governed workflow.

## Add A Command Only After Pilot Evidence

A command is a thin orchestration entry point, not a new capability or policy source. Add one only
when pilot usage shows a repeated routing problem, a recurring governance omission, a high-risk
review that benefits from standard inputs, or a meaningful multi-skill sequence.

Before adding a command:

1. Confirm the flow already exists in current skills and references.
2. Link to the existing skills and shared governance instead of duplicating their policy.
3. Define required input, sequence, output, handoffs, and stop conditions.
4. Keep approval, publishing, activation, sending, and execution outside the command.
5. Add it to [COMMANDS.md](COMMANDS.md) and test it against a realistic pilot case.

Do not add commands merely to provide aliases for every skill.

## Update References

Use references for shared governance, deterministic worksheets, reusable templates, identity locks,
and detailed material that multiple skills need.

When updating a reference:

1. Identify every skill and document that links to it.
2. Preserve existing risk controls unless an authorized policy change explicitly replaces them.
3. Label new requirements as approved facts, proposed policy, or facts to verify.
4. Avoid adding current values that will quickly become stale unless a source owner and review date
   are recorded.
5. Update test prompts and acceptance evidence when behavior changes.
6. Require human policy review for governance changes.

## Add A New Campaign Fact

Campaign facts should enter through an authorized brief or evidence-and-approval intake, not through
creative invention.

Record:

- The exact fact and its scope
- Source link or authorized local file reference
- Source owner and source date
- Approval status
- Time sensitivity or expiry date
- Channels where the fact may be used
- Any required terms, exclusions, or disclaimers

Put reusable commercial-fact handling in `vietjet-commercial-ops`. Pass only approved or clearly
labeled brief facts to `vietjet-creative-factory`. When a fact is missing or unsupported, record
`DATA UNAVAILABLE`, `FACT TO VERIFY`, or an equivalent explicit label.

## Add An Aircraft, Mascot, Or Face Lock Rule

Add lock rules to `vietjet-creative-factory` only from approved references or written
specifications.

For every lock update:

1. Record the approved reference identifier and usage scope.
2. Separate fixed identity traits from permitted creative variation.
3. State positive preservation instructions and explicit prohibited changes.
4. Define what is visually verifiable and what remains not verifiable.
5. Require QA against the approved reference.
6. For faces, confirm authorization and consent scope; prohibit public-figure implication,
   impersonation framing, sensitive-attribute inference, and voice cloning.
7. For aircraft and mascots, prohibit invented registrations, identity redesign, model substitution,
   wrong livery, and unsupported traits as applicable.

Do not convert a campaign mood, name, or style label into an approved identity reference.

## Change Governance Rules

Governance changes have a wider impact than ordinary reference edits.

Before changing governance:

1. Identify the policy owner and change reason.
2. Cite the approved policy or decision source.
3. Assess effects on every linked skill, worksheet, runbook, test, and handoff.
4. Preserve the rule that plugin outputs remain drafts until human approval.
5. Never use a documentation edit to grant authority, approval, or execution permission.
6. Re-run affected acceptance tests and release checks when validator dependencies are available.
7. Record the change in the relevant changelog and audit trail.

## Keep Facts Separate From Assumptions

Use explicit labels:

| Label | Meaning |
|---|---|
| `FACT` | Supplied by an authorized source and usable within its confirmed scope |
| `FACT TO VERIFY` | Presented as factual but not yet supported by authorized evidence |
| `ASSUMPTION` or `HYPOTHESIS` | Proposed for planning or creative exploration, not a claim |
| `DATA UNAVAILABLE` | Required evidence was not supplied or accessed |
| `NOT VERIFIABLE` | Cannot be confirmed from the supplied reference |
| `POLICY TO CONFIRM` | Governance or authority rule has not been approved |

Keep creative assumptions visually and structurally separate from campaign requirements. Never allow
an assumption to become published copy merely because it appears plausible.

## Never Hardcode Unsupported Business Controls

Do not hardcode:

- Approver names or roles unless an approved authority source provides them
- Approval thresholds or escalation limits
- Revenue, incremental revenue, bookings, conversion, or campaign performance
- Market demand, market size, competitor claims, or route performance
- Promotional inventory, seat quotas, fares, taxes, fees, or offer eligibility
- Live schedules, aircraft assignments, or operational commitments

Instead, use a source reference, explicit placeholder, missing-data label, or proposed-policy label.
State the human owner or approval requirement only when it is supplied or authorized. The plugins
may recommend that approval is needed, but they must not invent who can grant it.

## Customization Review Checklist

- [ ] The change belongs in the selected plugin.
- [ ] No existing skill already covers the workflow.
- [ ] Facts, assumptions, and missing data remain separate.
- [ ] Commercial claims stay under commercial governance.
- [ ] Creative locks rely on approved references.
- [ ] No approvers, thresholds, revenue, market data, inventory, or performance were invented.
- [ ] Human review remains required.
- [ ] Related docs, tests, and release evidence are identified.
- [ ] Validators will be run when required dependencies are available.
