---
name: matrix-export
description: SOP for exporting the dimensional matrix as a readable document or structured
  data.
execution: sop
---

# Matrix Export

Export the dimensional matrix as a readable summary document.

## Tool

`vault_graph_stats` + CC file write

## Protocol

1. Gather all dimension pages and their values
2. Reconstruct the matrix from graph edges
3. Format as markdown table(s) with cell status markers
4. Write to `topics/dimensional-matrix.md`
5. Include summary statistics (coverage %, top gaps, key patterns)

## HARD-GATE

<HARD-GATE>
Export must be readable without vault access — self-contained with all dimension names and values.
</HARD-GATE>

## Yield

Returns: `{ dimensions: number, total_cells: number, coverage_pct: number, export_path: string }`
