---
description: Run a governed promotion review with date, fare, inventory, terms, channel-parity, and human-approval checks.
argument-hint: [promotion brief, copy, evidence references, and current date]
---

# Governed Promo QA

## Arguments

The promotion brief, channel copy, evidence references, and supplied current date are in
`$ARGUMENTS`.

## Workflow

1. Read `skills/promo-qa/SKILL.md` and `references/operating-governance.md`.
2. Record the supplied current date. If no current date is supplied, state that date-sensitive
   conclusions require confirmation.
3. Separate facts, facts to verify, assumptions, and missing data.
4. Check booking/travel periods, fare and `0Đ` clarity, taxes/fees, eligibility, inventory,
   universal claims, channel parity, yield dependencies, and risky CTA wording.
5. Block expired or unsupported activation language and provide safer draft copy where useful.
6. List evidence required and human approval needs without inventing approvers or authority.

## Required Output

- Promotion summary and date status
- Blocking issues and required fixes
- Fare/terms and channel-parity matrix
- Safer draft copy
- Facts to verify and missing data
- Human approval needs

End with the operating-governance end-of-run block. Any recommendation is a draft input to human
approval and must not authorize launch.
