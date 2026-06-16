---
name: consensus-measurement
description: Compute consensus score from collected judgments using the appropriate
  statistical method.
execution: subagent
prompt: ./prompt.md
input: judgments[]
dependencies:
  sops:
  - spawn-agent
---

# Consensus Measurement

Compute a quantitative consensus score from the collected judgments. Automatically selects the appropriate measurement method based on data type (IQR for continuous, percentage agreement for categorical, Kendall's W for rankings).

## Execution

Spawn a subagent that analyzes the judgments array, determines the appropriate consensus metric, computes the score, and reports whether the consensus threshold is met.

## Why Subagent

- Statistical computation is a pure function with clear input/output
- Method selection logic is self-contained
- Result feeds directly into round-decision

## HARD-GATE

Output MUST contain: `consensus_score` (numeric), `method_used` (string), `threshold_met` (boolean), and `interpretation` (string). Score must be computed, not estimated.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
