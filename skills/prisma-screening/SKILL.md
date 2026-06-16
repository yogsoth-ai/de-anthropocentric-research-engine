---
name: prisma-screening
description: Multi-stage PRISMA screening tactic — progressively filter papers from
  a large candidate pool to a focused set for deep reading. Four stages (identification,
  title/abstract screening, full-text screening, inclusion) with documented counts
  at each stage.
execution: tactic
dependencies:
  sops:
  - knowledge-acquisition-paper-overview
  - knowledge-acquisition-paper-research
  - knowledge-acquisition-paper-search
  - prisma-flowchart
---

# PRISMA Screening

Multi-stage screening following PRISMA methodology. Progressively filter papers from a large candidate pool to a focused set for deep reading.

## Stages

1. **Identification** — gather all candidate papers (via paper-overview)
2. **Title/Abstract screening** — apply inclusion/exclusion criteria (from define-search-protocol)
3. **Full-text screening** — read AI summaries (paper-search) to confirm relevance
4. **Inclusion** — final set for deep reading (paper-research)

## Available SOPs

- `paper-overview` (import) — identification stage
- `paper-search` (import) — full-text screening stage
- `paper-research` (import) — inclusion stage (deep reading)
- `prisma-flowchart` (subagent) — generate PRISMA flow data

## Execution Guidance

- Each stage documents: how many in → how many out → reasons for exclusion
- prisma-flowchart SOP generates the flow data at the end
- CC decides exact thresholds for each stage based on inclusion/exclusion criteria from define-search-protocol
- Typical funnel: 60 identified → 40 title-screened → 30 deep-read
- Document exclusion reasons at each stage (e.g., "off-topic", "wrong population", "not empirical")

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| knowledge-acquisition-paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| knowledge-acquisition-paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| knowledge-acquisition-paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| prisma-flowchart | Generate PRISMA-compliant flow data documenting the screening funnel — counts at each stage (identification, screening, eligibility, inclusion) with exclusion reasons. Used by systematic-survey via prisma-screening tactic. |

<!-- END available-tables (generated) -->
