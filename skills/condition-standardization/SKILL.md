---
name: condition-standardization
description: Standardize evaluation condition differences across papers — 20 methods, 60 data points, 30 web searches budget
used-by: baseline-establishment
---

# Condition Standardization


## Purpose

Papers evaluate methods under different conditions (data splits, preprocessing, hardware, hyperparameter budgets). This strategy identifies condition differences, builds a normalization scheme, and produces fair-comparison baselines where results are adjusted to equivalent conditions.

## Budget

| Resource | Floor | Target |
|----------|-------|--------|
| Methods analyzed | 15 | 20 |
| Data points standardized | 40 | 60 |
| Web searches | 20 | 30 |
| Condition dimensions cataloged | 5 | 10 |

## State Ledger

```
<HARD-GATE>
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Methods analyzed | 0 | 20 | BLOCKED |
| Data points standardized | 0 | 60 | BLOCKED |
| Condition dimensions | 0 | 10 | — |
| Normalization rules defined | 0 | 5 | — |
| Fair comparison sets | 0 | 3 | — |
</HARD-GATE>
```

Cannot exit until data_points_standardized >= 48 (80% of target).

## Available Tactics

- **condition-normalization** — Compare and standardize experimental conditions

## Available SOPs

- **condition-cataloging** — Record all conditions per method-paper pair
- **compute-normalization** — Normalize by compute budget (Pareto analysis)
- **performance-table-assembly** — Produce unified comparison table

## Execution Guidance

1. Catalog all condition dimensions across extracted data points
2. Identify which conditions meaningfully affect reported scores
3. Group methods by comparable condition sets
4. Define normalization rules (e.g., adjust for data size, compute budget)
5. Apply compute-normalization for Pareto-optimal analysis
6. Produce fair comparison subsets where conditions are controlled
7. Annotate which comparisons are direct vs. adjusted

## Output Format

```json
{
  "condition_dimensions": [
    {
      "name": "string",
      "values_observed": ["string"],
      "impact_on_score": "high|medium|low|unknown",
      "normalization_rule": "string|null"
    }
  ],
  "fair_comparison_sets": [
    {
      "name": "string",
      "controlled_conditions": ["string"],
      "methods_included": ["string"],
      "adjusted_scores": []
    }
  ],
  "pareto_analysis": {
    "compute_vs_performance": [],
    "pareto_optimal_methods": []
  }
}
```
