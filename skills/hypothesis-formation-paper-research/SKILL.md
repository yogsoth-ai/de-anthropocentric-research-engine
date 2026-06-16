---
name: hypothesis-formation-paper-research
description: 'Import SOP: Deep literature research, raw full text + PDF Q&A (from
  literature-engine)'
version: 1.0.0
category: hypothesis-formation
type: import-sop
source: skills/literature-research/SKILL.md
source_skill: paper-research
provides: Deep literature research capability — full-text retrieval, PDF Q&A, in-depth
  analysis
dependencies:
  sops:
  - literature-research
execution: import
---

# Paper Research (Import)

Deep literature research capability imported from the `literature-engine` skill library.

## Purpose

- Retrieve paper full text (markdown format)
- Perform Q&A on a paper's PDF
- Analyze a paper's methods and results in depth

## How to Use

Directly call the `paper-research` skill in `literature-engine`. This skill provides:
- Paper full-text retrieval (multi-source fallback)
- PDF Q&A (AlphaXiv answer_pdf_queries)
- AI three-pass reading method (Keshav method)

## When to Use

- You need to understand a paper's methodological details in depth
- You need to extract specific information from a paper
- You need to perform in-depth analysis of a paper

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| literature-research | Deep literature research — raw full text reading and targeted PDF queries for rigorous analysis |

<!-- END available-tables (generated) -->
