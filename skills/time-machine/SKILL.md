---
name: time-machine
description: Temporal projection — view a solution from future/past time horizons
  to generate temporally-informed insights.
execution: subagent
prompt: ./prompt.md
input: solution (string), time_scale (string)
dependencies:
  sops:
  - spawn-agent
---

# Time Machine

Temporal projection: view from future/past.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Temporal projection requires sustained imaginative reasoning across multiple time horizons, benefiting from dedicated context free of present-bias.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
