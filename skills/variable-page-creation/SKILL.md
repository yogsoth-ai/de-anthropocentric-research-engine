---
name: variable-page-creation
description: SOP for creating a variable page in the causal model — documents a measurable
  quantity with its properties.
execution: sop
---

# Variable Page Creation

Create a page representing a causal variable — a measurable quantity that can change and affect other variables.

## Tool

CC file write + `vault_add_edge` + `vault_index`

## Protocol

1. Search vault to confirm variable doesn't already exist
2. Write `concepts/<variable-slug>.md` with frontmatter including tags: [causal-variable]
3. Body: definition, measurement method, known range, temporal dynamics
4. Add ≥1 edge connecting to existing causal graph
5. **Inline wikilinks:** For each edge created, ensure the variable page body contains `[[dir/slug]]` pointing to the target (dir/slug = target path minus `.md`). Place inline at semantically relevant location. Skip if already present.
6. Call vault_index (incremental)

## HARD-GATE

<HARD-GATE>
Variable must have a clear operational definition (how to measure it).
</HARD-GATE>

## Yield

Returns: `{ path: string, edges_added: number }`
