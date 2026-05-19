---
name: critical-path-identification
description: Identify which input uncertainties contribute most to output uncertainty and compute EVPI for research prioritization.
execution: subagent
prompt: ./prompt.md
input: propagation_results, input_output_relationships
used-by: uncertainty-propagation, decision-sensitivity
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete critical path analysis (importance ranking, EVPI computation, recommendations).
