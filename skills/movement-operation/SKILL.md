---
name: movement-operation
description: Extract constructive directions from PO provocations using 4 movement
  types (moment-to-moment, principle, focus difference, positive aspects).
execution: subagent
prompt: ./prompt.md
input: po_provocations (string)
dependencies:
  sops:
  - spawn-agent
---

# Movement Operation

Extract constructive directions from PO provocations (4 movement types).

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Movement requires holding each provocation in mind while systematically applying 4 distinct extraction lenses. Benefits from dedicated context that can fully explore each movement type without premature judgment.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
