---
name: inconsistency-localization
description: Identify which specific comparison pairs are most responsible for preference
  cycles and inconsistencies.
execution: subagent
prompt: ./prompt.md
input: comparison_matrix(object), cycles(array)
dependencies:
  sops:
  - spawn-agent
---

# Inconsistency Localization

Given detected cycles in a preference graph, identifies which specific pairwise judgments are most likely erroneous. Ranks problematic pairs by their participation in cycles and weakness of evidence.

## Execution

Runs as a subagent. Receives the comparison matrix and detected cycles, returns prioritized list of pairs to re-evaluate.

## Why Subagent

Localization requires cross-referencing cycle membership with edge confidence scores and computing centrality metrics on the inconsistency subgraph. This focused analysis benefits from isolation.

## HARD-GATE

Output MUST contain at least one problematic pair if cycles input is non-empty. Each pair MUST appear in at least one of the input cycles. Pairs MUST be ordered by priority (most problematic first).

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
