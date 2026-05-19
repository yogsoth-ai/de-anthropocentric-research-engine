---
name: threshold-sweep
description: Compute consensus status at multiple threshold levels to produce a threshold-consensus curve.
execution: subagent
prompt: ./prompt.md
input: judgments[], threshold_range
used-by: structured-consensus
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
