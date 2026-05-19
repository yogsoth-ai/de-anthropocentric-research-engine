---
name: consensus-classification
description: Classify items as consensus or dissensus at a given threshold.
execution: subagent
prompt: ./prompt.md
input: judgments[], threshold
used-by: structured-consensus
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
