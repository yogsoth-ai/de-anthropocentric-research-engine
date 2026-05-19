---
name: prisma-screening
description: Multi-stage PRISMA screening tactic — progressively filter papers from a large candidate pool to a focused set for deep reading. Four stages (identification, title/abstract screening, full-text screening, inclusion) with documented counts at each stage.
execution: tactic
used-by: literature-survey
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
