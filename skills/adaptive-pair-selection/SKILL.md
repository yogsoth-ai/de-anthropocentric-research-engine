---
name: adaptive-pair-selection
description: Iteratively select maximally informative pairs, execute comparisons,
  update ratings, and check convergence until ranking stabilizes.
execution: tactic
dependencies:
  sops:
  - comparison-executor
  - convergence-check
  - pair-selector
  - rating-update
---

# Adaptive Pair Selection

Select the next comparison pair by information gain, execute the comparison, update ratings, and check for convergence. Repeats until the ranking stabilizes or the comparison budget is exhausted.

## Stages

1. **Select** — pair-selector identifies the pair whose comparison would most reduce uncertainty
2. **Compare** — comparison-executor produces a judgment with confidence and reasoning
3. **Update** — rating-update incorporates the new judgment into the rating model
4. **Check** — convergence-check determines if ranking has stabilized

Loop stages 1-4 until convergence or budget exhaustion.

## Available SOPs

| Stage | SOP | Input | Output |
|-------|-----|-------|--------|
| Select | pair-selector | current_ratings, comparison_history | next_pairs[] |
| Compare | comparison-executor | pair, context | judgment |
| Update | rating-update | judgment, current_ratings, method | updated_ratings |
| Check | convergence-check | rating_history | converged, stability_score |

## Execution Guidance

- Start with high-uncertainty pairs (largest sigma or most uncertain boundary)
- For small N: may complete all pairs in first pass, then focus on inconsistencies
- For large N: prioritize pairs near rank boundaries (positions k and k+1)
- Track comparison count against budget; exit gracefully if budget hit
- Pass full rating_history to convergence-check (not just latest snapshot)

## Minimum Yield

- Global ranking + confidence intervals + convergence curve
- Global ranking with confidence intervals for each position
- Convergence curve showing stability score over iterations
- Comparison log with all judgments made

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| comparison-executor | Execute a pairwise comparison between two candidates, producing a judgment with winner, confidence, and reasoning. |
| convergence-check | Evaluate whether the ranking has stabilized by analyzing rating history and computing stability metrics. |
| pair-selector | Select the next comparison pairs that maximize information gain given current ratings and comparison history. |
| rating-update | Incorporate a new judgment into the rating model and return updated ratings for all candidates. |

<!-- END available-tables (generated) -->
