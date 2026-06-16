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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
