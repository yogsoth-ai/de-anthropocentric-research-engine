---
name: disagreement-visualization
description: Produce a structured disagreement map showing clusters, arguments, and
  fault lines.
execution: subagent
prompt: ./prompt.md
input: clusters[], arguments[]
dependencies:
  sops:
  - spawn-agent
---

# Disagreement Visualization

Produce a structured disagreement map that shows the topology of disagreement: which clusters exist, what arguments support each, where the fault lines lie, and what type of disagreement separates them.

## Execution

Spawn a subagent that takes clusters and their extracted arguments, then produces a structured map showing relationships, tensions, and potential bridges.

## Why Subagent

- Visualization synthesis requires integrating multiple cluster analyses
- Fault line identification is a distinct analytical step
- Output is the final deliverable of disagreement-mapping tactic

## HARD-GATE

Output MUST contain: `disagreement_map` with clusters, fault_lines (at least 1 if multiple clusters exist), and fault_line_types. Map must cover ALL input clusters.
