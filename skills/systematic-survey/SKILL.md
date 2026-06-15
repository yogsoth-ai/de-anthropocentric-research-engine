---
name: systematic-survey
description: Exhaustive PRISMA-style literature survey — comprehensive coverage of
  all related work on a specific question. Multi-stage screening, citation chaining,
  quality assessment, and structured data extraction. Use when the user needs to demonstrate
  complete literature coverage or conduct rigorous gap analysis.
dependencies:
  tactics:
  - citation-chaining
  - prisma-screening
  sops:
  - define-search-protocol
  - extract-data
  - knowledge-acquisition-gap-identification
  - knowledge-acquisition-paper-overview
  - knowledge-acquisition-paper-research
  - knowledge-acquisition-paper-search
  - knowledge-acquisition-saturation-detection
  - knowledge-acquisition-web-research
  - knowledge-acquisition-web-search
  - prisma-flowchart
  - quality-assessment
  - survey-synthesis
---

# Systematic Survey

**Purpose**: Deep and exhaustive — exhaustive coverage of all related work on a specific question. PRISMA-style rigor.

**When to use**: User needs to demonstrate comprehensive literature coverage (e.g., for a survey paper's related work section, or gap analysis requiring complete picture).

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 50 results | 45–55 |
| web-research | 5 pages | 4–6 |
| paper-overview | 60 papers | 54–66 |
| paper-search | 40 papers | 36–44 |
| paper-research | 30 papers | 27–33 |

## State Ledger

Print this table before each major iteration decision:

```
| SOP            | Target | Current | % Complete |
|----------------|--------|---------|------------|
| web-search     | 50     | ???     | ???%       |
| web-research   | 5      | ???     | ???%       |
| paper-overview | 60     | ???     | ???%       |
| paper-search   | 40     | ???     | ???%       |
| paper-research | 30     | ???     | ???%       |
```

Do not exit the strategy until all rows reach ≥90%.

## Available Tactics

- `prisma-screening` — multi-stage filtering (identification → screening → eligibility → inclusion)
- `citation-chaining` — forward/backward citation expansion until saturation

## Available SOPs

**Import** (strict protocol execution):
- `web-search` → web-browsing/skills/web-search/SKILL.md
- `web-research` → web-browsing/skills/web-research/SKILL.md
- `paper-overview` → literature-engine/skills/literature-overview/SKILL.md
- `paper-search` → literature-engine/skills/literature-search/SKILL.md
- `paper-research` → literature-engine/skills/literature-research/SKILL.md

**Subagent** (CC decides when to invoke):
- `define-search-protocol` — formalize queries + inclusion/exclusion criteria
- `extract-data` — structured comparison tables from deep-read papers
- `quality-assessment` — methodological rigor scoring
- `prisma-flowchart` — PRISMA-compliant flow documentation
- `saturation-detection` — determine when to stop expanding
- `gap-identification` — find what the literature hasn't addressed
- `survey-synthesis` — produce final structured output

## Execution Guidance

- Start with define-search-protocol (formalize queries + inclusion/exclusion criteria)
- Use prisma-screening tactic for multi-stage filtering
- citation-chaining to catch papers missed by keyword search
- saturation-detection to know when to stop expanding
- extract-data for structured comparison tables
- quality-assessment for methodological rigor scoring
- This is the most resource-intensive strategy — budget reflects depth

## Output Format

**Comprehensive Systematic Review** containing:
- PRISMA flow diagram (identification → screening → eligibility → inclusion counts)
- Structured comparison tables (method × dataset × metric)
- Quality assessment scores per paper
- Identified gaps with evidence
- Synthesis narrative connecting findings

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| citation-chaining | Forward and backward citation tracing tactic — expand paper coverage by tracing citation networks in both directions from seed/key papers. Alternates forward (who cited this) and backward (what this cited) passes until saturation. |
| prisma-screening | Multi-stage PRISMA screening tactic — progressively filter papers from a large candidate pool to a focused set for deep reading. Four stages (identification, title/abstract screening, full-text screening, inclusion) with documented counts at each stage. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| define-search-protocol | Formalize search queries and inclusion/exclusion criteria for systematic surveys. Produces a reproducible search protocol document. Used by systematic-survey. |
| extract-data | Structured data extraction from deep-read papers — produces comparison tables (method, dataset, metrics, results, limitations). Used by systematic-survey and deep-survey. |
| knowledge-acquisition-gap-identification | Identify what the literature has NOT addressed — missing methods, untested combinations, unexplored applications, contradictions without resolution. Used by all strategies. |
| knowledge-acquisition-paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| knowledge-acquisition-paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| knowledge-acquisition-paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| knowledge-acquisition-saturation-detection | Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey. |
| knowledge-acquisition-web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| knowledge-acquisition-web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |
| prisma-flowchart | Generate PRISMA-compliant flow data documenting the screening funnel — counts at each stage (identification, screening, eligibility, inclusion) with exclusion reasons. Used by systematic-survey via prisma-screening tactic. |
| quality-assessment | Methodological rigor scoring for papers — evaluates bias risk, reproducibility, sample adequacy using established frameworks. Used by systematic-survey. |
| survey-synthesis | Final synthesis step — weave all gathered evidence (reading notes, extracted data, categorizations) into a coherent structured output appropriate to the strategy type. Used by all 5 strategies as the final step. |

<!-- END available-tables (generated) -->
