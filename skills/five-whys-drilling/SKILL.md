---
name: five-whys-drilling
description: Iterative "Why?" questioning (5+ levels) to drill from surface phenomenon to actionable root cause. Each level verified against evidence.
execution: subagent
prompt: ./prompt.md
input: surface_phenomenon (string), context (string)
used-by: root-cause-drilling
---

# Five Whys Drilling

Iterative root cause analysis via successive "Why?" questions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one 5-Whys drilling pass.
