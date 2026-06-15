---
name: paper-research
description: 'Import SOP: paper full-text reading (from literature-engine skill)'
version: 1.0.0
category: experiment-execution
type: sop
execution: import
source: skills/literature-research/SKILL.md
dependencies:
  sops:
  - literature-research
---

# Paper Research (Import)

Paper full-text reading — imported from literature-engine skill.

## Execution

Import — invokes literature-engine skill's paper-research SOP.

## Usage

Available to all campaigns for deep reading of paper full text (experimental details, statistical methods, implementation specifics, appendix data, etc.).

## MCP Tools Used

- alphaxiv: `answer_pdf_queries`, `get_paper_content` (fullText mode)
