---
name: gap-synthesis-strategy
description: Compile all gap analysis products into a coherent final report with evidence
  gap maps, research agenda, and concept matrices.
dependencies:
  sops:
  - egm-construction
  - evidence-synthesis
  - gap-synthesis
---

# Gap Synthesis

Compile all validated, classified, and prioritized gaps into a coherent final report.

## When to Use

All upstream strategies (identification, classification, validation, prioritization) have completed — now synthesize into a unified deliverable.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 10 | 9–11 |
| web-research | 5 | 4–6 |
| paper-overview | 10 | 9–11 |
| paper-search | 5 | 4–6 |
| paper-research | 5 | 4–6 |

## State Ledger

Print before every iteration:

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 10 | ? |
| web-research | ? | 5 | ? |
| paper-overview | ? | 10 | ? |
| paper-search | ? | 5 | ? |
| paper-research | ? | 5 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** gap-synthesis, egm-construction
**Shared:** evidence-synthesis

## Execution Guidance

Compile all intermediate products (gap candidates, classifications, validations, priorities, EGM) into a coherent report with executive summary, detailed findings, and research agenda recommendations.

## Output Format

Gap Analysis Report — executive summary, evidence gap map, classified gap inventory, prioritized research agenda, methodology notes.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| egm-construction | Build structured Evidence Gap Maps — define axes (intervention × outcome or method × domain), place gaps in cells, annotate with evidence density and quality. |
| evidence-synthesis | Synthesize multi-source evidence into structured argumentation. Weaves findings from literature, web, and analysis into coherent evidence maps with explicit strength ratings. |
| gap-synthesis | Compile all gap analysis intermediate products into a coherent final report with executive summary, detailed findings, and research agenda. |

<!-- END available-tables (generated) -->
