---
name: cycle-detection
description: Scan a pairwise comparison matrix for preference cycles and compute transitivity metrics.
execution: subagent
prompt: ./prompt.md
input: comparison_matrix(object)
used-by: pairwise-ranking
---

# Cycle Detection

Scans a pairwise comparison matrix for preference cycles (A>B>C>A) and computes transitivity metrics. Identifies all minimal cycles and quantifies overall consistency.

## Execution

Runs as a subagent. Receives a comparison matrix, returns all detected cycles and transitivity scores.

## Why Subagent

Cycle detection requires graph traversal algorithms (Johnson's algorithm or DFS-based enumeration) applied to the preference digraph. Isolating this keeps algorithmic complexity out of the orchestrator.

## HARD-GATE

Output MUST contain a `cycles` array (empty if none found) and a numeric `transitivity_score` in [0, 1]. All reported cycles MUST be verifiable against the input matrix.
