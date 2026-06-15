---
name: alias-resolution
description: SOP for detecting and resolving concept aliases — merge duplicate pages,
  redirect edges.
execution: sop
---

# Alias Resolution

Detect when two concept pages refer to the same thing under different names. Merge into canonical page.

## Tool

`vault_search` + CC file operations + `vault_add_edge`

## Protocol

1. Search vault for the concept name and common synonyms
2. If multiple pages cover the same concept: choose canonical name
3. Merge content from duplicate into canonical page
4. Redirect all edges from duplicate to canonical
5. **Inline wikilinks:** After edge redirection, ensure the canonical page body contains `[[dir/slug]]` for all targets (dir/slug = target path minus `.md`). Place inline at semantically relevant locations. Skip if already present.
6. Delete duplicate page
7. Update index

## HARD-GATE

<HARD-GATE>
Before merging, verify the pages truly refer to the same concept (not related but distinct concepts).
</HARD-GATE>

## Yield

Returns: `{ merged: boolean, canonical: string, aliases_resolved: string[] }`
