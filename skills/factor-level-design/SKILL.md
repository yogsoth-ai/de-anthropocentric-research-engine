---
name: factor-level-design
description: Identify factors and their levels for a problem, then design an experiment matrix for systematic exploration.
execution: subagent
prompt: ./prompt.md
input: problem (string)
used-by: factorial-ideation, gap-driven-generation
---

# Factor-Level Design

Identify key factors, define their levels, and design a factorial experiment matrix for systematic exploration.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Factorial design requires careful identification of independent factors and meaningful levels. Benefits from dedicated analytical context to avoid confounding and ensure orthogonality.
