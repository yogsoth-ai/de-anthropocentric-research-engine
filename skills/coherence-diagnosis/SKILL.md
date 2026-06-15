---
name: coherence-diagnosis
description: Strategy for auditing preference consistency using Consistency Ratio,
  cycle enumeration, and mElo to detect and resolve intransitivities.
dependencies:
  tactics:
  - consistency-audit-loop
  sops:
  - convergence-check
  - ranking-synthesis
  - rating-update
---

# Coherence Diagnosis

## Purpose

Audit an existing comparison matrix for logical consistency. Detect cycles, quantify transitivity violations, localize problematic judgments, and recommend corrections. Essential as a quality gate before finalizing any ranking.

## When to use

- Existing comparison data needs validation
- Suspicion of inconsistent judgments
- Pre-finalization quality gate
- AHP consistency ratio check required
- Debugging unexpected ranking results

## Budget

| Resource | Allocation |
|----------|-----------|
| Cycle detection | Full matrix scan |
| Consistency metric | CR < 0.1 (AHP) or transitivity > 90% |
| Repair comparisons | ≤ 20% of original comparisons |
| Iterations | 1-3 audit-repair cycles |

## State Ledger

```yaml
comparison_matrix: {}   # pair → winner
candidates: []
consistency_metrics: {cr: null, transitivity: null, cycles_count: 0}
cycles: []              # [[a>b, b>c, c>a], ...]
problematic_pairs: []   # pairs involved in most cycles
repair_log: []          # [{pair, old_judgment, new_judgment, reason}]
iteration: 0
```

## Available Tactics

- **consistency-audit-loop** — detect, localize, repair, recompute

## Available SOPs

- cycle-detection
- inconsistency-localization
- comparison-executor (for re-comparison)
- rating-update (for recomputation)
- convergence-check
- ranking-synthesis

## Execution Guidance

1. Run cycle-detection on full comparison matrix
2. Compute consistency metrics (CR, transitivity score)
3. If consistent (CR < 0.1): proceed to ranking-synthesis
4. If inconsistent: run inconsistency-localization
5. Re-compare problematic pairs via comparison-executor
6. Recompute ratings and re-check consistency
7. Repeat until consistent or repair budget exhausted
8. Document all repairs in audit trail

## Output Format

```yaml
diagnosis:
  consistency_ratio: 0.04
  transitivity_score: 0.97
  cycles_found: 1
  cycles_resolved: 1
  repairs_made: 2
audit_trail:
  - {pair: ["b", "d"], original: "b", revised: "d", reason: "..."}
final_ranking_valid: true
method: consistency-ratio
```

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| consistency-audit-loop | Detect preference cycles, localize inconsistent judgments, request corrections, and recompute ratings until consistency threshold is met. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| convergence-check | Evaluate whether the ranking has stabilized by analyzing rating history and computing stability metrics. |
| ranking-synthesis | Produce the final ranking artifact from converged ratings and consistency report. |
| rating-update | Incorporate a new judgment into the rating model and return updated ratings for all candidates. |

<!-- END available-tables (generated) -->
