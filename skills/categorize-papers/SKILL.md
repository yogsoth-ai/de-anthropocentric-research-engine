---
name: categorize-papers
description: Cluster papers by theme, method, or timeline. Produces natural groupings
  from a paper collection. Used by scoping-survey and narrative-review.
execution: subagent
prompt: ./prompt.md
input: paper_list (string)
dependencies:
  sops:
  - spawn-agent
---

# Categorize Papers

Cluster papers by theme/method/timeline into natural groupings.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Categorization requires holding the entire paper collection in context simultaneously to identify patterns and groupings. Subagent provides dedicated space for this comparative analysis.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
