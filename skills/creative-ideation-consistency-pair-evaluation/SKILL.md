---
name: consistency-pair-evaluation
description: Evaluate pairwise value consistency (logical/empirical/normative)
execution: subagent
prompt: ./prompt.md
input: value_pairs (array)
dependencies:
  sops:
  - spawn-agent
---

# Consistency Pair Evaluation

Evaluate pairwise consistency of parameter-value combinations, classifying inconsistencies by type.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Consistency evaluation requires careful reasoning about whether two values from different parameters can coexist, considering logical constraints, empirical evidence, and normative conventions.
