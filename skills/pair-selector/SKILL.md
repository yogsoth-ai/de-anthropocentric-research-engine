---
name: pair-selector
description: Select the next comparison pairs that maximize information gain given
  current ratings and comparison history.
execution: subagent
prompt: ./prompt.md
input: current_ratings(object), comparison_history(array)
dependencies:
  sops:
  - spawn-agent
---

# Pair Selector

Selects the next set of comparison pairs that would most reduce ranking uncertainty. Uses information-theoretic criteria (maximum entropy reduction, uncertainty sampling, or boundary proximity) to prioritize which pairs to compare next.

## Execution

Runs as a subagent. Receives current ratings and comparison history, returns an ordered list of recommended next pairs.

## Why Subagent

Pair selection requires reasoning about the full rating landscape and comparison graph structure. Isolating this as a subagent allows focused computation without polluting the orchestrator's context with matrix calculations.

## HARD-GATE

Output MUST contain at least one pair. Each pair must reference exactly two distinct candidates that exist in the current_ratings input.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
