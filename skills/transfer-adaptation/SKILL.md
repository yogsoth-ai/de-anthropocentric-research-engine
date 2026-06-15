---
name: transfer-adaptation
description: Adapt transferred principle to target problem constraints. Produces concrete
  adapted solutions from abstract principles.
execution: subagent
prompt: ./prompt.md
input: abstract_principle (string), target_problem (string)
dependencies:
  sops:
  - spawn-agent
---

# Transfer Adaptation

Adapt transferred principle to target problem constraints.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Transfer adaptation requires careful reasoning about how abstract mechanisms instantiate in a new domain. Benefits from dedicated attention to constraint satisfaction and risk identification without being distracted by the broader creative process.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
