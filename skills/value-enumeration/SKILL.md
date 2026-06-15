---
name: value-enumeration
description: Enumerate 3-5 values per parameter including extremes
execution: subagent
prompt: ./prompt.md
input: parameter_list (array)
dependencies:
  sops:
  - spawn-agent
---

# Value Enumeration

Enumerate 3-5 meaningful values per parameter, ensuring coverage of boundary and extreme values.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Value enumeration requires creative thinking about each parameter's range, including non-obvious extremes and boundary values that expand the solution space beyond conventional options.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
