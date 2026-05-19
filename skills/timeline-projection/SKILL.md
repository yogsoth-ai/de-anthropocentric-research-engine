---
name: timeline-projection
description: "Extrapolate research landscape timelines using trend analysis and milestone projection"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - temporal-scenario
input: current state assessment, trend data, milestone markers, planning horizon
output: timeline with projected milestones, confidence intervals, and inflection points
---

# SOP: Timeline Projection

Extrapolate how the research landscape evolves over time by projecting key milestones, trend inflection points, and phase transitions. Uses historical trend data and analogical reasoning to estimate when critical thresholds will be crossed.

Subagent — spawned via subagent-spawning/spawn-agent skill.
