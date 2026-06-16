---
name: polarity-mapping
description: Map unresolvable tensions as Johnson polarities — 4 quadrants (positive/negative
  of each pole), early warnings, action steps for managing rather than solving.
execution: subagent
prompt: ./prompt.md
input: tension_pair (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Polarity Mapping

Map tensions that cannot be resolved, only managed.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one polarity map construction.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
