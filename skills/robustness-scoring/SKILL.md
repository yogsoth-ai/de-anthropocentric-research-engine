---
name: robustness-scoring
description: Compute robustness index across scenarios with sensitivity analysis
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: compiled impact assessment matrix, scenario probabilities, weighting preferences
output: robustness index (0-100), sensitivity analysis, pivot triggers
dependencies:
  sops:
  - spawn-agent
---

# SOP: Robustness Scoring

Compute an overall robustness index for the research approach across all evaluated scenarios. Perform sensitivity analysis and identify pivot triggers.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
