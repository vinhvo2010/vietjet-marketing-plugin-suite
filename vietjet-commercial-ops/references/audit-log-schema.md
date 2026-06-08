# Audit Log Schema

Use one audit-log record for every substantive plugin output. The log records workflow evidence; it does not grant approval.

## Required Schema

| Field | Type / allowed value | Description |
|---|---|---|
| `output_id` | String | Deterministic ID from [Output ID Convention](output-id-convention.md) |
| `date_time` | ISO 8601 datetime with timezone | Time the output record was created |
| `skill_used` | String or list | Plugin skill or skills used |
| `request_summary` | String | Concise description of the requested work |
| `input_facts` | List | Facts supplied or verified, with source references |
| `assumptions` | List | Assumptions used and validation status |
| `missing_data` | List | Missing evidence and its effect |
| `data_sources` | List | Authorized links or file references, source owner, and source date |
| `governance_flags` | List | Data-boundary, legal, revenue, brand, privacy, operational, or policy flags |
| `approval_status` | Enum | `NOT_REQUESTED`, `PENDING`, `APPROVED`, `APPROVED_WITH_CONDITIONS`, or `REJECTED` |
| `human_owner` | String | Named human owner or confirmed role |
| `final_output_link_file` | String | Link or file reference to the final draft/output |
| `version` | String | Plugin/output version used |
| `change_reason` | String | Why this record or output changed |

## Record Template

```yaml
output_id: VJ-COMOPS-SKILL-YYYYMMDD-NNN
date_time: YYYY-MM-DDTHH:MM:SS+TZ
skill_used:
  - skill-name
request_summary: ""
input_facts:
  - fact: ""
    source: ""
assumptions:
  - assumption: ""
    status: OPEN
missing_data:
  - item: ""
    impact: ""
data_sources:
  - reference: ""
    owner: ""
    source_date: ""
governance_flags:
  - ""
approval_status: PENDING
human_owner: ""
final_output_link_file: ""
version: "0.1.1-planned"
change_reason: "Initial draft"
```

## Logging Rules

- Create the record when substantive work begins; update it when evidence, approvals, or outputs change.
- Preserve prior records or revision history. Do not silently overwrite approval decisions.
- Do not place customer-level PII, PNR data, credentials, or restricted source content in the log.
- Record approval evidence as a link or file reference, not as an inferred status.
- Use `POLICY TO CONFIRM` when the human owner or approval workflow is unknown.
