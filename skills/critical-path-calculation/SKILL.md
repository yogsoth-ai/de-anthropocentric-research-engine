---
name: critical-path-calculation
description: CPM forward/backward pass with float calculation to identify the critical
  path
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: activity list with dependencies and PERT duration estimates
output: critical path, float table, earliest/latest start-finish times
dependencies:
  sops:
  - spawn-agent
---

# SOP: Critical Path Calculation

Perform CPM forward and backward pass to identify the critical path and calculate float for all activities.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
