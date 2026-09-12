---
name: detect-coverage-gap
description: "Given an explicit coverage representation (matrix, graph, taxonomy, IP feature space), identify absent, thin, disconnected, or weakly covered regions and characterize why they matter."
---

# detect-coverage-gap

## Purpose

Given an explicit matrix, graph, taxonomy, or IP feature space, identify absent, thin, disconnected, or weakly covered regions and explain why they matter.

## Input contract

```yaml
required: [coverage_representation, universe_definition, coverage_evidence]
optional: [gap_priority_rule, taxonomy, graph_statistics, domain_constraints]
constraints: [the representation and eligible universe are explicit; every reported gap points to an absent, thin, disconnected, or weakly covered region]
```

## Procedure

1. Validate the representation and enumerate its eligible regions or nodes.
2. Mark observed coverage and classify absent, thin, disconnected, and weak-link regions.
3. Characterize the consequence and evidence for each gap.
4. Prioritize gaps using the caller-supplied rule and return an actionable gap list.

## Output contract

```yaml
produces: [coverage_gap_list, coverage_map, priority_rationale, evidence_register]
delta_fields: [findings, evidence_updates, decisions, open_questions]
```

## Quality gates

- Declare the eligible universe, numerator, denominator, batch increment, stopping reason, source references, direction, and threshold rationale for relative coverage claims.
- Report coverage ratio whenever a relative coverage claim is made.
- When coverage is evaluated over evidence sources or batches, also report independent-source ratio, marginal information gain, and saturation state.
- The complete orphan list is analyzed where graph mode applies; weak links below `<0.3` are retained as source-defined evidence and not silently normalized.
- Matrix white-space detection and graph orphan detection remain distinct representations.

## Parameterization

The caller must provide the coverage representation type, eligible universe, observed evidence, region/node schema, thinness or connectivity rule, priority rule, and source references. For graph mode provide node/edge statistics; for IP mode provide the feature taxonomy and claim map.

## Failure and counterexamples

Reject when the universe is undefined, a gap is inferred from missing data rather than represented absence, or an orphan/weak-link result lacks a repair rationale.

## Provenance map

- resolved: creative-ideation/coverage-gap-detection
- resolved: creative-ideation/white-space-detection
- resolved: knowledge-acquisition/white-space-mapping
- resolved: knowledge-structuring/gap-detection
- resolved: knowledge-structuring/model-gap-detection
- intermediate: Pass3/detect-white-space
- intermediate: Pass3/map-ip-white-space
- intermediate: Pass3/detect-structural-gap

## Verbatim source criteria excerpts

- `gap-detection` line 27: Must analyze the full orphan list and report actionable gap descriptions.
- `model-gap-detection` line 21: Check for edges with weight < 0.3 — these are weak links needing more evidence.
- `model-gap-detection` line 27: Must check both orphans and weak links and include actionable suggestions.

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| knowledge-structuring/gap-detection | 14 | gate | Analyze the complete orphan list and provide executable repair suggestions. |
| knowledge-structuring/model-gap-detection | 14 | numeric/gate | Query orphan nodes with degree 0 and weak links `<0.3`; provide executable gaps and suggestions. |
