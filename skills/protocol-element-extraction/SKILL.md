---
name: protocol-element-extraction
description: Extract evaluation protocol parameters from papers
execution: subagent
prompt: ./prompt.md
input: paper_content, benchmark_name
dependencies:
  sops:
  - spawn-agent
---

# Protocol Element Extraction SOP

Extract all evaluation protocol parameters from a paper's description of how it evaluated on a specific benchmark. Captures the implementation details that affect reproducibility.

## Input

- **paper_content**: Full text or relevant sections of the paper
- **benchmark_name**: The specific benchmark whose evaluation protocol to extract

## Procedure

1. Locate evaluation/experimental setup sections
2. Extract all protocol parameters across 5 categories
3. Flag parameters that are ambiguous or unstated
4. Compare against original benchmark protocol (if known)
5. Note any deviations or innovations in protocol

## Output

Structured protocol specification with completeness assessment.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
