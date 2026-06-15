---
name: wickedness-scoring
description: Score a problem against Rittel's 10 criteria to determine if it is tame,
  complex, or wicked.
execution: subagent
prompt: ./prompt.md
input: problem_description, context
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete wickedness assessment (10-criterion scoring + classification).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
