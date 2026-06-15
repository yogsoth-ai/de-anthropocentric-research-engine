---
name: normalization
description: Normalize a score matrix using a specified method to make scores comparable
  across criteria.
execution: subagent
prompt: ./prompt.md
input: score_matrix (object), method (string)
dependencies:
  sops:
  - spawn-agent
---

# Normalization

Normalize the scoring matrix to make scores with different units and scales comparable across criteria.

## Execution

Subagent receives the raw scoring matrix and normalization method, outputs the normalized matrix.

## Why Subagent

Normalization involves mathematical transformations and direction handling; independent verification of transformation correctness is needed to avoid direction errors causing rank reversals.

## HARD-GATE

All normalized values must be in the [0, 1] range, with max-direction criteria having optimal value of 1, and min-direction criteria having optimal value of 1 (after inversion).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
