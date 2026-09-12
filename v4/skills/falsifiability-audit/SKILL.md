---
name: falsifiability-audit
description: "Gate a hypothesis on falsifiability, operational definition, and boundary conditions; can be entered from any hypothesis-generation path."
---

# falsifiability-audit

## Purpose

Gate a hypothesis on falsifiability, operational definition, and boundary conditions; can be entered from any hypothesis-generation path.

## Input contract

```yaml
required: [hypothesis, operational_definition, boundary_conditions]
optional: [assumptions, prior_findings, evidence_updates]
constraints: [consume named scientific objects; preserve provenance; keep unresolved uncertainty visible]
```

## Execution protocol

1. Use `evaluate-falsifiability` on its named scientific object and record the evidence or decision it contributes.
2. Use `operationalize-construct` on its named scientific object and record the evidence or decision it contributes.
3. Use `specify-boundaries` on its named scientific object and record the evidence or decision it contributes.

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [falsifiability_verdict, operational_definition, boundary_conditions]
delta_fields: [findings, decisions]
```

## Thresholds and quality gates

- Each output is traceable to an input object, operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain α 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the proposed conclusion; return the partial delta with the failure recorded.

## Provenance map

- resolved: falsifiability-audit
- resolved: hypothesis-operationalization

## Preserved source criteria ledger

| source | criterion | treatment |
|---|---|---|
| resolved v3 entries above | node-specific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | α = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
