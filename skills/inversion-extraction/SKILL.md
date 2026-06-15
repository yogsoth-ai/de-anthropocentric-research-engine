---
name: inversion-extraction
description: Extract constructive insights from worst solutions. Transform failure
  analysis into innovation directions.
execution: subagent
prompt: ./prompt.md
input: worst_solution (string), failure_analysis (string)
dependencies:
  sops:
  - spawn-agent
---

# Inversion Extraction

Extract constructive insights from worst solutions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Inversion extraction requires careful analytical reasoning to transform "why this is bad" into "what the good version implies." Benefits from dedicated focus to avoid superficial inversions and find deep structural insights.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
