---
name: intervention-page-creation
description: SOP for documenting an intervention — what happens when a causal variable
  is manipulated.
execution: sop
---

# Intervention Page Creation

Document an intervention: what variable is manipulated, how, and what the predicted/observed effects are.

## Tool

CC file write + `vault_add_edge`

## Protocol

1. Write `claims/<intervention-slug>.md` with frontmatter (type: claim, confidence, tags: [intervention])
2. Body: target variable, manipulation method, predicted effects, observed effects (if available)
3. Add edges: addresses (intervention → question), derived_from (intervention → variable)
4. Link supporting evidence
5. **Inline wikilinks:** For each edge created, ensure the intervention page body contains `[[dir/slug]]` pointing to the target (dir/slug = target path minus `.md`). Place inline at semantically relevant location. Skip if already present.

## HARD-GATE

<HARD-GATE>
Intervention must specify: target variable, direction of manipulation, predicted downstream effects.
</HARD-GATE>

## Yield

Returns: `{ path: string, target_variable: string, predicted_effects: string[] }`
