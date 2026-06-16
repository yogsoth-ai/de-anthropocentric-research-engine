---
name: hierarchy-visualization
description: SOP for inspecting the current hierarchy structure — query graph to display
  parent-child relationships.
execution: sop
---

# Hierarchy Visualization

Inspect the current hierarchy by querying the graph for component_of and instance_of edges.

## Tool

`vault_query_graph` + `vault_graph_stats`

## Protocol

1. Call vault_graph_stats for global overview (total nodes, edges, orphans)
2. For key root concepts, call vault_query_graph (direction=in, depth=3) to see hierarchy
3. Format as indented tree structure for readability
4. Identify gaps (levels with only 1 child, missing intermediate nodes)

## HARD-GATE

<HARD-GATE>
Must query at least the top 3 root concepts to provide meaningful hierarchy view.
</HARD-GATE>

## Yield

Returns: `{ roots_queried: number, max_depth: number, gaps_identified: string[] }`
