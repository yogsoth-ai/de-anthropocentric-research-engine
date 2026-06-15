---
name: evidence-linking
description: SOP for linking evidence pages to causal claims — creates supported_by
  or contradicts edges.
execution: sop
---

# Evidence Linking

Link evidence pages to the causal claims they support or contradict.

## Tool

`vault_add_edge`

## Protocol

1. Identify the claim (causal edge or claim page) that the evidence addresses
2. Determine relationship: supported_by or contradicts
3. Call vault_add_edge from evidence page to claim page
4. Set weight based on evidence strength (hierarchy: RCT > observational > theoretical)
5. **Inline wikilink:** Ensure the evidence page body contains `[[dir/slug]]` pointing to the claim (dir/slug = target path minus `.md`). Place inline at semantically relevant location. Skip if already present.

## HARD-GATE

<HARD-GATE>
Evidence must be linked to a specific claim, not to a general topic.
</HARD-GATE>

## Yield

Returns: `{ claim: string, evidence: string, relationship: string, weight: number }`
