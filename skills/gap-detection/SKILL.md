---
name: gap-detection
description: SOP for finding structural gaps in the ontology — missing concepts, thin
  branches, disconnected clusters.
execution: sop
---

# Gap Detection

Find structural gaps: missing intermediate concepts, thin branches, disconnected clusters.

## Tool

`vault_graph_stats` + `vault_query_graph` + `vault_lint`

## Protocol

1. Run vault_graph_stats — check orphan list and edge distribution
2. For each orphan, query its neighborhood — is it truly isolated or just missing one edge?
3. Check edge_type_distribution — are some types underrepresented?
4. Identify thin branches (nodes with only 1 edge)
5. Report gaps with suggested fixes

## HARD-GATE

<HARD-GATE>
Must analyze the full orphan list and report actionable gap descriptions.
</HARD-GATE>

## Yield

Returns: `{ orphans: number, thin_branches: number, suggested_fixes: string[] }`
