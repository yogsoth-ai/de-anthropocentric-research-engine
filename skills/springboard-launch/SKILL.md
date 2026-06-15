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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
