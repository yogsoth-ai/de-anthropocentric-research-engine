---
name: scenario-driver-identification
description: Identify key uncertainty drivers using PESTEL framework scanning
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: research context, planning horizon, domain constraints
output: ranked list of 5-8 uncertainty drivers with impact and uncertainty scores
dependencies:
  sops:
  - spawn-agent
---

# SOP: Scenario Driver Identification

Identify the key uncertainty drivers that could shift the research landscape within the planning horizon. Uses PESTEL (Political, Economic, Social, Technological, Environmental, Legal) framework to ensure comprehensive coverage.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
