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
