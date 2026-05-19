---
name: practitioner-hat
description: Engineer perspective — assess buildability, cost, timeline, and integration challenges.
execution: subagent
prompt: ./prompt.md
input: solution (string)
used-by: perspective-forcing, role-based-ideation, perspective-rotation
---

# Practitioner Hat

Engineer perspective: assess buildability.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Engineering assessment requires systematic evaluation of implementation details that benefits from focused, uninterrupted analysis.
