---
name: falsifiability-audit
description: "Gate a hypothesis on falsifiability, operational definition, and boundary conditions; can be entered from any hypothesis-generation path."
---

# falsifiability-audit

## Purpose

Gate a hypothesis on falsifiability, operational definition, and boundary conditions; can be entered from any hypothesis-generation path.

## Input contract

```yaml
required: [research_object, objective, constraints]
optional: [evidence, assumptions, prior_results]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

1. State the hypothesis as a claim with an observable consequence and explicit boundary conditions. (`evaluate-falsifiability`)
2. Operationalize constructs and evaluate whether an admissible observation could contradict the claim. (`operationalize-construct`)
3. Return the verdict, missing operational detail, and the smallest repair that preserves falsifiability. (`specify-boundaries`)

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [falsifiability_verdict, operational_definition, boundary_conditions]
delta_fields: [findings, uncertainties]
```

## Thresholds and quality gates

- Every output is traceable to a named input, called operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain α 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the conclusion; return the partial delta with the failure recorded.

## Provenance map

- resolved: falsifiability-audit
- resolved: hypothesis-operationalization

## Preserved source criteria ledger

| source | criterion | treatment |
|---|---|---|
| resolved v3 entries above | node-specific scientific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | α = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return only the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
