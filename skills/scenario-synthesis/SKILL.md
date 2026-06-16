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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
