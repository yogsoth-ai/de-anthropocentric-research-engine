---
name: web-search
description: 'Import SOP: quick web scan, discover URLs and snippets (from web-browsing)'
version: 1.0.0
category: hypothesis-formation
type: import-sop
source: skills/web-search/SKILL.md
source_skill: web-search
provides: Quick web search capability — discover relevant URLs, snippets, preliminary information
dependencies:
  sops:
  - web-search
execution: import
---

# Web Search (Import)

Quick web search capability imported from the `web-browsing` skill library.

## Purpose

- Quickly search theoretical frameworks and methodology literature
- Discover relevant URLs and snippets
- Preliminary information gathering

## How to Use

Directly invoke the `web-search` skill in `web-browsing`. This skill provides:
- Brave Search API calls
- Result filtering and ranking
- Snippet extraction

## When to Use

- Need a quick understanding of a concept/framework/method
- Need to find URLs for relevant resources
- Preliminary information scan (no deep reading required)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| web-search | Quick web scanning — discover pages, get snippets, find URLs. For orientation only, not substantive analysis. |

<!-- END available-tables (generated) -->
