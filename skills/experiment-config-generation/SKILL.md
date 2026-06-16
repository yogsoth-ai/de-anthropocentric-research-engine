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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
