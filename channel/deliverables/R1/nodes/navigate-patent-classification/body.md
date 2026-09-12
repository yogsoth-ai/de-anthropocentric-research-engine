# navigate-patent-classification

## Purpose

Traverse IPC/CPC-like classification neighborhoods to expand or delimit a technical patent domain.

## Input contract

```yaml
required: [seed_classifications, technical_domain]
optional: [patent_records, jurisdiction_scope, depth_limit]
constraints: [each expansion or exclusion must cite a classification relation and domain rationale]
```

## Procedure

1. Normalize seed classifications and their descriptions.
2. Traverse parent, child, and adjacent classifications relevant to the domain.
3. Record inclusion, exclusion, and overlap rationales.
4. Emit the declared classification universe and unresolved boundary cells.

## Output contract

```yaml
produces: [classification_neighborhood, included_classes, excluded_classes, boundary_cells, coverage_universe]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Classification relation and source are retained.
- Coverage claims name the resulting universe.

## Failure and counterexamples

Do not treat a shared keyword as classification equivalence or infer technical absence from an unsearched class.

## Provenance map

- `concept: knowledge-acquisition/classification-navigation`

