---
name: consensus-classification
description: Classify items as consensus or dissensus at a given threshold.
execution: subagent
prompt: ./prompt.md
input: judgments[], threshold
dependencies:
  sops:
  - spawn-agent
---

# Consensus Classification

Classify each item (question, indication, or topic) as having reached consensus or remaining in dissensus at the specified threshold. Produces two clean lists with supporting evidence.

## Execution

Spawn a subagent that takes judgments and a threshold value, then classifies each item and provides the evidence for classification.

## Why Subagent

- Classification is a bounded analytical task
- Output structure is standardized
- Feeds directly into synthesis and reporting

## HARD-GATE

Output MUST contain: `consensus_items[]` and `dissensus_items[]` arrays. Every item in the input must appear in exactly one list. Each item must include its score and classification rationale.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
