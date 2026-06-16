---
name: web-search
description: Quick web scanning for landscape understanding. Import of web-browsing/web-search
  skill. Snippets only — no conclusions from snippets alone.
execution: import
source: skills/web-search/SKILL.md
dependencies:
  sops:
  - stress-test-paper-search
  - stress-test-web-research
  - web-search
---

# Web Search

Quick web scanning for landscape understanding.

## Execution

Import — strictly follow `web-browsing/web-search` skill protocol.

## Quality Gate

Snippets only — do not draw conclusions from search result snippets alone. Snippets provide leads for deeper investigation (web-research or paper-search).

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one brave_web_search call (count=10 results).

## Import Source

`web-browsing` repo → `skills/web-search/SKILL.md`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| stress-test-paper-search | Paper AI summary report via alphaxiv get_paper_content. Import of literature-engine/paper-search skill. Structured AI-generated intermediate report. |
| stress-test-web-research | Deep web full-text retrieval via Apify RAG browser. Import of web-browsing/web-research skill. Full page content for substantive analysis. |
| web-search | Quick web scanning — discover pages, get snippets, find URLs. For orientation only, not substantive analysis. |

<!-- END available-tables (generated) -->
