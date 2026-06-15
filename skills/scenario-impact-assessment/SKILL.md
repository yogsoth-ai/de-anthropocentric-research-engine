---
name: scenario-impact-assessment
description: Assess each scenario's impact on the research approach across multiple
  dimensions
version: 1.0.0
category: experiment-execution
type: sop
execution: subagent
prompt: ./prompt.md
input: scenario narrative, research approach description, evaluation dimensions
output: multi-dimensional impact analysis with ratings and justifications
dependencies:
  sops:
  - spawn-agent
---

# SOP: Scenario Impact Assessment

Assess how a specific scenario affects the viability, relevance, and competitive positioning of the research approach. Produces a structured multi-dimensional impact analysis.

Subagent — spawned via subagent-spawning/spawn-agent skill.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
