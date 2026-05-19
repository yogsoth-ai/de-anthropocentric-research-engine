---
name: ablation-component-mapping
description: "Map system architecture to ablatable units for ablation studies"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - ablation-design
input: system architecture description, component list
output: ablation map with dependencies and removal strategies
---

# SOP: Ablation Component Mapping

Map the system architecture to a set of ablatable units, identifying dependencies, removal strategies, and expected impact for each component.

Subagent — spawned via subagent-spawning/spawn-agent skill.
