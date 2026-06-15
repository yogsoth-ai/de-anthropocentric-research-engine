---
name: cluster-analysis
description: Identify natural opinion clusters from collected judgments and characterize
  each cluster.
execution: subagent
prompt: ./prompt.md
input: judgments[]
dependencies:
  sops:
  - spawn-agent
---

# Cluster Analysis

Identify natural groupings of similar positions within the collected judgments. Characterize each cluster by its central position, shared reasoning patterns, and distinguishing features.

## Execution

Spawn a subagent that analyzes the judgments for similarity patterns, groups them into coherent clusters, and provides characterization of each cluster.

## Why Subagent

- Clustering requires holistic analysis of all judgments simultaneously
- Characterization is a bounded analytical task
- Output structure is standardized

## HARD-GATE

Output MUST contain: at least 2 clusters (if genuine disagreement exists), each with `cluster_id`, `position_summary`, `member_count`, and `characterization`. If all judgments agree, output 1 cluster with a note.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
