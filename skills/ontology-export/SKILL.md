---
name: ontology-export
description: SOP for exporting ontology summary — generate a readable overview of
  the current ontology state.
execution: sop
---

# Ontology Export

Generate a readable summary of the current ontology state for review or external consumption.

## Tool

`vault_graph_stats` + `vault_query_graph` + CC file write

## Protocol

1. Call vault_graph_stats for global metrics
2. Query top-level concepts (depth 2) to build hierarchy overview
3. Generate summary document with:
   - Total concepts, edges, coverage metrics
   - Top-level taxonomy tree
   - Edge type distribution
   - Orphan list
   - Confidence distribution
4. Write to `topics/ontology-summary.md` or return as structured data

## HARD-GATE

<HARD-GATE>
Export must include quantitative metrics (counts) and qualitative structure (hierarchy).
</HARD-GATE>

## Yield

Returns: `{ total_concepts: number, total_edges: number, hierarchy_depth: number, export_path: string }`
