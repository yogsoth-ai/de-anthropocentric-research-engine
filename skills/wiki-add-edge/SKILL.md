---
name: wiki-add-edge
description: SOP wrapping vault_add_edge — create a typed relationship between two
  vault pages.
execution: sop
---

# Wiki Add Edge

Create a typed edge between two pages in the knowledge graph.

## HARD-GATE

<HARD-GATE>
Both source and target paths must reference existing files in the vault.
Edge type must be one of the 10 defined types in _schema.md.
Do NOT create edges to non-existent pages.
</HARD-GATE>

## Tool

`vault_add_edge`

## Parameters

| Param | Required | Description |
|-------|----------|-------------|
| source | yes | Source page path (e.g., "concepts/transformer.md") |
| target | yes | Target page path (e.g., "concepts/attention.md") |
| edge_type | yes | One of: component_of, instance_of, supported_by, contradicts, supersedes, derived_from, addresses, raises, failed_for, related_to |
| weight | no | Edge weight 0.0-1.0 (default 1.0) |

## Protocol

1. Verify both source and target files exist
2. Select appropriate edge_type based on the semantic relationship
3. Call `vault_add_edge`
4. If duplicate rejected, this is expected — the relationship already exists
5. **Inline wikilink:** Ensure the source page body contains `[[dir/slug]]` pointing to the target (dir/slug = target path minus `.md`). Place at a semantically relevant location. If already present, skip. If no suitable location, append a sentence containing the wikilink at end of body.
6. Return result to calling tactic

## Edge Type Selection Guide

| Relationship | Edge Type |
|-------------|-----------|
| A is part of B | component_of |
| A is an example of B | instance_of |
| A provides evidence for B | supported_by |
| A conflicts with B | contradicts |
| A replaces B | supersedes |
| A was built from B | derived_from |
| A answers/solves B | addresses |
| A creates/implies B (question) | raises |
| A didn't work for B | failed_for |
| A is related to B (weak) | related_to |

## Yield

Returns: `{ success: boolean, edge_type: string, edge_count: number }`
