---
name: dominance-check
description: Identify dominated and non-dominated alternatives in a score matrix using Pareto dominance.
execution: subagent
prompt: ./prompt.md
input: score_matrix (object)
used-by: multi-criteria-scoring
---

# Dominance Check

Identify dominated alternatives (where another alternative is no worse on all criteria and strictly better on at least one) and non-dominated alternatives (Pareto front) in the scoring matrix.

## Execution

Subagent receives the scoring matrix, performs pairwise dominance relationship checks, and outputs the dominance graph and classification results.

## Why Subagent

Dominance checking requires O(n^2 x m) pairwise comparisons, logic-intensive but self-contained, suitable for independent execution.

## HARD-GATE

Each "dominated" determination must specify the dominating alternative, and verify the strict definition of dominance (no worse on all criteria + strictly better on at least one).
