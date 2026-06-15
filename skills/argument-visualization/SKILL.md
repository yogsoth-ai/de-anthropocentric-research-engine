---
name: argument-visualization
description: SOP for generating argument structure visualization — query graph for
  argument chains, format as mermaid diagram or indented tree, write to vault.
execution: sop
---

# Argument Visualization

Generate a visual representation of the argument structure for a topic.

## Tool

`vault_query_graph` + CC file write

## Protocol

1. Query graph starting from the topic node, traversing supported_by, contradicts, and derived_from edges
2. Collect all claims, evidence, and their relationships
3. Format as a mermaid diagram in the wiki page:
   - Green nodes: strong claims (strength ≥ 7)
   - Yellow nodes: moderate claims (strength 4-6)
   - Red nodes: weak claims (strength ≤ 3)
   - Solid edges: supported_by
   - Dashed edges: contradicts
4. Write/update `wiki/topics/<topic-slug>.md` with the argument map section
5. Include a summary: total claims, strongest/weakest, key contradictions

## HARD-GATE

<HARD-GATE>
Visualization must include at least 3 claims and their relationships. A single-node diagram is not useful.
</HARD-GATE>

## Yield

Returns: `{ topic: string, claims_shown: number, edges_shown: number, format: "mermaid" }`
