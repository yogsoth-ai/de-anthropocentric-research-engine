---
name: paper-search
description: AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper.
execution: import
source: literature-engine/skills/literature-search/SKILL.md
---

# Paper Search

AI-summarized paper reading for intermediate depth.

## Execution

Import — strictly follow `literature-engine/literature-search` skill protocol.

## Quality Gate

Must call get_paper_content (AI-generated report) for every analyzed paper. No conclusions from titles/abstracts alone at this depth level.

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one paper read with AI-generated summary.

## Import Source

`literature-engine` repo → `skills/literature-search/SKILL.md`
