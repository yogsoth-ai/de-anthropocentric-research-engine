---
name: analyze-experiment-results
description: "Interpret completed experimental outputs after host/runtime execution using pre-declared statistical tests, effect/uncertainty estimates, reproducibility checks, and calibrated synthesis."
---

# analyze-experiment-results

## Purpose

Interpret completed experimental outputs after host/runtime execution using pre-declared statistical tests, effect/uncertainty estimates, reproducibility checks, and calibrated synthesis.

## Input contract

```yaml
required: [experiment_results, predeclared_analysis_plan, reproducibility_target]
optional: [assumptions, prior_findings, evidence_updates]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `statistical-testing` to run the preregistered statistical tests and retain effect uncertainty.
2. You MUST load skill `verify-reproducibility` to verify the declared reproduction level.
   If the results must be assembled into claims, evidence, and counterclaims, consider `construct-argument-map`. If several interventions or methods require comparative selection, consider `rank-candidates`.

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [effect_estimates, uncertainty_summary, reproducibility_assessment, interpretation]
delta_fields: [uncertainties]
```

## Thresholds and quality gates

- Each output is traceable to an input object, operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain $\alpha$ 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the proposed conclusion; return the partial delta with the failure recorded.

## Provenance map

- intermediate: experiment-execution/result-analysis [strategy]
- resolved: result-validation-loop
- resolved: statistical-testing
- resolved: reproducibility-verification
- resolved: execution-synthesis
- resolved: result-collection

## Preserved source criteria ledger

| source | criterion | treatment |
|---|---|---|
| resolved v3 entries above | node-specific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | $\alpha$ = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
