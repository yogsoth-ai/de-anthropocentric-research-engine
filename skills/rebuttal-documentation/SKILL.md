---
name: rebuttal-documentation
description: SOP for documenting rebuttals and counter-claims — create rebuttal pages
  with typed contradiction edges and source attribution.
execution: sop
---

# Rebuttal Documentation

Document counter-claims and rebuttals that challenge existing claims.

## Tool

CC file write + `vault_add_edge`

## Protocol

1. Write `wiki/claims/<rebuttal-slug>.md` with frontmatter:
   - `type: claim`
   - `claim-type:` matching the type of the claim being rebutted
   - `confidence:` initial confidence based on rebuttal evidence
   - `rebuttal-of:` wikilink to the target claim
2. Body: the rebuttal stated clearly, with reasoning for why it contradicts the target
3. Add edge: `contradicts` (rebuttal → target claim)
4. Add edge: `derived_from` (rebuttal → source providing the rebuttal)
5. **Inline wikilinks:** For each edge created, ensure the rebuttal page body contains `[[dir/slug]]` pointing to the target (dir/slug = target path minus `.md`). Place inline at semantically relevant location. Skip if already present.

## HARD-GATE

<HARD-GATE>
Must specify exactly which claim is being rebutted and the type of contradiction (direct negation, scope limitation, alternative explanation, or undermining evidence).
</HARD-GATE>

## Yield

Returns: `{ path: string, target_claim: string, contradiction_type: string }`
