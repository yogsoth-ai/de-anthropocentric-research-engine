---
name: flip-point-detection
description: Find the minimal change magnitude along a dimension that causes the conclusion
  to flip from true to false.
execution: subagent
prompt: ./prompt.md
input: artifact (string), dimension (string), conclusion (string)
dependencies:
  sops:
  - spawn-agent
---

# Flip-Point Detection

Binary search for the minimal perturbation that reverses the conclusion.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Flip-point detection requires iterative reasoning about graduated changes, best done in isolated context.

## Input

- **artifact**: The original artifact
- **dimension**: The dimension to perturb along
- **conclusion**: The conclusion being tested

## Output

- **flip_point**: The minimal change that flips the conclusion
- **distance**: How far from actuality the flip-point is (0.0–1.0)
- **confidence**: Confidence in the flip-point location
- **search_path**: Steps taken to find the flip-point

## Budget

One unit = one binary search per dimension.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
