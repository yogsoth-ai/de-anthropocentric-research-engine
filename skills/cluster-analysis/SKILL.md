---
name: cluster-analysis
description: Identify natural opinion clusters from collected judgments and characterize each cluster.
execution: subagent
prompt: ./prompt.md
input: judgments[]
used-by: structured-consensus
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
