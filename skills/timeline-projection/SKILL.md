---
name: timeline-projection
description: Extrapolate research landscape timelines using trend analysis and milestone
  projection
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: current state assessment, trend data, milestone markers, planning horizon
output: timeline with projected milestones, confidence intervals, and inflection points
dependencies:
  sops:
  - spawn-agent
---

# SOP: Timeline Projection

Extrapolate how the research landscape evolves over time by projecting key milestones, trend inflection points, and phase transitions. Uses historical trend data and analogical reasoning to estimate when critical thresholds will be crossed.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
