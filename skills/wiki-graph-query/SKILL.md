---
name: wiki-graph-query
description: SOP wrapping vault_query_graph — traverse knowledge graph from a node
  to explore its neighborhood and context.
execution: sop
---

# Wiki Graph Query

Explore the neighborhood of a node in the knowledge graph. Used for understanding context before updates, finding connection opportunities, and identifying orphans.

## HARD-GATE

<HARD-GATE>
Node path must reference an existing file in the vault.
Verify the file exists before calling vault_query_graph.
</HARD-GATE>

## Tool

`vault_query_graph`

## Parameters

| Param | Required | Description |
|-------|----------|-------------|
| node | yes | Starting node path (e.g., "concepts/attention.md") |
| direction | yes | Traversal direction: "in", "out", or "both" |
| edge_type | no | Filter by edge type |
| depth | no | Traversal depth (default 1, max 3) |

## Protocol

1. Confirm node file exists in vault
2. Call `vault_query_graph` with node, direction, and optional filters
3. Analyze subgraph: identify clusters, orphan branches, missing connections
4. Return subgraph data to calling tactic

## Yield

Returns: `{ nodes_found: number, edges_found: number, subgraph: object }`
