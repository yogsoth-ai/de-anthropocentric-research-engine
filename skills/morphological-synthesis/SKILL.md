---
name: morphological-synthesis
description: Synthesize all morphological exploration outputs
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (object)
dependencies:
  sops:
  - spawn-agent
---

# Morphological Synthesis

Synthesize all intermediate morphological exploration outputs into a structured final report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Morphological synthesis requires integrating matrix construction, CCA results, path generation, white-space analysis, and combination evaluations into a coherent report with actionable recommendations.
