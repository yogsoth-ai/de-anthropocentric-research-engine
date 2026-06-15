---
name: parameter-enumeration
description: Enumerate possible values for each uncertainty driver using MECE principles
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: validated driver list, value count guidance (2-4 per driver)
output: complete Zwicky Box (driver × value matrix) with value descriptions
dependencies:
  sops:
  - spawn-agent
---

# SOP: Parameter Enumeration

Enumerate the possible future states (values) for each identified uncertainty driver. Values must be mutually exclusive and collectively exhaustive (MECE) within each driver dimension.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
