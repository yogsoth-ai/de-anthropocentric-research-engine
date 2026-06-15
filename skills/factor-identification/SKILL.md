---
name: factor-identification
description: Identify independent, dependent, and control variables for an experiment
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: hypothesis, system description, prior work
output: structured factor list with classifications
dependencies:
  sops:
  - spawn-agent
---

# SOP: Factor Identification

Identify all independent variables (factors to manipulate), dependent variables (outcomes to measure), and control variables (confounds to hold constant) for the experiment.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
