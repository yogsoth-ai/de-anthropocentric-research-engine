---
name: sensitivity-synthesis
description: Synthesize all sensitivity analysis results into a coherent report with prioritized recommendations.
execution: subagent
prompt: ./prompt.md
input: screening_results, decomposition_results, assumption_criticality, propagation_results, decision_sensitivity
used-by: sensitivity-analysis
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete synthesis report across all sensitivity analysis components.
