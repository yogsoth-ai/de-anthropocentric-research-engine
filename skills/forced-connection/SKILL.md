---
name: forced-connection
description: Force connection between two unrelated concepts. Deliberately construct
  bridging paths where no natural connection exists.
execution: subagent
prompt: ./prompt.md
input: concept_a (string), concept_b (string)
dependencies:
  sops:
  - spawn-agent
---

# Forced Connection

Force connection between two unrelated concepts.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Forced connection requires sustained creative pressure — the subagent must resist declaring "no connection exists" and instead push through discomfort to find bridging paths. Benefits from dedicated context that commits fully to the bridging process.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
