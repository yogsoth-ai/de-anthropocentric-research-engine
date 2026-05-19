---
name: experiment-config-generation
description: "SOP: generate executable experiment configuration files"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - factor-level-design
shared:
  - implementation-planning
input: "Design matrix + environment spec + seed protocol + metric definitions"
output: "Executable experiment configuration file set (YAML/JSON)"
---

# SOP: Experiment Config Generation

Synthesize all experiment design elements (design matrix, environment, seeds, metrics) into directly executable configuration files, enabling seamless transition from design to execution.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Config generation requires integrating outputs from multiple upstream SOPs, transforming abstract experiment designs into concrete executable specifications — involves format conversion and consistency validation.
