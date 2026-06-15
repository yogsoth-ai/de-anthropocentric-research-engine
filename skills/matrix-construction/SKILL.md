---
name: matrix-construction
description: Build n-dimensional morphological matrix
execution: subagent
prompt: ./prompt.md
input: parameters (array), values (object)
dependencies:
  sops:
  - spawn-agent
---

# Matrix Construction

Build an n-dimensional morphological matrix from parameters and their enumerated values.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Matrix construction requires careful organization of multi-dimensional data, computing combination counts, and presenting the matrix in a format suitable for downstream CCA and path generation.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
