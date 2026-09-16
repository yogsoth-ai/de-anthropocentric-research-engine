---
name: construct-causal-model
description: "Construct and validate an explicit causal model with measurable variables, mechanism edges, evidence links, feedback loops, interventions, counterevidence, and confidence."
---

# construct-causal-model

## Purpose

Construct and validate an explicit causal model with measurable variables, mechanism edges, evidence links, feedback loops, interventions, counterevidence, and confidence.

## Input contract

```yaml
required: [variable_records, mechanism_candidates, evidence_records]
optional: [assumptions, prior_findings, evidence_updates]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `identify-variables` to inventory outcomes, factors, mediators, moderators, confounders, and assumptions before drawing any edge.
2. You MUST load skill `extract-causal-structure` to extract directed cause-mediator-effect chains with temporal order, boundary conditions, and evidence anchors.
3. You MUST load skill `represent-mechanism-edge` to encode each mechanism edge with pathway, sign, enabling conditions, falsifier, and strength.
4. You MUST load skill `attach-evidence-to-relation` to attach independent supporting and contradicting evidence while retaining alternative interpretations.
5. You MUST load skill `detect-contradiction` to compare opposing causal claims under common scope before validation.
6. You MUST load skill `detect-feedback-loop` to find reinforcing and balancing cycles, delays, uncertain edges, and testable loop implications.
7. You MUST load skill `trace-causal-chain` to trace target outcomes through intermediate nodes, branches, and because-links.
8. You MUST load skill `analyze-intervention` to map intervention components, dose, timing, implementation fidelity, comparators, and heterogeneous effects.
9. You MUST load skill `construct-counterfactual` to propagate a declared intervention and classify the counterfactual outcome.
10. You MUST load skill `validate-causal-link` to apply CLR-style checks for existence, connection, sufficiency, omitted conditions, and alternatives.
11. You MUST load skill `update-confidence-from-evidence` to reweight confidence while preserving unresolved conflicts and permitted bounds.
    If the model should generate testable explanations, consider `formulate-hypotheses`. If a specific intervention needs minimal-flip and necessity analysis, consider `counterfactual-causal-analysis`.

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [causal_graph, mechanism_edges, intervention_implications, confidence_updates]
delta_fields: [findings, decisions]
```

## Thresholds and quality gates

- Each output is traceable to an input object, operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain $\alpha$ 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the proposed conclusion; return the partial delta with the failure recorded.

## Provenance map

- intermediate: knowledge-structuring/causal-modeling [campaign]
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
| resolved v3 entries above | node-specific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | $\alpha$ = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
