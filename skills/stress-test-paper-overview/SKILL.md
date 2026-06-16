---
name: stress-test-paper-overview
description: Paper landscape scan returning abstracts and metadata. Import of literature-engine/paper-overview
  skill. Abstracts only — no conclusions from abstracts.
execution: import
source: skills/literature-overview/SKILL.md
dependencies:
  sops:
  - literature-overview
  - stress-test-paper-research
  - stress-test-paper-search
---

# Paper Overview

Paper landscape scan — abstracts and metadata only.

## Execution

Import — strictly follow `literature-engine/paper-overview` skill protocol.

## Quality Gate

Returns abstracts only. Do NOT draw conclusions about methodology, results, or contributions from abstracts. Use paper-search or paper-research for substantive claims.

## Budget

Quantity target is set by the calling strategy's budget table. This SOP executes one unit = one discover_papers or relevanceSearch call.

## Import Source

`literature-engine` repo → `skills/paper-overview/SKILL.md`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| literature-overview | Quick landscape scan — discover papers on a topic without full-text reading |
| stress-test-paper-research | Paper full text access via alphaxiv answer_pdf_queries or get_paper_content(fullText=true). Import of literature-engine/paper-research skill. Raw extracted text for precise claims. |
| stress-test-paper-search | Paper AI summary report via alphaxiv get_paper_content. Import of literature-engine/paper-search skill. Structured AI-generated intermediate report. |

<!-- END available-tables (generated) -->
