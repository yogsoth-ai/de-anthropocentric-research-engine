---
name: stepping-stone
description: Use impractical ideas as stepping stones to reach practical solutions
  (de Bono Stepping Stone technique).
execution: subagent
prompt: ./prompt.md
input: impractical_ideas (string)
dependencies:
  sops:
  - spawn-agent
---

# Stepping Stone

Use impractical ideas as stepping stones to practical ones.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Stepping stone requires holding an impractical idea without rejecting it, then finding the bridge to practicality. Benefits from dedicated context that can resist the urge to dismiss and instead explore the connection path.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
