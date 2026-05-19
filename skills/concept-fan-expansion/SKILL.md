---
name: concept-fan-expansion
description: Expand concept fan from purpose through concepts to directions to ideas (de Bono Concept Fan).
execution: subagent
prompt: ./prompt.md
input: purpose_statement (string)
used-by: lateral-thinking, concept-fan, concept-hierarchy
---

# Concept Fan Expansion

Expand concept fan from purpose through concepts to ideas.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Concept fan expansion requires maintaining multiple abstraction levels simultaneously and generating ideas at each level. Benefits from dedicated context that can hold the full fan structure while exploring each branch.
