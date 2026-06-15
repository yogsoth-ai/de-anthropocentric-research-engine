---
name: reframing-matrix
description: Reframe the problem from 4 professional perspectives to reveal what each
  discipline would focus on.
execution: subagent
prompt: ./prompt.md
input: problem_statement
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete reframing matrix (4 perspectives) for one problem.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
