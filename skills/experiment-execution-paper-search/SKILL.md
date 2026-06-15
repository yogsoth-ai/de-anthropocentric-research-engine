---
name: paper-search
description: 'Import SOP: paper AI summary reading (from literature-engine skill)'
version: 1.0.0
category: experiment-execution
type: sop
execution: import
source: skills/literature-search/SKILL.md
dependencies:
  sops:
  - literature-search
---

# Paper Search (Import)

Paper AI summary reading — imported from literature-engine skill.

## Execution

Import — invokes literature-engine skill's paper-search SOP.

## Usage

Available to all campaigns for quickly obtaining AI-generated paper summaries (method overview, key contributions, experimental setup, etc.).

## MCP Tools Used

- alphaxiv: `get_paper_content`
- semantic-scholar: `paper`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| literature-search | Medium-depth literature search — read AI-summarized reports for every paper analyzed |

<!-- END available-tables (generated) -->
