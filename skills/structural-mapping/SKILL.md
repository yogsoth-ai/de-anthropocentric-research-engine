---
name: structural-mapping
description: Map source→target structural correspondences. Identifies corresponding,
  missing, and extra elements between domains.
execution: subagent
prompt: ./prompt.md
input: source_structure (string), target_domain (string)
dependencies:
  sops:
  - spawn-agent
---

# Structural Mapping

Map source→target structural correspondences.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Structure-mapping requires systematic alignment of relational systems, tracking correspondences at multiple levels simultaneously. Benefits from dedicated working memory to maintain the full mapping table.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
