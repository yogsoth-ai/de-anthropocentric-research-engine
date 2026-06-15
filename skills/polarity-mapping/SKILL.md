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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
