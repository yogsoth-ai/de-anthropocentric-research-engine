---
name: broad-web-search
description: 'Quick web scanning for field landscape understanding. Strict import
  of web-browsing/web-search skill. Hard constraint: brave_web_search count=10 per
  call, at least 150 total search results before completing.'
execution: import
source: skills/web-search/SKILL.md
dependencies:
  sops:
  - web-search
---

# Broad Web Search

Quick web scanning for landscape understanding.

## Execution

Import — strictly follow `web-browsing/web-search` skill protocol.

## Hard Constraints

- Set `count=10` on every `brave_web_search` call
- Execute multiple calls with varied queries
- Do not complete this SOP until at least 150 total search results have been gathered
- This ensures broad coverage, not just the first page of one query

## Import Source

`web-browsing` repo → `skills/web-search/SKILL.md`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| web-search | Quick web scanning — discover pages, get snippets, find URLs. For orientation only, not substantive analysis. |

<!-- END available-tables (generated) -->
