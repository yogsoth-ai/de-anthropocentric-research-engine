---
name: level-specification
description: Determine appropriate levels for each experimental factor
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: factor list with types and ranges
output: specified levels for each factor with justification
dependencies:
  sops:
  - spawn-agent
---

# SOP: Level Specification

Determine the specific values (levels) at which each factor will be tested, including spacing strategy and justification.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
