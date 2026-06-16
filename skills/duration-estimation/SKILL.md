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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
