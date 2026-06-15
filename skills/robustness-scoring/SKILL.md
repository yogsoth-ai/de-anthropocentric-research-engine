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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
