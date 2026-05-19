---
name: web-research
description: Full-page web reading for non-academic perspectives — blogs, tech reports, product pages, industry analysis. Import of web-browsing/web-research skill. Must fetch full page via apify for every analyzed page.
execution: import
source: web-browsing/skills/web-research/SKILL.md
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
