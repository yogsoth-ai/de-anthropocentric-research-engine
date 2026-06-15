---
name: distribution-assignment
description: Assign probability distributions to uncertain parameters based on available
  evidence and domain knowledge.
execution: subagent
prompt: ./prompt.md
input: parameter_list, available_evidence
dependencies:
  sops:
  - spawn-agent
---

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one complete distribution assignment pass over a parameter list.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
