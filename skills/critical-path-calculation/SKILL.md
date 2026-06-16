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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
