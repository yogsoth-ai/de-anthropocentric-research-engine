---
name: scoping-survey
description: Broad landscape mapping strategy — quickly understand what exists in
  a field. Prioritizes breadth over depth with high paper-overview volume and minimal
  deep reading. Use when entering a new field or needing orientation before committing
  to deeper investigation.
dependencies:
  sops:
  - categorize-papers
  - knowledge-acquisition-gap-identification
  - knowledge-acquisition-paper-overview
  - knowledge-acquisition-paper-search
  - knowledge-acquisition-web-research
  - knowledge-acquisition-web-search
  - survey-synthesis
  - taxonomy-mapping
---

# Scoping Survey

**Purpose**: Broad and shallow — map the landscape of a field quickly. Understand what exists, who's working on what, and where the boundaries are.

**When to use**: User is entering a new field, needs orientation before committing to deeper investigation.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 100 results | 90–110 |
| web-research | 10 pages | 9–11 |
| paper-overview | 100 papers | 90–110 |
| paper-search | 20 papers | 18–22 |
| paper-research | 0 | 0 |

CC may deviate within ±10% with documented reasoning. If the field is genuinely small (fewer papers exist), document and proceed.

## State Ledger

Print this table before each major iteration decision:

```
| SOP            | Target | Current | % Complete |
|----------------|--------|---------|------------|
| web-search     | 100    | ???     | ???%       |
| web-research   | 10     | ???     | ???%       |
| paper-overview | 100    | ???     | ???%       |
| paper-search   | 20     | ???     | ???%       |
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

**Subagent** (optional, CC decides):
- `categorize-papers` — cluster papers by theme/method/timeline
- `taxonomy-mapping` — construct hierarchical field map
- `gap-identification` — find what the literature hasn't addressed
- `survey-synthesis` — produce final structured output

## Execution Guidance

- Prioritize breadth over depth — many queries, fast scanning
- paper-overview is the primary operation (100 papers scanned at abstract level)
- paper-search (20 papers with AI summaries) is selective — only for key papers that need slightly deeper understanding
- No paper-research — this strategy does not deep-read
- taxonomy-mapping is particularly valuable here (produces field map)
- End with survey-synthesis to produce structured output

## Output Format

**Field Landscape Map** containing:
- Taxonomy of sub-areas (hierarchical)
- Key authors and research groups per sub-area
- Research trends (hot / active / declining / dormant)
- Open questions and unexplored directions
- Entry points for deeper investigation

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| categorize-papers | Cluster papers by theme, method, or timeline. Produces natural groupings from a paper collection. Used by scoping-survey and narrative-review. |
| knowledge-acquisition-gap-identification | Identify what the literature has NOT addressed — missing methods, untested combinations, unexplored applications, contradictions without resolution. Used by all strategies. |
| knowledge-acquisition-paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| knowledge-acquisition-paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| knowledge-acquisition-web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| knowledge-acquisition-web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |
| survey-synthesis | Final synthesis step — weave all gathered evidence (reading notes, extracted data, categorizations) into a coherent structured output appropriate to the strategy type. Used by all 5 strategies as the final step. |
| taxonomy-mapping | Construct a hierarchical field map from paper collection — multi-level taxonomy with parent/child relationships, paper counts per node, and maturity indicators. Used by scoping-survey. |

<!-- END available-tables (generated) -->
