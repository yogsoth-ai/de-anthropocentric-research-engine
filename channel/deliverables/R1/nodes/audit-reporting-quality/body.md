# audit-reporting-quality

## Purpose

Audit whether an artifact reports the information needed for interpretation and reproduction using a declared domain-appropriate checklist.

## Input contract

```yaml
required: [artifact, reporting_checklist]
optional: [domain_schema, reproduction_requirements, source_context]
constraints: [each checklist judgment must cite present, absent, or ambiguous evidence]
```

## Procedure

1. Instantiate the checklist for the artifact type and domain.
2. Inspect each item and record evidence, omission, or ambiguity.
3. Separate interpretation-critical omissions from cosmetic omissions.
4. Summarize reporting completeness and reproduction implications.

## Output contract

```yaml
produces: [checklist_results, critical_omissions, ambiguity_log, reporting_quality_summary]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- Checklist version and applicability are recorded.
- Missing information is not silently inferred.

## Failure and counterexamples

Do not equate a long report with complete reporting or treat an inapplicable checklist item as a failure.

## Provenance map

- `resolved: knowledge-acquisition-documentation-audit`
- `resolved: knowledge-acquisition-reproducibility-checklist-audit`
- `intermediate: Pass3/audit-benchmark-documentation`
- `intermediate: Pass3/audit-reproducibility-reporting`

