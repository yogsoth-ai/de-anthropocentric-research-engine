---
name: structured-consensus
description: "Map disagreement, iterate evidence/argument refinement, and terminate with an output contract containing stable consensus, unresolved disagreements, confidence/probabilities, and threshold/stop rationale."
---

# structured-consensus

## Purpose

Map disagreement, iterate evidence/argument refinement, and terminate with an output contract containing stable consensus, unresolved disagreements, confidence/probabilities, and threshold/stop rationale.

## Input contract

```yaml
required: [research_object, objective, constraints]
optional: [evidence, assumptions, prior_results]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

1. Map the judgment space into stable agreements, disagreements, evidence quality, and calibrated probabilities. (`map-disagreement`)
2. Run bounded convergence rounds that revise arguments and confidence without erasing minority positions. (`run-convergence-round`)
3. Apply the stopping threshold and return consensus, unresolved disagreements, confidence, and stop rationale. (`calibrate-probability-forecast`)
4. Map the judgment space into stable agreements, disagreements, evidence quality, and calibrated probabilities. (`set-threshold`)

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [consensus_report, unresolved_disagreements, confidence_summary]
delta_fields: [findings, uncertainties]
```

## Thresholds and quality gates

- Every output is traceable to a named input, called operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain α 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the conclusion; return the partial delta with the failure recorded.

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
| resolved v3 entries above | node-specific scientific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | α = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return only the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
