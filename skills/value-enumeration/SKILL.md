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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
