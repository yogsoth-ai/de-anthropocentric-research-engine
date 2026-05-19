---
name: constraint-injection
description: Inject artificial constraints to force creative divergence. Generates and applies constraints (resource, time, material, audience, scale) to existing ideas to produce variants.
execution: subagent
prompt: ./prompt.md
input: problem_or_idea (string), constraint_type (string)
used-by: perspective-forcing, lateral-thinking, structural-deconstruction, morphological-exploration
---

# Constraint Injection

Inject artificial constraints to force creative divergence.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Constraint injection requires generating appropriate constraints AND then reasoning about how to satisfy the problem under those constraints. The two-phase process benefits from dedicated attention.
