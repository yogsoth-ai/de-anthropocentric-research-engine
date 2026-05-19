---
name: enumeration-synthesis
description: Synthesize all systematic enumeration outputs into a structured idea report with prioritized recommendations.
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (object)
used-by: systematic-enumeration, benchmark-sweep, method-problem-matrix, ablation-brainstorm, failure-taxonomy, factorial-ideation
---

# Enumeration Synthesis

Synthesize all intermediate outputs from systematic enumeration into a coherent, prioritized idea report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Synthesis requires integrating diverse outputs (matrices, ablation results, failure taxonomies, factorial designs) into a coherent narrative. Benefits from dedicated context to hold all inputs simultaneously.
