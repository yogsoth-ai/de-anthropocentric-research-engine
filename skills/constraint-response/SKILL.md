---
name: constraint-response
description: Generate creative solutions under extreme constraints — no "impossible" allowed, find a way.
execution: subagent
prompt: ./prompt.md
input: constraint (string), problem (string)
used-by: perspective-forcing, constraint-driven-ideation, constraint-protocol
---

# Constraint Response

Generate creative solutions under extreme constraints.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Constraint-forced creativity requires sustained divergent thinking under pressure, benefiting from dedicated context that fully commits to the constraint.
