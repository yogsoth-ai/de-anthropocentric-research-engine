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

Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `evaluate-falsifiability` to evaluate the claim's reachable falsifiers.
2. You MUST load skill `operationalize-construct` to operationalize every construct used by the claim.
3. You MUST load skill `specify-boundaries` to state the scope and boundary conditions.
   If the audit exposes an ill-formed question, consider `formulate-research-question`. If the claim is ready for an empirical test, consider `design-experiment`. If a broader falsification program is required, `falsification-first-audit` may be the better next tactic.

Deviation: reorder only when a dependency is already satisfied or unavailable; record the reason and confidence effect.

## Output contract

```yaml
produces: [falsifiability_verdict, operational_definition, boundary_conditions]
delta_fields: [findings, decisions]
```

## Thresholds and quality gates

- Each output is traceable to an input object, operation, and evidence reference.
- Scope, assumptions, and unresolved alternatives remain explicit.
- Retain $\alpha$ 0.05 and power 0.8 wherever the predeclared statistical design requires them.

## Failure and counterexamples

Stop synthesis when a required object is absent, a precondition is violated, or a counterexample invalidates the proposed conclusion; return the partial delta with the failure recorded.

## Provenance map

- resolved: falsifiability-audit
- resolved: hypothesis-operationalization

## Preserved source criteria ledger

| source | criterion | treatment |
|---|---|---|
| resolved v3 entries above | node-specific criteria | retained and specialized to the v4 object contract |
| experiment-execution/statistical-testing | $\alpha$ = 0.05 | fixed value retained where applicable |
| experiment-execution/sample-size-estimation | power = 0.8 | fixed value retained where applicable |

## Context checkpoint / Delta notes

Return the node-specific research-state delta and preserve findings, evidence updates, uncertainties, decisions, open questions, and recommended jumps as applicable.
