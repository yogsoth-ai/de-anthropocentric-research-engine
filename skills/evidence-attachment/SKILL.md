---
name: evidence-attachment
description: SOP for attaching evidence to a claim — create typed edge (supported_by,
  contradicts, qualifies) with evidence quality metadata.
execution: sop
---

# Evidence Attachment

Attach a piece of evidence to a claim with a typed relationship edge.

## Tool

`vault_add_edge` + `vault_search`

## Protocol

1. Search vault for the target claim page and the evidence source page
2. Determine relationship type:
   - `supported_by` — evidence directly supports the claim
   - `contradicts` — evidence directly contradicts the claim
   - `qualifies` — evidence limits the scope or adds conditions (use `related_to` edge)
3. Add edge with metadata:
   - `edge_type:` supported_by | contradicts | related_to
   - `evidence_quality:` strong | moderate | weak
   - `directness:` direct | indirect | analogical
4. If evidence source page doesn't exist, create it first via wiki-ingest-source pattern
5. **Inline wikilink:** Ensure the evidence page body contains `[[dir/slug]]` pointing to the claim (dir/slug = target path minus `.md`). Place inline at semantically relevant location. Skip if already present.

## HARD-GATE

<HARD-GATE>
Must specify evidence quality and directness. "Supported_by" without quality assessment is not allowed.
</HARD-GATE>

## Yield

Returns: `{ claim: string, evidence: string, edge_type: string, quality: string }`
