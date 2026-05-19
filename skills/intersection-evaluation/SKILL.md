---
name: intersection-evaluation
description: Evaluate exploration status of each cell in a method×problem matrix, annotating as explored, partial, or unexplored.
execution: subagent
prompt: ./prompt.md
input: cross_matrix (object)
used-by: coverage-analysis, benchmark-sweep, method-problem-matrix
---

# Intersection Evaluation

Evaluate the exploration status of each cell in a method×problem matrix and prioritize unexplored intersections.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Evaluation requires careful assessment of each intersection's exploration depth, consulting literature and benchmarks. Benefits from focused context to maintain consistent evaluation criteria.
