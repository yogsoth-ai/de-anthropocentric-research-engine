---
name: web-search
description: 'Import SOP: quick web scan discovery (from web-browsing skill)'
version: 1.0.0
category: experiment-execution
type: sop
execution: import
source: skills/web-search/SKILL.md
dependencies:
  sops:
  - web-search
---

# Web Search (Import)

Quick web scan discovery — imported from web-browsing skill.

## Execution

Import — invokes web-browsing skill's web-search SOP.

## Usage

Available to all campaigns for rapid information discovery (methodologies, tools, datasets, competing methods, etc.).

## MCP Tools Used

- brave-search: `brave_web_search`, `brave_news_search`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| web-search | Quick web scanning — discover pages, get snippets, find URLs. For orientation only, not substantive analysis. |

<!-- END available-tables (generated) -->
