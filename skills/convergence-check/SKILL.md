---
name: convergence-check
description: Evaluate whether the ranking has stabilized by analyzing rating history and computing stability metrics.
execution: subagent
prompt: ./prompt.md
input: rating_history(array)
used-by: pairwise-ranking
---

# Convergence Check

Evaluates whether the current ranking has converged by analyzing the trajectory of ratings over recent iterations. Computes stability metrics and determines if further comparisons would meaningfully change the ranking.

## Execution

Runs as a subagent. Receives the full rating history and returns convergence status with metrics.

## Why Subagent

Convergence assessment requires analyzing trends across multiple snapshots and applying statistical tests. Isolating this prevents the orchestrator from needing to hold the full history in working memory.

## HARD-GATE

Output MUST contain a boolean `converged` field and a numeric `stability_score` in [0, 1]. If converged=false, MUST include `recommendation` for what to do next.
