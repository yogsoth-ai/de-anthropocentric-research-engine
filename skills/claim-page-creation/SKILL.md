---
name: claim-page-creation
description: SOP for creating a claim page in the vault — atomic proposition with
  type classification, source attribution, and initial confidence.
execution: sop
---

# Claim Page Creation

Create a claim page in the vault representing a single atomic proposition.

## Tool

CC file write + `vault_add_edge`

## Protocol

1. Write `wiki/claims/<claim-slug>.md` with frontmatter:
   - `type: claim`
   - `claim-type:` one of [empirical, definitional, causal, normative, existential]
   - `confidence:` initial confidence (0.0-1.0) based on source quality
   - `source:` attribution to the originating source page
2. Body: the claim stated clearly in one sentence, followed by brief context
3. Add edge: `derived_from` (claim → source page)
4. If related claims exist, add `related_to` edges
5. **Inline wikilinks:** For each edge created, ensure the claim page body contains `[[dir/slug]]` pointing to the target (dir/slug = target path minus `.md`). Place inline at semantically relevant location. Skip if already present.

## HARD-GATE

<HARD-GATE>
Claim must be atomic — one proposition only. If it contains "and", "but", "because", or multiple independent assertions, it must be decomposed first.
</HARD-GATE>

## Yield

Returns: `{ path: string, claim_type: string, confidence: number }`
