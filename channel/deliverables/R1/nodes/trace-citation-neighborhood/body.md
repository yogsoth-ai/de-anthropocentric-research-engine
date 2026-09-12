# trace-citation-neighborhood

## Purpose

Expand an evidence set through backward and forward citation chaining, then stop using explicit relevance and saturation criteria.

## Input contract

```yaml
required: [seed_sources, citation_edges, relevance_rules]
optional: [backward_depth, forward_depth, source_quality, criticality_schema]
constraints: [citation direction, source identity, independence, and stopping evidence must be retained]
```

## Procedure

1. Select seeds and declare the eligible citation neighborhood and relevance rules.
2. Trace backward and forward links, deduplicating lineage and dependent versions.
3. Prioritize high-information and critical nodes for full evidence review.
4. Compare each batch's new independent evidence and stop when marginal gain meets the declared saturation rationale.

## Output contract

```yaml
produces: [citation_neighborhood, lineage_edges, critical_node_set, independent_evidence_rate, saturation_assessment]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions, recommended_jumps]
```

## Quality gates

- Backward and forward coverage are reported separately.
- High-information/critical-node coverage uses a declared universe and relative numerator.
- Each batch records increment, stopping reason, source references, direction, threshold, and rationale.

## Failure and counterexamples

Do not treat citation presence as evidence relevance or count versions of one study as independent evidence.

## Provenance map

- `concept: knowledge-acquisition/snowball-survey`
- `resolved: citation-chaining`
