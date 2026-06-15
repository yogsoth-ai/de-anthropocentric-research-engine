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
