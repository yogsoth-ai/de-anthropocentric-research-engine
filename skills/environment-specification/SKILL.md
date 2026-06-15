---
name: environment-specification
description: 'SOP: define complete experiment environment specification'
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
shared:
- implementation-planning
input: Experiment design + hardware requirements + software dependencies
output: Complete environment spec (hardware/software/data/configuration)
dependencies:
  sops:
  - spawn-agent
---

# SOP: Environment Specification

Define the complete experiment runtime environment specification including hardware, software, data, and configuration to ensure experiments can be precisely reproduced across different times and locations.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Environment specification requires systematically enumerating all factors that could affect experiment results — from GPU model to library versions to OS settings — demanding meticulous checklist-style work.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
