---
name: counterfactual-scenario-construction
description: Construct precise, internally consistent counterfactual scenarios where
  specified factors are altered, then reason about the resulting conclusion.
execution: subagent
prompt: ./prompt.md
input: artifact (string), factor_to_change (string), change_specification (string)
dependencies:
  sops:
  - spawn-agent
---

# Counterfactual Scenario Construction

Builds precise counterfactual worlds where specified factors differ from actuality.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Scenario construction requires careful reasoning about cascading effects of changes while maintaining internal consistency.

## Input

- **artifact**: The original artifact
- **factor_to_change**: Which factor to alter
- **change_specification**: How to alter it (remove, weaken, strengthen, invert)

## Output

- **scenario**: The counterfactual world description
- **conclusion_status**: holds/weakened/flipped/indeterminate
- **cascading_effects**: What else changes as a result
- **consistency_check**: Whether the scenario is internally consistent

## Budget

One unit = one scenario construction per factor change.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
