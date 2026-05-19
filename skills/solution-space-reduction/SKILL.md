---
name: solution-space-reduction
description: Apply CCA to remove inconsistent combinations
execution: subagent
prompt: ./prompt.md
input: matrix (object), consistency_judgments (array)
used-by: consistency-checking, cross-consistency-analysis, general-morphological-analysis
---

# Solution Space Reduction

Apply cross-consistency analysis to remove all configurations containing inconsistent pairs, producing a reduced solution space.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Space reduction requires systematic application of consistency constraints across the full matrix, computing which complete configurations survive filtering, and reporting reduction statistics.
