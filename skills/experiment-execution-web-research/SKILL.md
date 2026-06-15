---
name: web-research
description: 'Import SOP: deep full-page content analysis (from web-browsing skill)'
version: 1.0.0
category: experiment-execution
type: sop
execution: import
source: skills/web-research/SKILL.md
dependencies:
  sops:
  - web-research
---

# Web Research (Import)

Deep full-page content analysis — imported from web-browsing skill.

## Execution

Import — invokes web-browsing skill's web-research SOP.

## Usage

Available to all campaigns for in-depth reading and analysis of specific web pages (technical docs, framework guides, API documentation, etc.).

## MCP Tools Used

- apify: `rag-web-browser`
- brave-search: `brave_llm_context`
