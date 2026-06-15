---
name: scenario-synthesis
description: Comprehensive scenario analysis report synthesizing all scenario work
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: all scenario narratives, impact assessments, robustness scores, pivot triggers
output: comprehensive scenario portfolio report with strategic recommendations
dependencies:
  sops:
  - spawn-agent
---

# SOP: Scenario Synthesis

Compile all scenario analysis outputs into a comprehensive report with strategic recommendations, contingency plans, and monitoring framework.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
