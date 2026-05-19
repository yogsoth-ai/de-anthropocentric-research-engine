---
name: path-generation
description: Generate combination paths through consistent space
execution: subagent
prompt: ./prompt.md
input: reduced_space (object)
used-by: zwicky-box-construction, general-morphological-analysis, parameter-variation
---

# Path Generation

Generate combination paths through the consistent solution space, prioritizing unexplored and novel configurations.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Path generation requires strategic traversal of the reduced solution space, selecting configurations that maximize coverage, novelty, and diversity rather than random sampling.
