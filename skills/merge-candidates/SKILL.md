---
name: merge-candidates
description: SOP for identifying near-duplicate concepts that should be merged.
execution: sop
---

# Merge Candidates

Find concept pages that likely refer to the same thing and should be merged.

## Tool

`vault_search`

## Protocol

1. For each concept, search vault with its title and common synonyms
2. If search returns another concept with score > 7.0, flag as merge candidate
3. Compare definitions — if semantically equivalent, recommend merge
4. Return candidate pairs with confidence assessment

## HARD-GATE

<HARD-GATE>
Must scan at least 10 concepts (or all concepts if fewer than 10 exist).
</HARD-GATE>

## Yield

Returns: `{ scanned: number, candidates: Array<{a: string, b: string, confidence: number}> }`
