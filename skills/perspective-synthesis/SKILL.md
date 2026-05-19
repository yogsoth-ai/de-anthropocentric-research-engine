---
name: perspective-synthesis
description: Synthesize all perspective outputs into a structured multi-perspective idea report.
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (string)
used-by: perspective-forcing, role-based-ideation, temporal-projection, stakeholder-simulation, constraint-driven-ideation, perspective-rotation
---

# Perspective Synthesis

Synthesize all perspective outputs into structured report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Synthesis requires holding all perspective outputs simultaneously and finding patterns across them, benefiting from a fresh context that can see the forest rather than individual trees.
