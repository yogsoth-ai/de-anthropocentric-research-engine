---
name: direct-analogy-generation
description: Find direct analogies from nature/tech/society that share structural
  properties with the problem. Produces analogy list with structural mappings.
execution: subagent
prompt: ./prompt.md
input: problem (string)
dependencies:
  sops:
  - spawn-agent
---

# Direct Analogy Generation

Find direct analogies from nature, technology, and society.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Direct analogy generation requires broad cross-domain knowledge search and careful structural mapping. Benefits from dedicated focus on finding non-obvious parallels without premature solution generation.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
