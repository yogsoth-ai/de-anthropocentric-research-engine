---
name: quality-assessment
description: Methodological rigor scoring for papers — evaluates bias risk, reproducibility,
  sample adequacy using established frameworks. Used by systematic-survey.
execution: subagent
prompt: ./prompt.md
input: paper_details (string)
dependencies:
  sops:
  - spawn-agent
---

# Quality Assessment

Evaluate research rigor using established quality assessment frameworks.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Quality assessment requires applying consistent criteria across multiple papers while maintaining objectivity. Dedicated context ensures the assessment framework is applied uniformly.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
