---
name: springboard-launch
description: Convert analogy insights into concrete feasible solutions. Transform
  abstract connections into actionable mechanisms.
execution: subagent
prompt: ./prompt.md
input: analogy_insights (string)
dependencies:
  sops:
  - spawn-agent
---

# Springboard Launch

Convert analogy insights into concrete feasible solutions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Springboard launch requires shifting from abstract/metaphorical thinking to concrete engineering. Benefits from dedicated focus on feasibility and mechanism design without the pull of further abstraction.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
