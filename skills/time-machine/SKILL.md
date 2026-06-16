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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
