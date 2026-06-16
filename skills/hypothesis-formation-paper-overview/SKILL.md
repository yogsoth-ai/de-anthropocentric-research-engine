---
name: paper-overview
description: 'Import SOP: Quick paper scan, returns abstract and metadata (from literature-engine)'
version: 1.0.0
category: hypothesis-formation
type: import-sop
source: skills/literature-overview/SKILL.md
source_skill: paper-overview
provides: Quick paper scan capability — abstract, metadata, basic information
dependencies:
  sops:
  - literature-overview
execution: import
---

# Paper Overview (Import)

Quick paper scan capability imported from the `literature-engine` skill library.

## Purpose

- Quickly understand a paper's topic and contribution
- Obtain paper metadata (authors, year, citation count)
- Judge whether a paper is worth reading in depth

## How to Use

Directly call the `paper-overview` skill in `literature-engine`. This skill provides:
- Semantic Scholar / AlphaXiv metadata retrieval
- Abstract extraction
- Basic relevance judgment

## When to Use

- You need to quickly judge whether a paper is relevant
- You need to obtain a paper's basic information
- When batch-scanning multiple papers

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| literature-overview | Quick landscape scan — discover papers on a topic without full-text reading |

<!-- END available-tables (generated) -->
