---
name: assumption-surfacing
description: Enumerate implicit assumptions in a problem statement or existing solution.
  Produces categorized assumption inventory (physical, social, temporal, economic,
  technical).
execution: subagent
prompt: ./prompt.md
input: target_description (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Assumption Surfacing

Enumerate implicit assumptions in a problem or solution.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Assumption surfacing requires systematic examination of every element in a problem statement, questioning what is taken for granted. Benefits from dedicated analytical focus without the distraction of solution generation.
