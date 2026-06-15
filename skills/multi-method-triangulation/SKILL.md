---
name: multi-method-triangulation
description: Apply 2-3 MCDA methods to the same candidates, compare rankings, and
  identify method-sensitive options.
execution: tactic
dependencies:
  sops:
  - alternative-scoring
  - method-sensitivity-report
  - rank-comparison
---

# Multi-Method Triangulation

Score the same set of alternatives using 2-3 MCDA methods, compare ranking differences, identify method-sensitive options, and improve decision robustness.

## Stages

1. **Method Selection** — Select 2-3 complementary MCDA methods
2. **Parallel Scoring** — Score and rank candidates using each method separately
3. **Rank Comparison** — Compute ranking consistency (Kendall tau, Spearman rho)
4. **Sensitivity Identification** — Identify alternatives whose rankings change significantly across methods
5. **Method Sensitivity Report** — Analyze causes of differences and provide recommendations

## Available SOPs

- alternative-scoring — Score alternatives (invoked once per method)
- rank-comparison — Ranking consistency comparison
- method-sensitivity-report — Method sensitivity analysis report

## Execution Guidance

- Method selection should cover different paradigms (e.g., compensatory WSM + non-compensatory ELECTRE + compromise VIKOR)
- All methods use the same criteria and weights; only aggregation logic differs
- Kendall tau > 0.8 indicates high inter-method consistency, results are trustworthy
- tau < 0.6 indicates method choice significantly impacts results, requiring deeper analysis
- Pay special attention to alternatives with ranking differences >= 3 positions
- Final recommendations should clarify which conclusions are method-independent (robust) and which depend on method choice

## Minimum Yield

Ranking comparison across >=2 methods + difference analysis

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| alternative-scoring | Score each candidate alternative against all criteria to produce a score matrix. |
| method-sensitivity-report | Analyze how the choice of MCDA method affects final rankings and identify method-sensitive alternatives. |
| rank-comparison | Compare multiple ranking results to assess agreement and identify divergent items. |

<!-- END available-tables (generated) -->
