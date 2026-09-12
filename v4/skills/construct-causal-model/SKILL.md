---
name: construct-causal-model
description: "Construct and validate an explicit causal model with measurable variables, mechanism edges, evidence links, feedback loops, interventions, counterevidence, and confidence."
---

# construct-causal-model

## Purpose

Construct and validate an explicit causal model with measurable variables, mechanism edges, evidence links, feedback loops, interventions, counterevidence, and confidence.

## Input contract

```yaml
required: [research_object, objective, constraints]
optional: [evidence, assumptions, prior_results]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

1. Define measurable variables and candidate mechanisms with explicit direction and scope. (`identify-variables`)
2. Represent mechanism edges, evidence, feedback, interventions, and counterfactual dependencies in one inspectable graph. (`extract-causal-structure`)
3. Validate causal links and update confidence while distinguishing correlation, mechanism, and intervention evidence. (`represent-mechanism-edge`)
4. Define measurable variables and candidate mechanisms with explicit direction and scope. (`attach-evidence-to-relation`)
5. Represent mechanism edges, evidence, feedback, interventions, and counterfactual dependencies in one inspectable graph. (`detect-contradiction`)
6. Validate causal links and update confidence while distinguishing correlation, mechanism, and intervention evidence. (`detect-feedback-loop`)
7. Define measurable variables and candidate mechanisms with explicit direction and scope. (`trace-causal-chain`)
8. Represent mechanism edges, evidence, feedback, interventions, and counterfactual dependencies in one inspectable graph. (`analyze-intervention`)
9. Validate causal links and update confidence while distinguishing correlation, mechanism, and intervention evidence. (`construct-counterfactual`)
10. Define measurable variables and candidate mechanisms with explicit direction and scope. (`validate-causal-link`)
11. Represent mechanism edges, evidence, feedback, interventions, and counterfactual dependencies in one inspectable graph. (`update-confidence-from-evidence`)

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [causal_graph, mechanism_edges, intervention_implications, confidence_updates]
delta_fields: [findings, evidence_updates, hypothesis_updates, assumption_updates]
```

## Thresholds and quality gates

- Every output is traceable to a named input, called operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain α 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the conclusion; return the partial delta with the failure recorded.

## Provenance map

- resolved: causal-modeling
- intermediate: variable-identification [strategy]
- resolved: mechanism-mapping
- resolved: evidence-collection
- resolved: intervention-analysis
- resolved: model-validation
- resolved: counterfactual-reasoning
- resolved: evidence-weighing

## Preserved source criteria ledger

| source | criterion | treatment |
|---|---|---|
| resolved v3 entries above | node-specific scientific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | α = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return only the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
