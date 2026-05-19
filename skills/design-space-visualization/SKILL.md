---
name: design-space-visualization
description: Generate structured description of design space
execution: subagent
prompt: ./prompt.md
input: matrix (object), coverage_status (object)
used-by: design-space-mapping
---

# Design Space Visualization

Generate a structured textual description of the design space showing explored, unexplored, and infeasible regions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Design space visualization requires synthesizing matrix structure, coverage data, and white-space analysis into a coherent spatial description that communicates opportunity zones.
