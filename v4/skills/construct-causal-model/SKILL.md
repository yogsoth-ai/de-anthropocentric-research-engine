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

1. Inventory outcomes, factors, mediators, moderators, confounders, and assumptions before drawing any edge. (`identify-variables`)
2. Extract directed cause–mediator–effect chains with temporal order, boundary conditions, and evidence anchors. (`extract-causal-structure`)
3. Encode each mechanism edge with pathway, sign, enabling conditions, falsifier, and strength. (`represent-mechanism-edge`)
4. Attach independent supporting and contradicting evidence to those typed edges, retaining alternative interpretations. (`attach-evidence-to-relation`)
5. Compare opposing causal claims under common scope so conflicts are recorded before model validation. (`detect-contradiction`)
6. Search the directed structure for reinforcing and balancing cycles, delays, uncertain edges, and testable loop implications. (`detect-feedback-loop`)
7. Trace the validated graph from each target outcome through intermediate nodes, branches, and because-links. (`trace-causal-chain`)
8. Map intervention components, dose, timing, implementation fidelity, comparators, and heterogeneous effects onto the model. (`analyze-intervention`)
9. Freeze declared invariants, propagate the intervention through the graph, and classify the counterfactual outcome. (`construct-counterfactual`)
10. Apply CLR-style checks to each causal link for existence, connection, sufficiency, omitted conditions, and alternatives. (`validate-causal-link`)
11. Reweight confidence using the complete evidence ledger, preserving unresolved conflicts and permitted bounds. (`update-confidence-from-evidence`)

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
