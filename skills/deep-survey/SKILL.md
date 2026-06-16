---
name: deep-survey
description: Precise, targeted investigation of a specific sub-problem — few papers,
  all read in full depth. High paper-research ratio (50% deep-read rate). Use when
  the user knows exactly what they need to understand and requires detailed technical
  analysis with equations, hyperparameters, and specific claims extracted.
dependencies:
  sops:
  - extract-data
  - knowledge-acquisition-gap-identification
  - knowledge-acquisition-paper-overview
  - knowledge-acquisition-paper-research
  - knowledge-acquisition-paper-search
  - knowledge-acquisition-web-research
  - knowledge-acquisition-web-search
  - survey-synthesis
---

# Deep Survey

**Purpose**: Precise search, full-depth reading — precise investigation of a specific sub-problem. Not broad, not exhaustive — targeted and thorough.

**When to use**: User knows exactly what they're looking for and needs precise, detailed understanding. E.g., "How exactly does DPO handle the reward model?" or "What are all the variants of LoRA rank adaptation?"

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 30 results | 27–33 |
| web-research | 5 pages | 4–6 |
| paper-overview | 40 papers | 36–44 |
| paper-search | 40 papers | 36–44 |
| paper-research | 20 papers | 18–22 |

## State Ledger

Print this table before each major iteration decision:

```
| SOP            | Target | Current | % Complete |
|----------------|--------|---------|------------|
| web-search     | 30     | ???     | ???%       |
| web-research   | 5      | ???     | ???%       |
| paper-overview | 40     | ???     | ???%       |
| paper-search   | 40     | ???     | ???%       |
| paper-research | 20     | ???     | ???%       |
```

Do not exit the strategy until all rows reach ≥90%.

## Available Tactics

None mandatory — CC composes directly from SOPs.

## Available SOPs

**Import** (strict protocol execution):
- `web-search` → web-browsing/skills/web-search/SKILL.md
- `web-research` → web-browsing/skills/web-research/SKILL.md
- `paper-overview` → literature-engine/skills/literature-overview/SKILL.md
- `paper-search` → literature-engine/skills/literature-search/SKILL.md
- `paper-research` → literature-engine/skills/literature-research/SKILL.md

**Subagent** (CC decides when to invoke):
- `extract-data` — structured comparison tables from deep-read papers
- `gap-identification` — find what the literature hasn't addressed
- `survey-synthesis` — produce final structured output

## Execution Guidance

- Search is focused and precise — few but highly targeted queries
- High ratio of paper-research to paper-overview (20/40 = 50% deep-read rate)
- paper-research is the core operation — read raw full text, extract equations, hyperparameters, specific claims
- extract-data produces detailed comparison of approaches
- End with precise, authoritative conclusions — not "overview" but "definitive understanding"

## Output Format

**Detailed Technical Analysis** containing:
- Specific methods compared side-by-side
- Equations and algorithms extracted verbatim
- Hyperparameters and implementation details
- Precise conclusions with evidence citations
- Remaining open questions at this level of detail

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| extract-data | Structured data extraction from deep-read papers — produces comparison tables (method, dataset, metrics, results, limitations). Used by systematic-survey and deep-survey. |
| knowledge-acquisition-gap-identification | Identify what the literature has NOT addressed — missing methods, untested combinations, unexplored applications, contradictions without resolution. Used by all strategies. |
| knowledge-acquisition-paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| knowledge-acquisition-paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| knowledge-acquisition-paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| knowledge-acquisition-web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| knowledge-acquisition-web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |
| survey-synthesis | Final synthesis step — weave all gathered evidence (reading notes, extracted data, categorizations) into a coherent structured output appropriate to the strategy type. Used by all 5 strategies as the final step. |

<!-- END available-tables (generated) -->
