---
name: re-scoring
description: Re-evaluate S/O/D scores after mitigation measures are in place. Validates
  that mitigations actually reduce risk as expected.
execution: subagent
prompt: ./prompt.md
input: failure_modes (string), mitigations (string), original_scores (string)
dependencies:
  sops:
  - spawn-agent
---

# Re-Scoring

Re-evaluates Severity, Occurrence, and Detection scores after mitigations are applied.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Re-scoring requires fresh evaluation without anchoring to original scores. Isolated context prevents confirmation bias toward expected improvement.

## Input

- **failure_modes**: Original failure mode descriptions
- **mitigations**: Proposed mitigation measures
- **original_scores**: Pre-mitigation S/O/D scores for comparison

## Output

- **new_scores**: Post-mitigation S, O, D, and RPN for each mode
- **effectiveness**: Comparison with original scores
- **still_high**: Modes that remain H-priority after mitigation

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
