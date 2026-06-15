---
name: narrative-framing
description: Theory-driven reading tactic — define a theoretical framework first,
  then guide reading to fill it with evidence. Five stages (theme identification,
  argument construction, evidence collection, counter-evidence, synthesis). The most
  intellectually demanding tactic.
execution: tactic
dependencies:
  sops:
  - knowledge-acquisition-paper-research
  - knowledge-acquisition-paper-search
  - knowledge-acquisition-web-research
  - thematic-coding
---

# Narrative Framing

Define a theoretical framework first, then guide reading to fill it with evidence.

## Stages

1. **Theme identification** — from initial reading, identify 3-5 major themes
2. **Argument construction** — define the narrative arc (thesis → evidence → synthesis)
3. **Evidence collection** — targeted reading to support each theme
4. **Counter-evidence** — actively search for work that challenges the narrative
5. **Synthesis** — weave themes into coherent argument

## Available SOPs

- `paper-search` (import) — targeted reading for evidence
- `paper-research` (import) — deep reading of key supporting/opposing papers
- `thematic-coding` (subagent) — identify patterns across papers
- `web-research` (import) — blogs, opinion pieces, industry perspectives

## Execution Guidance

- This is the most "intellectual" tactic — requires judgment about what matters
- thematic-coding helps identify patterns across papers
- CC must actively seek counter-evidence (intellectual honesty)
- Output is not a list but a structured argument
- Themes should emerge from reading, not be imposed a priori

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| knowledge-acquisition-paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| knowledge-acquisition-paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| knowledge-acquisition-web-research | Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page. |
| thematic-coding | Identify recurring themes across papers using qualitative coding methodology. Produces a codebook with theme definitions, supporting evidence, and frequency counts. Used by narrative-review. |

<!-- END available-tables (generated) -->
