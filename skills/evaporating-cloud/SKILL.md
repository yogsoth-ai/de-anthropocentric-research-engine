---
name: evaporating-cloud
description: Model conflicts as Goldratt's Evaporating Cloud — expose hidden assumptions
  behind opposing needs to dissolve the conflict.
execution: subagent
prompt: ./prompt.md
input: opposing_needs (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Evaporating Cloud

Dissolve conflicts by exposing hidden assumptions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one evaporating cloud construction.
