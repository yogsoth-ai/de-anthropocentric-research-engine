---
name: analyze-experiment-results
description: "Interpret completed experimental outputs after host/runtime execution using pre-declared statistical tests, effect/uncertainty estimates, reproducibility checks, and calibrated synthesis."
---

# analyze-experiment-results

## Purpose

Interpret completed experimental outputs after host/runtime execution using pre-declared statistical tests, effect/uncertainty estimates, reproducibility checks, and calibrated synthesis.

## Input contract

```yaml
required: [research_object, objective, constraints]
optional: [evidence, assumptions, prior_results]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

1. Freeze the predeclared estimand and analysis plan before reading the outcome pattern. (`statistical-testing`)
2. Run the statistical procedure and reproducibility check on the completed outputs, keeping effect size separate from decision significance. (`verify-reproducibility`)

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [effect_estimates, uncertainty_summary, reproducibility_assessment, interpretation]
delta_fields: [findings, uncertainties]
```

## Thresholds and quality gates

- Every output is traceable to a named input, called operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain α 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the conclusion; return the partial delta with the failure recorded.

## Provenance map

- resolved: result-analysis
- resolved: result-validation-loop
- resolved: statistical-testing
- resolved: reproducibility-verification
- resolved: execution-synthesis
- resolved: result-collection

## Preserved source criteria ledger

| source | criterion | treatment |
|---|---|---|
| resolved v3 entries above | node-specific scientific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | α = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return only the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
