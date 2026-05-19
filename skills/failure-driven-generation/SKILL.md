---
name: failure-driven-generation
description: Generate targeted solutions for each identified failure mode, ensuring every failure has at least one proposed mitigation.
execution: subagent
prompt: ./prompt.md
input: failure_modes (array)
used-by: failure-taxonomy, gap-driven-generation
---

# Failure-Driven Generation

Generate solutions that specifically target identified failure modes.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Solution generation for failures requires creative thinking constrained by specific failure characteristics. Benefits from dedicated context that can deeply engage with each failure mode's mechanics.
