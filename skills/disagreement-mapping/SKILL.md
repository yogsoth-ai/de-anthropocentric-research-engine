---
name: disagreement-mapping
description: Map disagreement structure by collecting judgments, clustering opinions, extracting arguments per cluster, and visualizing fault lines.
execution: tactic
used-by: structured-consensus
---

# Disagreement Mapping

Map the structure of disagreement rather than forcing convergence. Collect diverse judgments, identify natural clusters of opinion, extract the core arguments supporting each cluster, and produce a visual map of the disagreement topology.

## Stages

1. **Collect** — Run `judgment-collection` to gather positions and reasoning from all perspectives
2. **Cluster** — Run `cluster-analysis` to identify natural groupings of similar positions
3. **Extract** — Run `argument-extraction` for each cluster to surface core arguments
4. **Visualize** — Run `disagreement-visualization` to produce the disagreement map

## Available SOPs

| SOP | Role in Tactic |
|-----|---------------|
| judgment-collection | Gather positions with reasoning from all perspectives |
| cluster-analysis | Identify natural opinion clusters and characterize them |
| argument-extraction | Extract and steel-man core arguments for each cluster |
| disagreement-visualization | Produce structured map of clusters, arguments, and fault lines |

## Execution Guidance

- Collect BOTH positions AND reasoning (not just ratings)
- Clustering should be based on reasoning similarity, not just position proximity
- Each cluster's arguments should be steel-manned (strongest possible version)
- Visualization should show: cluster sizes, key arguments, fault lines between clusters
- Identify whether disagreements are empirical, value-based, or definitional

## Minimum Yield

- Disagreement clusters (identified clusters with characterization)
- Core arguments per cluster (core arguments per cluster, steel-manned)
- Visualization (disagreement map showing topology and fault lines)
