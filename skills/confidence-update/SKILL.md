---
name: confidence-update
description: SOP for updating confidence scores on claims and evidence pages based
  on new information.
execution: sop
---

# Confidence Update

Update confidence scores on claim and evidence pages when new supporting or contradicting information arrives.

## Tool

CC file edit + `vault_search`

## Protocol

1. Identify pages with outdated confidence (based on new evidence or contradictions)
2. Read current page content and confidence score
3. Assess new evidence: does it support or contradict?
4. Update confidence score in frontmatter (increase for support, decrease for contradiction)
5. Add note in page body explaining the update

## HARD-GATE

<HARD-GATE>
Confidence changes must be justified with specific evidence references.
Never change confidence without citing the reason.
</HARD-GATE>

## Yield

Returns: `{ updated: number, pages: Array<{path: string, old: number, new: number}> }`
