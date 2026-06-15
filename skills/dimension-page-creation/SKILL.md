---
name: dimension-page-creation
description: SOP for creating a dimension page — documents an axis of variation with
  its values and semantics.
execution: sop
---

# Dimension Page Creation

Create a page representing a dimension (axis of variation) in the design space.

## Tool

CC file write + `vault_add_edge` + `vault_index`

## Protocol

1. Search vault to confirm dimension doesn't already exist
2. Write `concepts/<dimension-slug>.md` with frontmatter (tags: [dimension])
3. Body: definition, axis values (discrete or continuous range), examples of work at each value
4. Add edges: component_of (dimension → parent domain concept)
5. **Inline wikilinks:** For each edge created, ensure the dimension page body contains `[[dir/slug]]` pointing to the target (dir/slug = target path minus `.md`). Place inline at semantically relevant location. Skip if already present.
6. Call vault_index (incremental)

## HARD-GATE

<HARD-GATE>
Dimension must have ≥2 distinct values and a clear definition of what varies along the axis.
</HARD-GATE>

## Yield

Returns: `{ path: string, values: string[], edges_added: number }`
