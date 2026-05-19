---
name: scenario-synthesis
description: "Comprehensive scenario analysis report synthesizing all scenario work"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - scenario-planning
input: all scenario narratives, impact assessments, robustness scores, pivot triggers
output: comprehensive scenario portfolio report with strategic recommendations
---

# SOP: Scenario Synthesis

Compile all scenario analysis outputs into a comprehensive report with strategic recommendations, contingency plans, and monitoring framework.

Subagent — spawned via subagent-spawning/spawn-agent skill.
