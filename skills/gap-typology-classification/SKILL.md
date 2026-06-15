---
name: gap-typology-classification
description: Classify gaps using Miles 7-type taxonomy (theoretical, methodological,
  empirical, population, practical, knowledge void, evidence gap).
execution: subagent
prompt: ./prompt.md
input: gap_description (string), evidence (string)
dependencies:
  sops:
  - spawn-agent
---

# Gap Typology Classification

Classify research gaps by type using established taxonomies.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one gap classification pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
