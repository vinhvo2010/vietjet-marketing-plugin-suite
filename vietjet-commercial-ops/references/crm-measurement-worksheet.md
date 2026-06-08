# CRM Measurement Worksheet

Use this worksheet for CRM and ancillary-upsell measurement. Use authorized aggregate data only and preserve a transparent customer experience.

## Journey and Audience Definition

| Field | Entry |
|---|---|
| Output ID |  |
| Journey or upsell name |  |
| Business objective |  |
| Target audience |  |
| Eligibility criteria |  |
| Exclusion and suppression criteria |  |
| Conversion event |  |
| Attribution window |  |
| Frequency cap |  |
| Primary data source and owner |  |

## Experiment Groups

| Measure | Exposed users | Control/holdout users |
|---|---:|---:|
| Eligible assigned users |  |  |
| Users reached |  |  |
| Conversion events |  |  |
| Upgrade revenue |  |  |
| Ancillary revenue |  |  |
| Unsubscribes |  |  |
| Complaints |  |  |

## Deterministic Calculations

```text
Exposed conversion rate = exposed conversions / exposed eligible assigned users
Control conversion rate = control conversions / control eligible assigned users

Incremental conversion rate = exposed conversion rate - control conversion rate
Incremental conversions = incremental conversion rate × exposed eligible assigned users

Exposed revenue per eligible =
  (exposed upgrade revenue + exposed ancillary revenue) / exposed eligible assigned users

Control revenue per eligible =
  (control upgrade revenue + control ancillary revenue) / control eligible assigned users

Incremental revenue =
  (exposed revenue per eligible - control revenue per eligible)
  × exposed eligible assigned users
```

Report gross upgrade revenue, gross ancillary revenue, and incremental revenue separately.

## Customer Impact

| Check | Result | Required action |
|---|---|---|
| Unsubscribe-rate difference versus control/baseline |  |  |
| Complaint-rate difference versus control/baseline |  |  |
| Refund or service-contact impact |  |  |
| Frequency cap respected |  |  |
| No-dark-pattern check passed | `YES` / `NO` |  |
| Customer value check passed | `YES` / `NO` |  |

### No-Dark-Pattern Check

- [ ] No paid option is preselected
- [ ] Decline path is equally clear
- [ ] Incremental price and conditions are visible
- [ ] Benefits are verified and not overstated
- [ ] No false scarcity, hidden opt-out, or misleading urgency

### Customer Value Check

- [ ] Offer is relevant to the confirmed eligible audience
- [ ] Verified benefits justify the presented price
- [ ] Journey does not target disrupted, refund, complaint, or suppressed cases
- [ ] Contact pressure remains within the confirmed frequency cap
- [ ] Negative customer signals are reviewed with conversion outcomes

## Validity and Confidence

| Check | Result |
|---|---|
| Assignment randomized or selection bias documented |  |
| Eligibility consistent across groups |  |
| Measurement windows aligned |  |
| Holdout contamination checked |  |
| Sample sizes and uncertainty reviewed |  |
| Missing data documented |  |

**Confidence level:** `HIGH` / `MEDIUM` / `LOW`  
**What can be claimed:**  
**What cannot be claimed:**  

## Approval Gate

| Approval owner | Scope | Status | Conditions |
|---|---|---|---|
|  | Journey and customer experience |  |  |
|  | Pricing/revenue |  |  |
|  | Privacy and consent |  |  |
|  | Measurement method |  |  |
