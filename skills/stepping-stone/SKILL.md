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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
