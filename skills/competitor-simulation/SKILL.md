---
name: competitor-simulation
description: Competitor perspective — design strategies to defeat this solution, then use attack vectors to improve it.
execution: subagent
prompt: ./prompt.md
input: solution (string)
used-by: perspective-forcing, role-based-ideation
---

# Competitor Simulation

Competitor perspective: how to defeat this solution.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Competitive analysis requires adversarial thinking that benefits from dedicated context to avoid contaminating constructive ideation.
