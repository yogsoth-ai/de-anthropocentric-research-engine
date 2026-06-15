---
name: duration-estimation
description: Three-point PERT estimation for implementation activities
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: sequenced activity list with dependency information
output: PERT estimates (optimistic, most likely, pessimistic, expected, variance)
  per activity
dependencies:
  sops:
  - spawn-agent
---

# SOP: Duration Estimation

Estimate activity durations using three-point PERT methodology.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
