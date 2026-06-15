---
name: temporal-sensitivity-testing
description: Test whether a gap persists across different time windows (2/5/10 years).
  Determines if gap is narrowing, widening, or stable over time.
execution: subagent
prompt: ./prompt.md
input: gap_description (string), time_parameters (string)
dependencies:
  sops:
  - spawn-agent
---

# Temporal Sensitivity Testing

Assess gap stability across time windows.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Budget

One unit = one temporal sensitivity assessment for a single gap.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
