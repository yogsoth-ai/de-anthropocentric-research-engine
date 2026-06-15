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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
