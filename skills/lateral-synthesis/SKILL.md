---
name: lateral-synthesis
description: Synthesize all lateral thinking intermediate outputs into a structured idea report.
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (string)
used-by: lateral-thinking, provocation-and-movement, random-entry, concept-fan, challenge-operation, six-hats-ideation
---

# Lateral Synthesis

Synthesize all lateral thinking outputs into a structured report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Synthesis requires reviewing all intermediate outputs from multiple SOPs and tactics, identifying patterns, resolving conflicts, and producing a coherent final report. Benefits from dedicated context that can hold all outputs simultaneously.
