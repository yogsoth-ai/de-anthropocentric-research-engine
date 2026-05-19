---
name: reviewer2-hat
description: Hostile reviewer perspective — find fatal flaws, logical gaps, and missing evidence in a solution.
execution: subagent
prompt: ./prompt.md
input: solution (string)
used-by: perspective-forcing, role-based-ideation, perspective-rotation
---

# Reviewer 2 Hat

Hostile reviewer perspective: find fatal flaws.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Hostile reviewing requires sustained adversarial reasoning that benefits from dedicated attention and prevents contamination of the constructive ideation context.
