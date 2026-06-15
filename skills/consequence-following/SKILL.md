---
name: consequence-following
description: Follow a provocation's logical consequences step by step to extract viable
  insights and new research directions.
execution: subagent
prompt: ./prompt.md
input: provocation_statement
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete consequence chain (3-5 steps) for one provocation.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
