---
name: web-research
description: Full-page web reading for non-academic perspectives — blogs, tech reports,
  product pages, industry analysis. Import of web-browsing/web-research skill. Must
  fetch full page via apify for every analyzed page.
execution: import
source: skills/web-research/SKILL.md
dependencies:
  sops:
  - web-research
---

# Web Research

Full-page web reading for non-academic perspectives (blogs, tech reports, products, industry analysis).

## Execution

Import — strictly follow `web-browsing/web-research` skill protocol.

## Quality Gate

Must fetch full page content via apify rag-web-browser for every analyzed page. No conclusions from snippets or partial content.

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one full page read and analyzed.

## Import Source

`web-browsing` repo → `skills/web-research/SKILL.md`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| web-research | Deep web research — fetches full page content for analysis. Snippets alone are PROHIBITED for conclusions. |

<!-- END available-tables (generated) -->
