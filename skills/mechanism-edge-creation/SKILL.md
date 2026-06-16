---
name: mechanism-edge-creation
description: SOP for creating a causal mechanism edge — documents how one variable
  causes changes in another.
execution: sop
---

# Mechanism Edge Creation

Create an edge representing a causal mechanism between two variables.

## Tool

`vault_add_edge`

## Protocol

1. Verify both variable pages exist
2. Determine edge type: derived_from (direct causation), component_of (mediating variable)
3. Call vault_add_edge with appropriate weight (strength of mechanism)
4. Document mechanism description in the source variable's page body
5. **Inline wikilink:** Ensure the source page contains `[[dir/slug]]` pointing to the target (dir/slug = target path minus `.md`). Place inline where the mechanism is documented. If already present, skip.

## HARD-GATE

<HARD-GATE>
Every causal edge must have a stated mechanism (HOW does X cause Y).
Weight must reflect mechanism strength: 1.0=strong, 0.5=moderate, 0.2=weak.
</HARD-GATE>

## Yield

Returns: `{ success: boolean, mechanism: string, weight: number }`
