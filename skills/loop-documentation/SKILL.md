---
name: loop-documentation
description: SOP for documenting a feedback loop — classify, describe dynamics, identify
  break points.
execution: sop
---

# Loop Documentation

Document an identified feedback loop in the causal graph.

## Tool

CC file write + `vault_add_edge`

## Protocol

1. Write `relations/<loop-slug>.md` with frontmatter (type: relation, tags: [feedback-loop])
2. Body: loop type (reinforcing/balancing), variables involved, time delay, dominant conditions
3. Add edges connecting the relation page to all variables in the loop
4. Identify and document potential break points
5. **Inline wikilinks:** For each edge created, ensure the loop page body contains `[[dir/slug]]` pointing to the target variable (dir/slug = target path minus `.md`). Place inline where the variable is mentioned. Skip if already present.

## HARD-GATE

<HARD-GATE>
Must classify loop as reinforcing or balancing. Must list all variables in the cycle.
</HARD-GATE>

## Yield

Returns: `{ path: string, loop_type: string, variables: string[], break_points: string[] }`
