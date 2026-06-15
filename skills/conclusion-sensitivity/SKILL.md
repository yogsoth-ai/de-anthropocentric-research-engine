---
name: conclusion-sensitivity
description: Map which assumptions are load-bearing by assessing how the conclusion
  changes if each assumption fails.
execution: subagent
prompt: ./prompt.md
input: assumptions[], challenges[]
dependencies:
  sops:
  - spawn-agent
---

# Conclusion Sensitivity

Maps the relationship between assumptions and conclusions — identifying which assumptions are load-bearing (conclusion changes if they fail) versus decorative (conclusion holds regardless). Produces a sensitivity map for decision-makers.

## Execution

Spawns a subagent that takes all extracted assumptions and their challenges, then maps conclusion sensitivity to each.

## Why Subagent

- Sensitivity analysis requires holistic view across all assumptions simultaneously
- Must consider interaction effects between assumptions
- Isolation ensures objective assessment without motivated reasoning

## HARD-GATE

Output must include:
- Sensitivity rating for every assumption
- Identification of critical assumptions (conclusion-changing)
- Interaction effects between assumptions
- Overall decision robustness rating

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
