---
name: axis-validation
description: SOP for validating that candidate axes are independent and meaningful.
execution: sop
---

# Axis Validation

Verify that candidate dimensions are truly independent and meaningful.

## Tool

`vault_query_graph` + `vault_search`

## Protocol

1. For each pair of candidate dimensions, check: can one change without the other changing?
2. Search literature for examples where dimensions vary independently
3. If dimensions always co-vary, merge them into one
4. If a dimension has only 1 value in practice, it's not a useful dimension — remove it

## HARD-GATE

<HARD-GATE>
Must test pairwise independence for all candidate dimensions.
</HARD-GATE>

## Yield

Returns: `{ validated: string[], merged: string[], removed: string[] }`
