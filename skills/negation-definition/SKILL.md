---
name: negation-definition
description: Define strongest plausible alternatives (negations) for each assumption
  to enable perturbation analysis.
execution: subagent
prompt: ./prompt.md
input: assumption_list
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete negation definition pass over an assumption list.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
