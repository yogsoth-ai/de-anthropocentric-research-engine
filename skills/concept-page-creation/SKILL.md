---
name: concept-page-creation
description: SOP for creating a new concept page with proper frontmatter, content,
  and initial edges.
execution: sop
---

# Concept Page Creation

Create a new concept page in the vault with proper structure.

## Tool

CC file write + `vault_add_edge` + `vault_index`

## Protocol

1. Search vault to confirm concept doesn't already exist
2. Write `concepts/<slug>.md` with frontmatter (type, title, created, tags)
3. Body: one-paragraph definition + key properties + `[[wikilinks]]` to related concepts
4. Add ≥1 edge connecting to existing graph
5. **Inline wikilinks:** For each edge created, ensure the concept page body contains `[[dir/slug]]` pointing to the target (dir/slug = target path minus `.md`). Place inline at semantically relevant location. Skip if already present.
6. Call vault_index (incremental)

## HARD-GATE

<HARD-GATE>
Every new concept page must have ≥1 edge to the existing graph.
No orphan creation allowed.
</HARD-GATE>

## Yield

Returns: `{ path: string, edges_added: number }`
