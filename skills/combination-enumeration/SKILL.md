---
name: combination-enumeration
description: SOP for systematically enumerating combinations across dimensions.
execution: sop
---

# Combination Enumeration

Systematically enumerate combinations by crossing dimension values.

## Tool

`vault_search` + CC reasoning

## Protocol

1. Take 2-3 dimensions with their value lists
2. Generate all combinations (Cartesian product)
3. For each combination, search vault for existing work covering it
4. Classify: occupied (existing work), empty (opportunity), impossible (constraint)
5. Return classified matrix

## HARD-GATE

<HARD-GATE>
Must enumerate ALL combinations for the given dimensions, not just a sample.
</HARD-GATE>

## Yield

Returns: `{ total: number, occupied: number, empty: number, impossible: number }`
