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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
