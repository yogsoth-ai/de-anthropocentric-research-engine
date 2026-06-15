---
name: destruction-synthesis
description: Synthesize all assumption destruction outputs into structured destructive
  innovation report.
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (string), campaign_context (string)
dependencies:
  sops:
  - spawn-agent
---

# Destruction Synthesis

Synthesize all assumption destruction outputs.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Destruction synthesis requires integrating diverse outputs (perturbation results, reversals, inversions, sacred cows, constructive alternatives) into a coherent innovation report. Benefits from dedicated synthesis attention.
