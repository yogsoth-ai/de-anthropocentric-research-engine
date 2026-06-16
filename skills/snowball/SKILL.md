---
name: snowball
description: Citation-chain-driven literature survey starting from seed papers. Traces
  research lineage in both forward (who cited this) and backward (what this cited)
  directions until saturation. High deep-read ratio (67%). Use when the user already
  has key papers and wants to find everything connected to them — ancestors, descendants,
  and branch points.
dependencies:
  tactics:
  - citation-chaining
  sops:
  - knowledge-acquisition-gap-identification
  - knowledge-acquisition-paper-overview
  - knowledge-acquisition-paper-research
  - knowledge-acquisition-paper-search
  - knowledge-acquisition-saturation-detection
  - knowledge-acquisition-web-research
  - knowledge-acquisition-web-search
  - seed-selection
  - survey-synthesis
---

# Snowball

**Purpose**: Seed-first, forward/backward tracing — start from known seed papers and trace the research lineage in both directions.

**When to use**: User already has key papers and wants to find everything connected to them — what they built on, what built on them.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 20 results | 18–22 |
| web-research | 3 pages | 2–4 |
| paper-overview | 30 papers | 27–33 |
| paper-search | 30 papers | 27–33 |
| paper-research | 20 papers | 18–22 |

## State Ledger

Print this table before each major iteration decision:

```
| SOP            | Target | Current | % Complete |
|----------------|--------|---------|------------|
| web-search     | 20     | ???     | ???%       |
| web-research   | 3      | ???     | ???%       |
| paper-overview | 30     | ???     | ???%       |
| paper-search   | 30     | ???     | ???%       |
| paper-research | 20     | ???     | ???%       |
```

Do not exit the strategy until all rows reach ≥90%.

## Available Tactics

- `citation-chaining` — forward/backward citation expansion until saturation

## Available SOPs

**Import** (strict protocol execution):
- `web-search` → web-browsing/skills/web-search/SKILL.md
- `web-research` → web-browsing/skills/web-research/SKILL.md
- `paper-overview` → literature-engine/skills/literature-overview/SKILL.md
- `paper-search` → literature-engine/skills/literature-search/SKILL.md
- `paper-research` → literature-engine/skills/literature-research/SKILL.md

**Subagent** (CC decides when to invoke):
- `seed-selection` — validate and prioritize starting papers
- `saturation-detection` — determine when to stop (diminishing returns)
- `gap-identification` — find what the literature hasn't addressed
- `survey-synthesis` — produce final structured output

## Execution Guidance

- seed-selection validates and prioritizes the starting papers
- citation-chaining is the primary operation — iterate until saturation
- saturation-detection determines when to stop (diminishing returns)
- Minimal web-search (only for context that papers don't provide)
- High paper-research ratio (20/30 = 67% deep-read rate) — trace papers deserve thorough reading
- Build a clear lineage: who influenced whom, how ideas evolved

## Output Format

**Research Lineage Map** containing:
- Seed papers → ancestors (backward trace)
- Seed papers → descendants (forward trace)
- Evolution of ideas across generations
- Key branch points where the field diverged
- Current frontier (most recent descendants)
- Lineage visualization (text-based DAG)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| citation-chaining | Forward and backward citation tracing tactic — expand paper coverage by tracing citation networks in both directions from seed/key papers. Alternates forward (who cited this) and backward (what this cited) passes until saturation. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| knowledge-acquisition-gap-identification | Identify what the literature has NOT addressed — missing methods, untested combinations, unexplored applications, contradictions without resolution. Used by all strategies. |
| knowledge-acquisition-paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| knowledge-acquisition-paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| knowledge-acquisition-paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| knowledge-acquisition-saturation-detection | Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey. |
| knowledge-acquisition-web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| knowledge-acquisition-web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |
| seed-selection | Validate and prioritize starting papers for snowball surveys. Evaluates which seeds will yield the richest citation traces based on citation count, recency, and network position. |
| survey-synthesis | Final synthesis step — weave all gathered evidence (reading notes, extracted data, categorizations) into a coherent structured output appropriate to the strategy type. Used by all 5 strategies as the final step. |

<!-- END available-tables (generated) -->
