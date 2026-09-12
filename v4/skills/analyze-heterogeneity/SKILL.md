---
name: analyze-heterogeneity
description: "Identify clinical, methodological, and statistical heterogeneity sources and prioritize subgroup/meta-regression/outlier investigation."
---

# analyze-heterogeneity

## Purpose

Identify clinical, methodological, and statistical heterogeneity sources and prioritize subgroup, meta-regression, or outlier investigation.

## Input contract

```yaml
required: [evidence_records, outcome_schema, comparison_context]
optional: [covariate_schema, effect_estimates, subgroup_hypotheses]
constraints: [heterogeneity claims require record-level conditions and provenance]
```

## Procedure

1. Group records by declared design, population, intervention, outcome, and condition dimensions.
2. Compare effect or performance patterns within and across groups.
3. Identify plausible moderators, outliers, and confounding condition differences.
4. Prioritize subgroup or meta-regression investigations and record uncertainty.

## Output contract

```yaml
produces: [heterogeneity_sources, moderator_candidates, outlier_list, investigation_priorities]
delta_fields: [findings, evidence_updates, uncertainties, open_questions]
```

## Quality gates

- Each heterogeneity source must point to affected records and a comparison dimension.
- Do not infer a moderator from a single discrepant record without an uncertainty marker.

## Failure and counterexamples

Do not label ordinary measurement noise as a causal subgroup effect, and do not pool records whose condition vectors are incomparable.

## Provenance map

- `resolved: heterogeneity-source-analysis`
- `resolved: heterogeneity-investigation`
