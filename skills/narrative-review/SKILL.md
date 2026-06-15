---
name: narrative-review
description: Theory-driven literature review for building arguments and frameworks.
  Flexible, subjective, and narrative-focused — selects evidence strategically to
  support a thesis. High web-research budget for blogs, opinion pieces, and industry
  perspectives. Use when the user is writing a position paper, survey introduction,
  or constructing a coherent narrative around a research theme.
dependencies:
  tactics:
  - narrative-framing
  sops:
  - categorize-papers
  - knowledge-acquisition-gap-identification
  - knowledge-acquisition-paper-overview
  - knowledge-acquisition-paper-research
  - knowledge-acquisition-paper-search
  - knowledge-acquisition-web-research
  - knowledge-acquisition-web-search
  - survey-synthesis
  - thematic-coding
---

# Narrative Review

**Purpose**: Flexible, subjective, theory-driven — build a theoretical argument supported by literature. Not objective coverage, but persuasive framing.

**When to use**: User is writing a position paper, survey introduction, or needs to construct a coherent narrative around a research theme.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 80 results | 72–88 |
| web-research | 15 pages | 13–17 |
| paper-overview | 50 papers | 45–55 |
| paper-search | 40 papers | 36–44 |
| paper-research | 20 papers | 18–22 |

## State Ledger

Print this table before each major iteration decision:

```
| SOP            | Target | Current | % Complete |
|----------------|--------|---------|------------|
| web-search     | 80     | ???     | ???%       |
| web-research   | 15     | ???     | ???%       |
| paper-overview | 50     | ???     | ???%       |
| paper-search   | 40     | ???     | ???%       |
| paper-research | 20     | ???     | ???%       |
```

Do not exit the strategy until all rows reach ≥90%.

## Available Tactics

- `narrative-framing` — define themes → build argument → select supporting evidence

## Available SOPs

**Import** (strict protocol execution):
- `web-search` → web-browsing/skills/web-search/SKILL.md
- `web-research` → web-browsing/skills/web-research/SKILL.md
- `paper-overview` → literature-engine/skills/literature-overview/SKILL.md
- `paper-search` → literature-engine/skills/literature-search/SKILL.md
- `paper-research` → literature-engine/skills/literature-research/SKILL.md

**Subagent** (CC decides when to invoke):
- `categorize-papers` — cluster papers by theme/method/timeline
- `thematic-coding` — identify recurring themes across papers
- `gap-identification` — find what the literature hasn't addressed
- `survey-synthesis` — produce final structured output

## Execution Guidance

- narrative-framing tactic is central — defines the argument structure first, then searches for evidence
- High web-research (15 pages) because narrative reviews draw on blogs, opinion pieces, industry perspectives
- thematic-coding to identify recurring themes across papers
- Reading is selective and theory-driven — not exhaustive, but strategically chosen to support the narrative
- gap-identification frames the "so what" of the narrative

## Output Format

**Structured Narrative** containing:
- Thesis / central argument statement
- Supporting evidence organized by theme
- Counterarguments acknowledged and addressed
- Gap / opportunity identified (the "so what")
- Suggested narrative arc for writing

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| narrative-framing | Theory-driven reading tactic — define a theoretical framework first, then guide reading to fill it with evidence. Five stages (theme identification, argument construction, evidence collection, counter-evidence, synthesis). The most intellectually demanding tactic. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| categorize-papers | Cluster papers by theme, method, or timeline. Produces natural groupings from a paper collection. Used by scoping-survey and narrative-review. |
| knowledge-acquisition-gap-identification | Identify what the literature has NOT addressed — missing methods, untested combinations, unexplored applications, contradictions without resolution. Used by all strategies. |
| knowledge-acquisition-paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| knowledge-acquisition-paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| knowledge-acquisition-paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| knowledge-acquisition-web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| knowledge-acquisition-web-search | Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone. |
| survey-synthesis | Final synthesis step — weave all gathered evidence (reading notes, extracted data, categorizations) into a coherent structured output appropriate to the strategy type. Used by all 5 strategies as the final step. |
| thematic-coding | Identify recurring themes across papers using qualitative coding methodology. Produces a codebook with theme definitions, supporting evidence, and frequency counts. Used by narrative-review. |

<!-- END available-tables (generated) -->
