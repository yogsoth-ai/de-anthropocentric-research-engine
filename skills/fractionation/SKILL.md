---
name: fractionation
description: Split concepts into smaller units and recombine them differently to produce novel structures.
execution: subagent
prompt: ./prompt.md
input: concept (string)
used-by: lateral-thinking, concept-fan, concept-hierarchy
---

# Fractionation

Split concepts into smaller units, recombine differently.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Fractionation requires holding a concept's fragments in mind while exploring all possible recombinations. Benefits from dedicated context that can systematically enumerate fragment combinations without losing track.
