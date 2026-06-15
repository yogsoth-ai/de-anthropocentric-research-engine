---
name: experiment-config-generation
description: 'SOP: generate executable experiment configuration files'
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
shared:
- implementation-planning
input: Design matrix + environment spec + seed protocol + metric definitions
output: Executable experiment configuration file set (YAML/JSON)
dependencies:
  sops:
  - spawn-agent
---

# SOP: Experiment Config Generation

Synthesize all experiment design elements (design matrix, environment, seeds, metrics) into directly executable configuration files, enabling seamless transition from design to execution.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Config generation requires integrating outputs from multiple upstream SOPs, transforming abstract experiment designs into concrete executable specifications — involves format conversion and consistency validation.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
