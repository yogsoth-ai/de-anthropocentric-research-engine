---
name: selection-from-frontier
description: Select the final portfolio from the Pareto front by applying stakeholder
  preferences and decision criteria.
execution: subagent
prompt: ./prompt.md
input: pareto_front, preferences
dependencies:
  sops:
  - spawn-agent
---

# Selection from Frontier

Apply stakeholder preferences, decision criteria, and practical considerations to select a single portfolio from the Pareto front.

## Execution

Spawns a subagent that evaluates Pareto front solutions against stated preferences and produces a justified selection with alternatives noted.

## Why Subagent

Selection requires integrating quantitative frontier data with qualitative preferences, practical constraints, and judgment calls. This deliberative process benefits from focused reasoning.

## HARD-GATE

Output must include the selected portfolio, explicit justification referencing frontier position, and at least one noted alternative with explanation of what would be gained/lost by choosing it instead.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
