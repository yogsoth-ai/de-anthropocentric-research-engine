---
name: movement-operation
description: Extract constructive directions from PO provocations using 4 movement types (moment-to-moment, principle, focus difference, positive aspects).
execution: subagent
prompt: ./prompt.md
input: po_provocations (string)
used-by: lateral-thinking, provocation-and-movement, movement-extraction, six-hats-ideation
---

# Movement Operation

Extract constructive directions from PO provocations (4 movement types).

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Movement requires holding each provocation in mind while systematically applying 4 distinct extraction lenses. Benefits from dedicated context that can fully explore each movement type without premature judgment.
