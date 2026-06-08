# Output ID Convention

Use deterministic output IDs for substantive plugin outputs and their audit-log records.

## Format

```text
VJ-{PLUGIN}-{SKILL}-{YYYYMMDD}-{NNN}
```

Example:

```text
VJ-COMOPS-PROMOQA-20260608-001
```

## Components

| Component | Rule |
|---|---|
| `VJ` | Fixed Vietjet prefix |
| `{PLUGIN}` | Use `COMOPS` for `vietjet-commercial-ops` |
| `{SKILL}` | Use the approved uppercase skill code below |
| `{YYYYMMDD}` | Local calendar date when the output record is first created |
| `{NNN}` | Three-digit sequence starting at `001` |

## Skill Codes

| Skill | Code |
|---|---|
| `brand-voice` | `BRANDVOICE` |
| `campaign-factory` | `CAMPAIGN` |
| `crm-personalization` | `CRM` |
| `executive-reporter` | `EXECREPORT` |
| `promo-qa` | `PROMOQA` |
| `revenue-governance` | `REVGOV` |
| `revenue-pmo` | `REVPMO` |
| `route-marketing` | `ROUTEMKT` |

For a multi-skill output, use the primary skill's code and list all supporting skills in the audit log.

## Sequence Rules

1. Sequence numbers reset each local calendar day for each skill code.
2. Assign the next unused sequence for that date and skill.
3. Never reuse an ID, including after an output is rejected or deleted.
4. Revisions retain the original output ID; record revision/version and change reason in the audit log.
5. If the next sequence cannot be confirmed, use `PENDING-ID` until the audit-log owner assigns it. Do not guess.

## Examples

```text
VJ-COMOPS-ROUTEMKT-20260608-001
VJ-COMOPS-PROMOQA-20260608-001
VJ-COMOPS-PROMOQA-20260608-002
VJ-COMOPS-CRM-20260609-001
```
