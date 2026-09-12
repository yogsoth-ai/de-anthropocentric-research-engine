# assess-publication-bias

## Purpose

Assess publication, reporting, time-lag, citation, and language bias using diagnostics appropriate to the evidence design.

## Input contract

```yaml
required: [evidence_records, outcome_schema, inclusion_frame]
optional: [registry_records, search_log, effect_estimates]
constraints: [bias claims require an observable missingness or selection pattern]
```

## Procedure

1. Define the eligible study universe and the observed evidence subset.
2. Compare availability, reporting, citation, timing, and language patterns across the declared dimensions.
3. Apply design-appropriate diagnostics and record assumptions.
4. Distinguish detected bias, plausible bias, and unassessed domains.

## Output contract

```yaml
produces: [bias_domain_assessments, diagnostic_results, sensitivity_implications, unassessed_domains]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- The denominator for each bias domain is explicit.
- Diagnostics are not used outside their design assumptions.

## Failure and counterexamples

Do not equate small samples with publication bias or treat absence from one index as non-publication.

## Provenance map

- `resolved: knowledge-acquisition-publication-bias-assessment`
- `resolved: bias-detection`
