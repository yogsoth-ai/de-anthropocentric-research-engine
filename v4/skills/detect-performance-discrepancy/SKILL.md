---
name: detect-performance-discrepancy
description: "Detect material score discrepancies for the same method/task across sources and propose likely explanatory condition differences."
---

# detect-performance-discrepancy

## Purpose

Detect material score discrepancies for the same method or task across sources and identify plausible condition differences.

## Input contract

```yaml
required: [performance_records, method_key, task_key, metric_schema]
optional: [protocol_records, condition_schema, uncertainty_estimates]
constraints: [comparisons require aligned metric direction and declared conditions]
```

## Procedure

1. Align records by method, task, metric, and observation context.
2. Quantify score differences with uncertainty and identify materially different pairs.
3. Compare datasets, prompts, evaluators, budgets, and protocol conditions.
4. Rank plausible explanations and retain unresolved alternatives.

## Output contract

```yaml
produces: [discrepancy_pairs, condition_difference_map, explanation_candidates, residual_uncertainties]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Materiality uses a declared comparison basis.
- Protocol mismatch is separated from method change.

## Failure and counterexamples

Do not call rounding noise a discrepancy or infer a method improvement from non-equivalent evaluation conditions.

## Provenance map

- `resolved: discrepancy-identification`
- `resolved: discrepancy-analysis`
