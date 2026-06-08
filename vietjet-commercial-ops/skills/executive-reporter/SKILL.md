---
name: executive-reporter
description: Convert internal documents, emails, Sheets data, campaign results, and briefings into CCO/CEO-ready one-pagers, board-style updates, and executive summaries. Output is precise, data-grounded, and decision-oriented.
---

# executive-reporter

Before starting, read and apply [Operating Governance](../../references/operating-governance.md).

## Purpose
Transform complex, multi-source internal content into clear, board-ready executive communication. Produces one-pagers, monthly close narratives, board packs, stakeholder updates, and CCO/CEO briefings — in the register that senior leaders read quickly and act on.

## Input Required
Provide ONE or MORE of:
- A Google Sheet with revenue or campaign performance data (paste or link)
- A Google Doc brief or report (paste or link)
- A set of bullet points or raw data to structure
- Email threads with key decisions or outcomes
- A request: "Summarise last month's revenue performance for the board"

Minimum viable input: key metrics + context (what happened, why, what's next).

## Connected Tools Needed
| Tool | Used For | Required? |
|---|---|---|
| Google Drive | Read source reports, briefs | Recommended |
| Google Sheets | Pull revenue tables, KPI data | Recommended |
| Google Docs | Read source material; output as shareable doc | Recommended |
| Gmail | Read email threads for context | Optional |

## Step-by-Step Workflow

**Step 1 — Identify output type**
Determine which format is needed:
- One-pager (CCO/CEO, 5-minute read)
- Monthly revenue close narrative
- Board pack section
- Stakeholder update (non-finance audience)
- Campaign performance summary

**Step 2 — Identify audience**
- CCO/CFO: numbers-first, variance explanation, decisions needed
- CEO: one headline, top 3 implications, one ask
- Cross-functional (Network, Ops, HR): translate metrics to their domain's impact
- Board: 8 pages maximum; every number traceable to a source

**Step 3 — Extract and validate facts**
- Separate confirmed data (from source documents) from estimates
- Mark all estimates with [EST] and hypotheses with [HYP]
- Mark unavailable data as [DATA UNAVAILABLE] — never fill gaps with narrative

**Step 4 — Apply the executive writing rules**
- First sentence: most important fact (not background, not context)
- Active voice: "Revenue declined 4%" not "There was a decline in revenue"
- Numbers rounded to readable precision: VND 1.2B not VND 1,234,567,890
- Maximum 3 bullets per section — cut the rest

**Step 5 — Build the output document**
Follow the format for the selected output type (see below).

**Step 6 — Flag decisions and actions**
Every executive document ends with: Decisions Required (numbered, with owner and deadline) and Next Steps (numbered, with owner and date).

For a campaign or route-launch decision brief, include:
- Decision requested and decision deadline
- Options: approve / approve with conditions / defer
- Confirmed facts versus assumptions
- Commercial upside and downside without inventing a financial case
- Gating evidence still required before execution

## Output Format

### One-Pager (default)
```
[TITLE] | [Date] | DRAFT

THE SITUATION (2–3 bullets — most important fact first)

THE NUMBERS
Metric | Actual | Plan/Target | Variance | Note

TOP 3 WINS

TOP 3 CONCERNS

DECISIONS NEEDED FROM LEADERSHIP
1. [Decision] — Owner: [role] — By: [date]

OPTIONS AND TRADE-OFFS
[Approve / Approve with conditions / Defer]

NEXT STEPS
1. [Action] — Owner: [role] — By: [date]

[DRAFT — HUMAN APPROVAL REQUIRED before distribution]
```

### Monthly Revenue Close Narrative
```
[Month] Revenue Performance Summary | DRAFT

HEADLINE: [One sentence: total revenue vs. plan, % variance]

PASSENGER REVENUE
[3 bullets: what drove variance, top routes, bottom routes]

ANCILLARY REVENUE
[2 bullets: APax vs. target, top/bottom product]

PROMO REVIEW
[2 bullets: ROI, yield floor maintained?]

FORECAST ACCURACY
[1 bullet: MAPE for the month]

FORWARD LOOK + DECISIONS NEEDED
[3 bullets max]

[DRAFT — HUMAN APPROVAL REQUIRED before distribution]
```

## Human Approval Checkpoint
> Before any executive document is shared with CCO, CFO, CEO, or Board: the designated data owner must review all numbers for accuracy, and the designated communications owner must review tone and brand consistency. Confirm these roles from the authority matrix. Never send directly from Codex; export, review, then send manually.

## Example Command
```
/executive-reporter

Output type: One-pager for CCO
Source: Paste data below

Revenue last month: VND 1.8T vs. plan VND 2.1T (-14%)
Yield decline: -6% domestic, -2% international
APax: VND 290k vs. target VND 320k
Key issues: HAN-SGN underperformed, promo in Week 2 diluted yield
Action taken: Tightened promo checklist, RM team expanded
```

## Risks and Guardrails
- **No invented numbers** — if a figure is not in the input, write [DATA UNAVAILABLE].
- **No forward-looking revenue projections** unless based on provided forecast data — flag as [FORECAST — subject to change].
- **Board documents are legal/regulatory documents** in listed companies — flag: [LEGAL REVIEW RECOMMENDED before Board distribution].
- **Currency and rounding** — always confirm whether figures are VND or USD before outputting. Never mix currencies without labelling.
- **Competitive intelligence** in board packs — any competitor data must be sourced. Do not include unsourced competitor claims.
