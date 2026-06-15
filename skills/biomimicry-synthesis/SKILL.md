---
name: biomimicry-synthesis
description: Synthesize all biomimicry outputs into a structured idea report. Integrate
  biological strategies, design principles, and technical solutions.
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (string)
dependencies:
  sops:
  - spawn-agent
---

# Biomimicry Synthesis

Synthesize all biomimicry outputs into a structured idea report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Synthesis requires integrating diverse outputs from multiple SOPs, identifying cross-cutting themes, resolving conflicts, and producing a coherent final report. Benefits from dedicated integrative attention.
