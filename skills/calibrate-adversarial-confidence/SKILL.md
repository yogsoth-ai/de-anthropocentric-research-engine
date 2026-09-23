---
name: calibrate-adversarial-confidence
description: "Track confidence in competing claims/roles across adversarial rounds and update confidence only when evidence or argument quality warrants it."
---

# calibrate-adversarial-confidence
## Purpose
Track confidence in competing claims or roles across adversarial rounds and update only when evidence or argument quality warrants it.
## Input contract
```yaml
required: [round_records, competing_claims, update_rule]
optional: [prior_confidence, calibration_history]
constraints: [every update cites evidence or argument-quality change]
```
## Procedure
1. Record each round's claims, arguments, and evidence.
2. Apply the declared update rule and preserve dissent.
3. Mark escalation, continuation, termination, or saturation with rationale.
## Output contract
```yaml
produces: [confidence_trace, update_rationale, round_status, unresolved_dissent]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- A-class calibration: declared universe = all completed debate rounds; numerator = rounds with evidence-linked updates; batch increment = one round; stopping reason = confidence stabilizes or unresolved dissent is explicit; source references = round/evidence IDs; direction/threshold reason = update only toward claims supported by new evidence or stronger argument.
## Failure and counterexamples
Do not update confidence for rhetoric, repetition, or role status alone.
## Provenance map
- resolved: adversarial-escalation
- concept: confidence-escalation [sop]
- resolved: confidence-calibration
