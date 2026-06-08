# Post-Campaign Measurement Worksheet

Use this worksheet for deterministic post-campaign reporting. Use authorized aggregate data only. Do not describe gross or attributed outcomes as incremental.

## Campaign Definition

| Field | Entry |
|---|---|
| Output ID |  |
| Campaign name |  |
| Business objective |  |
| Booking/campaign period |  |
| Attribution window |  |
| Exposed-group definition |  |
| Holdout/control-group definition |  |
| Baseline definition and period |  |
| Primary data source and owner |  |

## Required Inputs

| Measure | Exposed group | Holdout/control group | Baseline | Data source |
|---|---:|---:|---:|---|
| Eligible users or opportunities |  |  |  |  |
| Gross bookings |  |  |  |  |
| Gross revenue |  |  |  |  |
| Ancillary revenue, if in scope |  |  |  |  |
| Cancellations/refunds, if in scope |  |  |  |  |

## Deterministic Calculations

Use the same eligibility rules and measurement window for exposed and control groups.

```text
Exposed booking rate = exposed gross bookings / exposed eligible population
Control booking rate = control gross bookings / control eligible population

Incremental booking rate = exposed booking rate - control booking rate
Incremental bookings = incremental booking rate × exposed eligible population

Exposed revenue per eligible = exposed gross revenue / exposed eligible population
Control revenue per eligible = control gross revenue / control eligible population

Incremental revenue per eligible = exposed revenue per eligible - control revenue per eligible
Incremental revenue = incremental revenue per eligible × exposed eligible population
```

If no valid control exists, report gross outcomes and baseline comparisons only. Mark incremental bookings and incremental revenue `NOT MEASURABLE`.

## Confounders and Validity

| Check | Result | Impact on claim |
|---|---|---|
| Randomized or otherwise comparable groups |  |  |
| Same eligibility criteria |  |  |
| Same attribution and measurement windows |  |  |
| Overlapping campaigns or promotions |  |  |
| Fare, schedule, inventory, or operational changes |  |  |
| Channel spillover or holdout contamination |  |  |
| Refund/cancellation treatment |  |  |
| Missing or delayed data |  |  |

## Confidence Level

| Level | Minimum interpretation |
|---|---|
| `HIGH` | Valid comparable control, complete authorized data, aligned windows, and no material unresolved confounders |
| `MEDIUM` | Usable comparison with documented limitations or minor unresolved confounders |
| `LOW` | Baseline-only, non-comparable groups, incomplete data, or material confounders |

**Assigned confidence:** `HIGH` / `MEDIUM` / `LOW`  
**Reason:**  

## Claim Boundary

**What can be claimed**

- Gross bookings and gross revenue supported by the identified authorized data source.
- Incremental bookings or revenue only when the control design and calculation pass the validity checks.
- Channel or audience comparisons only when definitions and windows are comparable.

**What cannot be claimed**

- Exposed gross revenue as incremental revenue.
- Causation from a baseline-only comparison.
- ROI without approved cost and incremental-impact inputs.
- Universal campaign success when route, channel, audience, or inventory data is incomplete.

## Human Review

| Review owner | Review scope | Status | Conditions or corrections |
|---|---|---|---|
|  | Data accuracy |  |  |
|  | Incrementality method |  |  |
|  | Commercial interpretation |  |  |
