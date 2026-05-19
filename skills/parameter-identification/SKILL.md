---
name: parameter-identification
description: Identify the key parameters/dimensions of a problem space. Produces a structured parameter list with value ranges for morphological analysis.
execution: subagent
prompt: ./prompt.md
input: system_description (string)
used-by: structural-deconstruction, morphological-exploration, combinatorial-creativity, systematic-enumeration
---

# Parameter Identification

Identify the key parameters/dimensions of a problem space.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Parameter identification requires systematic decomposition of a system into orthogonal dimensions. Benefits from focused analytical attention to ensure completeness and independence of parameters.
