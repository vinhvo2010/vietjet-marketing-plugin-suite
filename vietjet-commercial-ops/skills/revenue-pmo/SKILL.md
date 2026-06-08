---
name: revenue-pmo
description: Turn airline revenue or commercial briefs into a 12-week execution backlog with owners, KPIs, risks, dependencies, and weekly review cadence. Use for any new commercial initiative, department build, or revenue program launch.
---

# revenue-pmo

Before starting, read and apply [Operating Governance](../../references/operating-governance.md).

## Purpose
Convert a commercial or revenue strategy brief into a fully structured 12-week transformation program — with workstreams, owners, deliverables, dependencies, KPIs, risks, and a week-by-week action plan. Produces output that a VP or Head can assign and track from Day 1.

## Input Required
Provide ONE or MORE of:
- A strategy document or brief (paste text or link Drive file)
- A goal statement: "We want to [achieve X] by [date] for [route/product/team]"
- An existing plan that needs to be operationalized
- The Revenue Department Blueprint (`VJ-Revenue-Department/00_Master_Blueprint_v2.md`)

Minimum viable input: 3 sentences describing the initiative, the team, and the deadline.

## Connected Tools Needed
| Tool | Used For | Required? |
|---|---|---|
| Google Drive | Read strategy brief or existing docs | Optional — can paste manually |
| Google Docs | Output backlog as a shared document | Optional |
| Google Sheets | Output week-by-week task tracker | Optional |

## Step-by-Step Workflow

**Step 1 — Understand scope**
Identify: initiative name, business unit, sponsor, timeline, team size, and success metric.
Ask if unclear: "What does success look like at Week 12? Who owns execution?"

**Step 2 — Identify assumptions**
Flag any statement that is a hypothesis (not confirmed by data). List them separately with validation method.

**Step 3 — Define workstreams**
Group work into 5–9 workstreams (e.g., People, Data, Process, Technology, Governance, Commercial, CRM, AI Systems).

**Step 4 — Build 12-week backlog**
For each workstream, produce:
- Week 1–2: Foundation tasks
- Week 3–4: Operational build
- Week 5–8: Depth and testing
- Week 9–12: Scale and review

**Step 5 — Assign each task**
Every task gets: Owner (role), Definition of Done, Data Required, Blocker flag.

**Step 6 — KPI tree**
Primary metric → sub-metrics → operational inputs. Each with formula and data source.

**Step 7 — Risk register**
Top 5 risks: description, likelihood (H/M/L), impact (H/M/L), mitigation, owner.

**Step 8 — Weekly cadence**
Daily standup agenda, weekly review agenda, monthly close agenda.

## Output Format

```
SECTION A: Initiative Summary (1 page)
SECTION B: Assumptions to Validate (table)
SECTION C: 12-Week Backlog by Workstream (table per workstream)
SECTION D: RACI Matrix
SECTION E: KPI Tree
SECTION F: Risk Register
SECTION G: Operating Cadence Templates
SECTION H: First 10 Actions (start tomorrow)

[DRAFT — HUMAN APPROVAL REQUIRED before sharing]
```

## Human Approval Checkpoint
> Before this backlog is shared with any team or used to assign work, the VP/Head sponsoring the initiative must review and confirm: (1) owners are correct, (2) timelines are realistic, (3) assumptions are acknowledged. Add a sign-off block at the bottom of the output.

## Example Command
```
/revenue-pmo

Brief: We are building a Revenue Management Department for Vietjet's international routes.
Goal: Full department operational in 12 weeks.
Team: VP Revenue (hire), Head of RM (hire), 2 analysts (existing staff reassigned).
Success metric: Daily RM standup running, D-14 forecast live, first board pack delivered.
Deadline: Week 12 from today.
```

## Risks and Guardrails
- **Do not set revenue targets** in the backlog unless the user has provided validated baseline data. Write [TARGET TBC — requires baseline data] instead.
- **Do not name specific individuals** as owners — use role titles only, unless user explicitly provides names.
- **Do not claim current state** of any system unless user has provided evidence. Use [HYPOTHESIS] tag.
- **Timelines are recommendations** — flag any task where the Week assignment depends on a hiring or data access dependency.
