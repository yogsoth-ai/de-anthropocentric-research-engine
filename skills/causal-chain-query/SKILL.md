---
name: causal-chain-query
description: SOP for tracing causal chains — follow edges from cause to effect through
  intermediate variables.
execution: sop
---

# Causal Chain Query

Trace a causal chain from a starting variable through intermediate variables to downstream effects.

## Tool

`vault_query_graph`

## Protocol

1. Call vault_query_graph with starting node, direction=out, depth=3
2. Filter results to only causal edges (derived_from, component_of)
3. Reconstruct the chain as an ordered sequence
4. Identify branching points (one cause → multiple effects)
5. Check for cycles (indicates feedback loop)

## HARD-GATE

<HARD-GATE>
Must report the full chain, not just endpoints. Include intermediate variables.
</HARD-GATE>

## Yield

Returns: `{ chain: string[], branches: number, has_cycle: boolean }`
