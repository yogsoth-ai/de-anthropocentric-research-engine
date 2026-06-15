---
name: structural-synthesis
description: Synthesize all structural transformation outputs into a coherent, ranked
  idea report with lineage tracking.
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (string)
dependencies:
  sops:
  - spawn-agent
---

# Structural Synthesis

Synthesize all structural transformation outputs into a final report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Synthesis requires integrating outputs from multiple diverse operations, deduplicating, clustering, and ranking. Benefits from dedicated context that can hold all intermediate results simultaneously for cross-referencing.
