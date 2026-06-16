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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
