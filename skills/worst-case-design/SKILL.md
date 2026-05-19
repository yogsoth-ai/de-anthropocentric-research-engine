---
name: worst-case-design
description: Design the worst possible solution. Deliberate failure engineering to reveal hidden constraints and inversion opportunities.
execution: subagent
prompt: ./prompt.md
input: problem (string), constraints (string)
used-by: inversion-protocol, reverse-brainstorming, worst-method-inversion
---

# Worst-Case Design

Design the worst possible solution.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Worst-case design requires creative perversity — deliberately optimizing for failure across multiple dimensions. Benefits from dedicated focus to produce genuinely terrible solutions (not just mediocre ones) that yield rich inversion material.
