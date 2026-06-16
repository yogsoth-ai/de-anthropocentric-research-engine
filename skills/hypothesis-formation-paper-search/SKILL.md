---
name: paper-search
description: 'Import SOP: Medium-depth literature search, AI summary report (from literature-engine)'
version: 1.0.0
category: hypothesis-formation
type: import-sop
source: skills/literature-search/SKILL.md
source_skill: paper-search
provides: Medium-depth literature search capability — search, filter, AI summary
dependencies:
  sops:
  - literature-search
execution: import
---

# Paper Search (Import)

Medium-depth literature search capability imported from the `literature-engine` skill library.

## Purpose

- Search for papers relevant to a specific topic
- Obtain AI-generated paper summary reports
- Filter and rank search results

## How to Use

Directly call the `paper-search` skill in `literature-engine`. This skill provides:
- Multi-source search (Semantic Scholar + Google Scholar + AlphaXiv)
- AI summary generation
- Relevance ranking

## When to Use

- You need to find a collection of papers relevant to a topic
- You need AI-assisted paper summaries
- You need to search across multiple databases

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| literature-search | Medium-depth literature search — read AI-summarized reports for every paper analyzed |

<!-- END available-tables (generated) -->
