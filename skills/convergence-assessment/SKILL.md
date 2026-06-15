---
name: convergence-assessment
description: Compare results across multiple model variants — quantitative agreement
  metrics and qualitative conclusion stability.
execution: subagent
prompt: ./prompt.md
input: model_outputs (string), comparison_criteria (string)
dependencies:
  sops:
  - spawn-agent
---

# Convergence Assessment

Assess whether conclusions converge across model variants.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one convergence assessment pass.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
