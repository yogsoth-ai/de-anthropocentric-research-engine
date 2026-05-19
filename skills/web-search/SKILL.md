---
name: web-search
description: Quick web scanning for landscape understanding. Import of web-browsing/web-search skill. Snippets only — no conclusions from snippets alone.
execution: import
source: web-browsing/skills/web-search/SKILL.md
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
