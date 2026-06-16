---
name: paper-search
description: Paper AI summary report via alphaxiv get_paper_content. Import of literature-engine/paper-search
  skill. Structured AI-generated intermediate report.
execution: import
source: skills/literature-search/SKILL.md
dependencies:
  sops:
  - literature-search
  - stress-test-paper-research
---

# Paper Search

Paper AI summary report — structured intermediate report optimized for LLM consumption.

## Execution

Import — strictly follow `literature-engine/paper-search` skill protocol.

## Quality Gate

Returns AI-generated summary. Sufficient for methodology and results claims. For exact quotes or detailed data, use paper-research (full text).

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one get_paper_content call.

## Import Source

`literature-engine` repo → `skills/paper-search/SKILL.md`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| literature-search | Medium-depth literature search — read AI-summarized reports for every paper analyzed |
| stress-test-paper-research | Paper full text access via alphaxiv answer_pdf_queries or get_paper_content(fullText=true). Import of literature-engine/paper-research skill. Raw extracted text for precise claims. |

<!-- END available-tables (generated) -->
