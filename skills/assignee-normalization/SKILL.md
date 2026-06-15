---
name: assignee-normalization
description: Standardize assignee names and identify corporate group affiliations
  across patent offices
execution: subagent
prompt: ./prompt.md
input: raw_assignee_list
dependencies:
  sops:
  - spawn-agent
---

# Assignee Normalization

Standardizes patent assignee names across different patent offices and identifies corporate group affiliations (parent companies, subsidiaries, acquired entities).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
