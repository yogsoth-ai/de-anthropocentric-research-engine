---
name: wiki-edge-audit
description: SOP for auditing wikilink coverage — scans all edges and reports which
  source pages are missing [[dir/slug]] wikilinks to their targets.
execution: sop
---

# Wiki Edge Audit

Audit wikilink coverage across all edges. Identifies source pages that have edges in `_edges.jsonl` but lack the corresponding `[[dir/slug]]` wikilink in their body text.

## Tool

`vault_edge_audit`

## Protocol

1. Call `vault_edge_audit` (zero parameters)
2. Review results: `total_edges`, `covered`, `missing_count`, `missing[]`
3. If `missing_count == 0`: report full coverage, done
4. If `missing_count > 0`: for each missing entry, open the source page and insert `[[dir/slug]]` (where dir/slug = target path minus `.md`) at a semantically relevant location in the body. If no suitable location, append a sentence containing the wikilink at end of body.
5. After all fixes applied, re-run `vault_edge_audit` to confirm coverage

## HARD-GATE

<HARD-GATE>
Do NOT skip the fix step. Every missing wikilink must be resolved before reporting success.
Re-audit must show missing_count == 0.
</HARD-GATE>

## Yield

Returns: `{ total_edges: number, covered: number, fixed: number }`
