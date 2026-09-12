---
name: predict-competitive-move
description: "Predict plausible competitor research moves, timing, and preemption/priority risk with explicit assumptions."
---

# predict-competitive-move

## Purpose

Predict plausible competitor research moves, timing, and preemption/priority risk with explicit assumptions.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Separate observed competitor signals from assumptions about capability, intent, and timing.
2. Construct plausible next moves and attach a timing range, enabling evidence, and preemption consequence to each.
3. Rank priority risks under the declared horizon and identify what new evidence would reverse the forecast.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The predict competitive move decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject predict competitive move when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: competitive-move-prediction
