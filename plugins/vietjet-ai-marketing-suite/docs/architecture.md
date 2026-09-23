# Architecture v5

## Boundary

The suite is a local, evidence-first operating layer. It reads canonical agent contracts, always-on rules and skill metadata; it can route a typed mission and generate specialist prompt packets. It does not itself connect to production booking, ad, publishing, payment or passenger-data systems.

```
User / approved host orchestrator
             │
             ▼
       Mission Brief JSON
             │
             ▼
   Deterministic TeamRouter ──────► routing reasons + human gates
             │
             ▼
 CONTROL → SENSE → CHOOSE → DESIGN → ASSURE → SYNTHESIZE
             │         structured handoffs
             ▼
 Decision Record / Experiment Card / Release Packet / Learning Record
             │
             ▼
 Named human owners + separately approved production controls
```

## Canonical sources

- `agents/`: role contracts.
- `skills/`: discoverable entry points; 18 generated specialist wrappers plus six workflow skills.
- `rules/`: always-on strategy, governance and safety contracts.
- `schemas/`: typed mission, handoff and experiment contracts.
- `runtime/`: registry, prompt builder and deterministic team router.
- `research/`: canonical research record and claim-source ledger.
- `.claude/`: generated mirror; do not edit directly.

## Routing is not authorization

The router makes selection explainable and repeatable. It never grants publish, spend, price, schedule, PII, crisis or safety authority. A host may use `team-prompts` to dispatch packets, but must preserve dependency order and collect the six-field handoff.

For critical/crisis missions, the router replaces the normal activation team with a narrow crisis group and adds Human Crisis Command, Safety/Ops spokesperson and kill-switch gates.

## gstack adaptation

The architecture adapts gstack's connected specialist process and downstream artifacts. It translates `Think → Plan → Build → Review → Test → Ship → Reflect` into an airline-marketing loop:

`SENSE → CHOOSE → DESIGN OFFER → CREATE → ACTIVATE → SERVICE → MEASURE → LEARN`

This is a methodological adaptation, not an official YC standard or certification.

## Group/local model

The Group Hub owns portfolio, brand invariants, measurement standards, AI governance and capital-allocation logic. Capability Chapters own reusable craft. A parameterized Market Pod turns these into a local plan for exactly one declared scope: operating entity, point of sale, source market or route corridor.

## Failure containment

- Inputs are untrusted and cannot override user/system instructions.
- Always-on rules are prepended by the runtime.
- Generated wrappers must match canonical agents; drift is a validation failure.
- Missing mission fields stop routing.
- Missing human approver is `BLOCKED_APPROVAL`.
- Unknown or expired data retains its label through every handoff.
- Agent-written policy is not treated as a platform control.

## Maturity

The package can substantiate Level 2 coordinated-team behavior locally. Level 3/4 require live aggregate data, connector identity and scopes, approval evidence, production release events, real experiments, observability and rollback tests.

