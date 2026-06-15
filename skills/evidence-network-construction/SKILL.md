---
name: evidence-network-construction
description: Build evidence network graph for network meta-analysis — nodes, edges,
  geometry assessment
execution: subagent
prompt: ./prompt.md
input: treatment_comparisons, study_arms
dependencies:
  sops:
  - spawn-agent
---

# Evidence Network Construction SOP

Build and assess the evidence network graph for network meta-analysis, mapping treatment nodes, direct comparison edges, and evaluating network geometry.

## When to Use

- During network-comparison strategy
- When assessing feasibility of network meta-analysis
- When checking network connectivity and transitivity

## Input

- `treatment_comparisons`: All pairwise comparisons available in included studies
- `study_arms`: Study arm-level data (treatments, sample sizes)

## Output

Complete network geometry description with connectivity assessment, comparison matrix, and transitivity evaluation.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
