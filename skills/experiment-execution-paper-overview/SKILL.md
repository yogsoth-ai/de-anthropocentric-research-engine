---
name: paper-overview
description: 'Import SOP: paper landscape scan (from literature-engine skill)'
version: 1.0.0
category: experiment-execution
type: sop
execution: import
source: skills/literature-overview/SKILL.md
dependencies:
  sops:
  - literature-overview
---

# Paper Overview (Import)

Paper landscape scan — imported from literature-engine skill.

## Execution

Import — invokes literature-engine skill's paper-overview SOP.

## Usage

Available to all campaigns for rapid scanning of the paper landscape in a given area (discovering key papers, identifying research trends, locating methodology sources).

## MCP Tools Used

- semantic-scholar: `relevanceSearch`, `paperBatch`
- alphaxiv: `discover_papers`
