---
name: polarity-mapping
description: Map unresolvable tensions as Johnson polarities — 4 quadrants (positive/negative
  of each pole), early warnings, action steps for managing rather than solving.
execution: subagent
prompt: ./prompt.md
input: tension_pair (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Polarity Mapping

Map tensions that cannot be resolved, only managed.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one polarity map construction.
