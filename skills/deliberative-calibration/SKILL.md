---
name: deliberative-calibration
description: Strategy for small-N complete pairwise comparison using Bradley-Terry,
  Thurstone, AHP, and Borda methods to produce calibrated rankings.
dependencies:
  tactics:
  - adaptive-pair-selection
  - consistency-audit-loop
  sops:
  - ranking-synthesis
---

# Deliberative Calibration

## Purpose

Produce a fully calibrated ranking when the candidate set is small enough (5-15 items) to allow complete or near-complete pairwise comparison. Leverages parametric models (Bradley-Terry, Thurstone) and structured weighting (AHP) to extract maximum information from each comparison.

## When to use

- Candidate count N ≤ 15
- Complete comparison matrix is feasible (N(N-1)/2 pairs manageable)
- High precision required — every rank position matters
- Calibrated strength scores needed, not just ordinal ranking

## Budget

| Resource | Allocation |
|----------|-----------|
| Comparisons | N(N-1)/2 (complete) or ≥ N×log(N) (near-complete) |
| Iterations | 2-4 rounds (initial + consistency repair) |
| Convergence target | CR < 0.1, rating stability ≥ 95% |

## State Ledger

```yaml
candidates: []          # list of items being ranked
comparison_matrix: {}   # pair → {winner, confidence, reasoning}
ratings: {}             # candidate → score
method: ""              # bradley-terry | thurstone | ahp | borda
iteration: 0
convergence: {stable: false, score: 0.0}
consistency: {cr: null, cycles: []}
```

## Available Tactics

- **adaptive-pair-selection** — select next pairs by information gain, compare, update, check convergence
- **consistency-audit-loop** — verify transitivity, repair inconsistencies

## Available SOPs

- pair-selector
- comparison-executor
- rating-update
- convergence-check
- cycle-detection
- inconsistency-localization
- ranking-synthesis

## Execution Guidance

1. Initialize ratings uniformly for all candidates
2. Run adaptive-pair-selection tactic until convergence or complete matrix
3. Run consistency-audit-loop to verify transitivity
4. If CR > 0.1, re-compare flagged pairs and recompute
5. Produce final ranking via ranking-synthesis

## Output Format

```yaml
ranking:
  - {rank: 1, candidate: "...", score: 0.95, ci: [0.91, 0.99]}
  - {rank: 2, candidate: "...", score: 0.82, ci: [0.77, 0.87]}
method: bradley-terry
consistency_ratio: 0.04
total_comparisons: 28
convergence_iterations: 3
```

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| adaptive-pair-selection | Iteratively select maximally informative pairs, execute comparisons, update ratings, and check convergence until ranking stabilizes. |
| consistency-audit-loop | Detect preference cycles, localize inconsistent judgments, request corrections, and recompute ratings until consistency threshold is met. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| ranking-synthesis | Produce the final ranking artifact from converged ratings and consistency report. |

<!-- END available-tables (generated) -->
