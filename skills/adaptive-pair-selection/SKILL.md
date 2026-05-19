---
name: adaptive-pair-selection
description: Iteratively select maximally informative pairs, execute comparisons, update ratings, and check convergence until ranking stabilizes.
execution: tactic
used-by: pairwise-ranking
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
