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

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
