# analyze-patent-citation-network

## Purpose

Analyze patent citation and family relationships to identify central prior art, lineages, clusters, bridge patents, and citation anomalies.

## Input contract

```yaml
required: [patent_records, citation_edges, family_keys]
optional: [classification_schema, assignee_keys, time_window]
constraints: [edge direction, source, jurisdiction, and date must be retained]
```

## Procedure

1. Deduplicate patents and family members while preserving jurisdictional edges.
2. Build directed citation and priority/family graphs.
3. Identify central, bridging, clustered, and anomalous records.
4. Interpret technical lineage with classification and source evidence.

## Output contract

```yaml
produces: [citation_graph, lineage_map, cluster_summary, bridge_patents, anomaly_report]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Centrality or cluster claims must state the graph universe and edge provenance.
- Family membership must not be used as an independent citation event without evidence.

## Failure and counterexamples

Do not equate citation count with technical importance, and do not infer absence of prior art from an incomplete graph.

## Provenance map

- `concept: knowledge-acquisition/patent-mining/citation-network-analysis`
