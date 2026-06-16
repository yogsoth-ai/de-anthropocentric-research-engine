---
name: single-factor-removal
description: Remove one specified factor from the artifact's support structure and
  reason about how the conclusion changes.
execution: subagent
prompt: ./prompt.md
input: artifact (string), factor_to_remove (string), factors_list (list)
dependencies:
  sops:
  - spawn-agent
---

# Single Factor Removal

Ablation unit: removes one factor and reasons about conclusion stability.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Each removal must be reasoned about independently to avoid contamination from other removal results.

## Input

- **artifact**: The original artifact
- **factor_to_remove**: Which factor to remove
- **factors_list**: All factors (for context of what remains)

## Output

- **conclusion_before**: Original conclusion status
- **conclusion_after**: Conclusion status without this factor
- **degradation_score**: 0.0 (no effect) to 1.0 (collapse)
- **reasoning**: Why the conclusion is/isn't affected

## Budget

One unit = one factor removal per invocation.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
