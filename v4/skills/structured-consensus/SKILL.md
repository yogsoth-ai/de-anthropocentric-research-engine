---
name: structured-consensus
description: "Map disagreement, iterate evidence/argument refinement, and terminate with an output contract containing stable consensus, unresolved disagreements, confidence/probabilities, and threshold/stop rationale."
---

# structured-consensus

## Purpose

Map disagreement, iterate evidence/argument refinement, and terminate with an output contract containing stable consensus, unresolved disagreements, confidence/probabilities, and threshold/stop rationale.

## Input contract

```yaml
required: [judgment_records, evidence_records, stopping_rule]
optional: [assumptions, prior_findings, evidence_updates]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

1. Use `map-disagreement` on its named scientific object and record the evidence or decision it contributes.
2. Use `run-convergence-round` on its named scientific object and record the evidence or decision it contributes.
3. Use `calibrate-probability-forecast` on its named scientific object and record the evidence or decision it contributes.
4. Use `set-threshold` on its named scientific object and record the evidence or decision it contributes.

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [consensus_report, unresolved_disagreements, confidence_summary]
delta_fields: [findings, decisions]
```

## Thresholds and quality gates

- Each output is traceable to an input object, operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain $\alpha$ 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the proposed conclusion; return the partial delta with the failure recorded.

## Provenance map

- resolved: structured-consensus
- resolved: convergence-distillation
- resolved: disagreement-cartography
- resolved: argument-crystallization
- resolved: disagreement-mapping
- resolved: iterative-convergence-round

## Preserved source criteria ledger

| source | criterion | treatment |
|---|---|---|
| resolved v3 entries above | node-specific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | $\alpha$ = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
