---
name: contradiction-flagging
description: SOP for flagging contradictions in the causal model — identify conflicting
  evidence or mechanism claims.
execution: sop
---

# Contradiction Flagging

Identify and flag contradictions: conflicting evidence, incompatible mechanisms, or circular reasoning.

## Tool

`vault_query_graph` + `vault_add_edge`

## Protocol

1. Query graph around a claim to find all evidence (supported_by and contradicts edges)
2. If both supporting and contradicting evidence exists, flag the contradiction
3. Create a contradicts edge between the conflicting items if not already present
4. Document the contradiction in a question page for resolution
5. **Inline wikilinks:** For each edge created, ensure the source page body contains `[[dir/slug]]` pointing to the target (dir/slug = target path minus `.md`). Place inline at semantically relevant location. Skip if already present.

## HARD-GATE

<HARD-GATE>
Contradictions must be documented, not silently ignored.
</HARD-GATE>

## Yield

Returns: `{ contradictions_found: number, documented: string[] }`
