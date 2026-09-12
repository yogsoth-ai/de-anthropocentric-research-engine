---
name: optimize-design-under-budget
description: "Given cost per run and resource budget, choose the most information-efficient feasible design while preserving essential validity constraints."
---

# optimize-design-under-budget

## Purpose

Given cost per run and resource budget, choose the most information-efficient feasible design while preserving essential validity constraints.

## Input contract

```yaml
required: [research_object, operation_parameters]
optional: [evidence, assumptions, constraints]
constraints: [use named scientific objects; retain provenance and missingness; α = 0.05 and power = 0.8 where applicable]
```

## Procedure

1. Translate the resource budget into per-run limits, fixed overhead, and validity constraints that no candidate may violate.
2. Compare feasible designs by expected information per cost while preserving the essential contrast, randomization, and measurement plan.
3. Select the dominant design or document the tradeoff when no candidate is strictly superior; include the budget ledger.

## Output contract

```yaml
produces: [operation_result, evidence_trace, uncertainties]
delta_fields: [findings, evidence_updates, uncertainties]
```

## Quality gates

- The optimize design under budget decision is tied to its declared scientific object and source evidence.
- Missing values, assumptions, and boundary conditions remain visible.
- Statistical criteria stay exact where applicable: α 0.05 and power 0.8.

## Failure and counterexamples

Reject optimize design under budget when the target schema is incomplete, evidence is incompatible, or a counterexample defeats the stated interpretation.

## Provenance map

- resolved: budget-constrained-design
