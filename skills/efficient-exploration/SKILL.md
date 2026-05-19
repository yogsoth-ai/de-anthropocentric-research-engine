---
name: efficient-exploration
description: Strategy for large-N sparse pairwise comparison using TrueSkill, active learning, and rank centrality to rank 100+ candidates from limited comparisons.
used-by: pairwise-ranking
---

# Efficient Exploration

## Purpose

Produce reliable rankings when the candidate set is too large for complete comparison. Uses information-theoretic pair selection and sparse-matrix rating algorithms to converge quickly with minimal comparisons.

## When to use

- Candidate count N ≥ 100
- Complete comparison infeasible (budget << N(N-1)/2)
- Approximate ranking acceptable — top-k identification sufficient
- Speed/efficiency prioritized over perfect calibration

## Budget

| Resource | Allocation |
|----------|-----------|
| Comparisons | N×log(N) to 3N×log(N) |
| Iterations | 5-20 rounds of adaptive selection |
| Convergence target | Top-k stability ≥ 90% for 3 consecutive rounds |

## State Ledger

```yaml
candidates: []          # full candidate list
comparison_history: []  # [{pair, winner, confidence, round}]
ratings: {}             # candidate → {mu, sigma}
method: ""              # trueskill | bt-incomplete | rank-centrality
iteration: 0
budget_remaining: 0
convergence: {stable: false, score: 0.0, top_k_stable: false}
```

## Available Tactics

- **adaptive-pair-selection** — maximize information gain per comparison
- **consistency-audit-loop** — spot-check transitivity in top-k region

## Available SOPs

- pair-selector
- comparison-executor
- rating-update
- convergence-check
- cycle-detection
- ranking-synthesis

## Execution Guidance

1. Initialize all candidates with prior (mu=25, sigma=8.33 for TrueSkill)
2. Run adaptive-pair-selection with uncertainty-based pair selection
3. Prioritize comparisons that reduce uncertainty in top-k boundary
4. Check convergence every N/10 comparisons
5. When budget exhausted or converged, run ranking-synthesis
6. Optional: spot-check consistency in top-10 region

## Output Format

```yaml
ranking:
  - {rank: 1, candidate: "...", mu: 38.2, sigma: 1.4, ci: [35.4, 41.0]}
  - {rank: 2, candidate: "...", mu: 36.8, sigma: 1.6, ci: [33.6, 40.0]}
method: trueskill
total_comparisons: 847
budget_utilization: 0.92
top_10_stability: 0.96
convergence_round: 14
```
