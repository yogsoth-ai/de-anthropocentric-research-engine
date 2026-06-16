---
name: stress-test-paper-research
description: Paper full text access via alphaxiv answer_pdf_queries or get_paper_content(fullText=true).
  Import of literature-engine/paper-research skill. Raw extracted text for precise
  claims.
execution: import
source: skills/literature-research/SKILL.md
dependencies:
  sops:
  - literature-research
---

# Paper Research

Paper full text access — raw extracted text for precise claims and exact data.

## Execution

Import — strictly follow `literature-engine/paper-research` skill protocol.

## Quality Gate

Returns full paper text. Use for exact quotes, detailed methodology, specific numbers, or any claim requiring precision beyond AI summary.

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one answer_pdf_queries or get_paper_content(fullText=true) call.

## Import Source

`literature-engine` repo → `skills/paper-research/SKILL.md`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| literature-research | Deep literature research — raw full text reading and targeted PDF queries for rigorous analysis |

<!-- END available-tables (generated) -->
