---
name: edge-batch-creation
description: SOP for creating multiple edges in a batch — efficient bulk relationship
  creation.
execution: sop
---

# Edge Batch Creation

Create multiple edges efficiently. Used when a set of relationships has been identified and needs to be committed to the graph.

## Tool

`vault_add_edge` (called multiple times)

## Protocol

1. Receive list of (source, target, edge_type) triples
2. Validate all paths exist
3. Call vault_add_edge for each triple
4. Report successes and failures (duplicates are expected, not errors)
5. **Inline wikilinks:** For each successfully created edge, ensure the source page contains `[[dir/slug]]` pointing to the target (dir/slug = target path minus `.md`). Place inline at semantically relevant location; if none, append at end. Skip if already present.

## HARD-GATE

<HARD-GATE>
All source and target paths must exist before batch creation begins.
Validate the full batch upfront, not one-by-one.
</HARD-GATE>

## Yield

Returns: `{ attempted: number, created: number, duplicates_skipped: number }`
