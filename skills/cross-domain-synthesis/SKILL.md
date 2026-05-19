---
name: cross-domain-synthesis
description: Synthesize all cross-domain findings into a structured idea report. Integrates outputs from all strategies and SOPs.
execution: subagent
prompt: ./prompt.md
input: all_intermediate_outputs (string)
used-by: cross-domain-discovery, facet-bisociation, analogical-transfer, random-stimulus-entry, forced-bridge-construction, design-by-analogy
---

# Cross-Domain Synthesis

Synthesize all cross-domain findings into a structured idea report.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Synthesis requires integrating diverse outputs from multiple strategies and SOPs into a coherent report. Benefits from a fresh perspective that can identify patterns across all intermediate outputs without being anchored to any single strategy's framing.
