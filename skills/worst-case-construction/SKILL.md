---
name: worst-case-construction
description: Construct extreme but plausible worst-case scenarios for stress testing
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: vulnerability drivers, failure dimensions, compound combination guidance
output: extreme scenario with breaking points, failure cascades, and recovery assessment
dependencies:
  sops:
  - spawn-agent
---

# SOP: Worst-Case Construction

Construct extreme but plausible worst-case scenarios that maximally stress the research approach. Identify breaking points, failure cascades, and recovery possibilities.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
