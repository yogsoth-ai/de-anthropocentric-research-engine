---
name: abstraction-to-design
description: Abstract biological principle to design principle. Bridge from biology
  to engineering.
execution: subagent
prompt: ./prompt.md
input: biological_strategy (string)
dependencies:
  sops:
  - spawn-agent
---

# Abstraction to Design

Abstract biological principle to design principle.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Abstraction requires careful removal of biological specifics while preserving the functional essence, then mapping to engineering design space. Benefits from focused analytical attention to avoid over-literal or over-abstract transfers.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
