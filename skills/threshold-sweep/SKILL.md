---
name: threshold-sweep
description: Compute consensus status at multiple threshold levels to produce a threshold-consensus
  curve.
execution: subagent
prompt: ./prompt.md
input: judgments[], threshold_range
dependencies:
  sops:
  - spawn-agent
---

# Threshold Sweep

Systematically compute consensus status at multiple threshold levels across a specified range. Produces a curve showing how many items achieve consensus as the threshold varies, revealing robust vs. fragile consensus items.

## Execution

Spawn a subagent that takes judgments and a threshold range, then computes consensus classification at each threshold level to produce the curve.

## Why Subagent

- Sweep computation is a bounded, parallelizable task
- Produces a standardized curve structure
- Keeps orchestration context clean

## HARD-GATE

Output MUST contain: `threshold_curve` with at least 5 data points, each showing threshold value and number of consensus items. Curve must span the full input range.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
