---
name: white-space-mapping
description: Feature cross-matrix construction and blank area identification for patent
  opportunity mapping
execution: subagent
prompt: ./prompt.md
input: feature_dimensions, existing_patents
dependencies:
  sops:
  - spawn-agent
---

# White Space Mapping

Constructs multi-dimensional feature cross-matrices from patent data and identifies blank areas representing unprotected technology combinations.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
