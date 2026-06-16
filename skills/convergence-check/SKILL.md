---
name: convergence-check
description: Evaluate whether the ranking has stabilized by analyzing rating history
  and computing stability metrics.
execution: subagent
prompt: ./prompt.md
input: rating_history(array)
dependencies:
  sops:
  - spawn-agent
---

# Convergence Check

Evaluates whether the current ranking has converged by analyzing the trajectory of ratings over recent iterations. Computes stability metrics and determines if further comparisons would meaningfully change the ranking.

## Execution

Runs as a subagent. Receives the full rating history and returns convergence status with metrics.

## Why Subagent

Convergence assessment requires analyzing trends across multiple snapshots and applying statistical tests. Isolating this prevents the orchestrator from needing to hold the full history in working memory.

## HARD-GATE

Output MUST contain a boolean `converged` field and a numeric `stability_score` in [0, 1]. If converged=false, MUST include `recommendation` for what to do next.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
