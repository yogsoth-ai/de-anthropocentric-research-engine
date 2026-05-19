---
name: scenario-impact-assessment
description: "Assess each scenario's impact on the research approach across multiple dimensions"
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
used-by:
  - stress-scenario
  - strategy-robustness-testing
input: scenario narrative, research approach description, evaluation dimensions
output: multi-dimensional impact analysis with ratings and justifications
---

# SOP: Scenario Impact Assessment

Assess how a specific scenario affects the viability, relevance, and competitive positioning of the research approach. Produces a structured multi-dimensional impact analysis.

Subagent — spawned via subagent-spawning/spawn-agent skill.
