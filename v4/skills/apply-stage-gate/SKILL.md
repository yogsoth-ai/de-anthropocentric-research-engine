---
name: apply-stage-gate
description: "Apply explicit GO / HOLD / RECYCLE / KILL (or supplied) stage-gate criteria with evidence thresholds and next-step conditions."
---

# apply-stage-gate
## Purpose
Apply explicit GO / HOLD / RECYCLE / KILL gates to a candidate or work package, tying each outcome to evidence thresholds and a next action.
## Input contract
```yaml
required: [candidate_record, gate_criteria, evidence_register]
optional: [prior_gate_decision, remediation_options]
constraints: [each criterion has an observable status; gate outcome and next action are explicit]
```
## Procedure
1. Normalize the candidate, gate criteria, evidence, and unresolved assumptions into a gate table.
2. Evaluate every criterion as met, unmet, or unknown, preserving the cited evidence and threshold direction.
3. Apply precedence: KILL for disqualifying hard failure, RECYCLE for repairable failure, HOLD for insufficient evidence, otherwise GO.
4. Emit the gate decision, failed criteria, evidence gaps, and the smallest justified next action.
## Output contract
```yaml
produces: [gate_table, gate_decision, failed_criteria, next_action]
delta_fields: [findings, evidence_updates, uncertainties, decisions, recommended_jumps]
```
## Quality gates
- A-class gate: declared universe = all candidate criteria and evidence items; numerator = criteria with explicit status and source; batch increment = one evaluated criterion; stopping reason = every criterion resolved or a hard failure terminates the gate; source references = criterion/evidence IDs; direction/threshold reason = GO requires all hard criteria met, while HOLD/RECYCLE/KILL follows the declared precedence.
- No GO is emitted while any hard criterion is unknown.
## Failure and counterexamples
Do not turn an absent measurement into a pass. A repairable shortfall is RECYCLE only when a concrete remediation and re-gate condition are recorded.
## Provenance map
- concept: convergence/feasibility-assessment/stage-gate [strategy/tactic]
