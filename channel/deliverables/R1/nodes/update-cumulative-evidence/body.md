# update-cumulative-evidence

## Purpose

Update a cumulative evidence estimate or ordering as new studies or evidence blocks arrive and detect material inference change over time.

## Input contract

```yaml
required: [prior_estimate, new_evidence_block, estimand]
optional: [prior_data, heterogeneity_model, time_field, sensitivity_plan]
constraints: [new evidence must be linked to the same estimand or an explicit comparability change]
```

## Procedure

1. Validate the new block against the cumulative evidence schema and estimand.
2. Update the cumulative estimate, uncertainty, and evidence ordering.
3. Compare the update with the prior state and identify material changes.
4. Record time coverage, independent-study coverage, and unresolved dependence.

## Output contract

```yaml
produces: [updated_cumulative_estimate, change_summary, uncertainty_update, time_coverage, independence_coverage]
delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- Prior and updated states are directly comparable.
- New evidence is not double-counted through shared data or duplicate reports.
- Sequential stopping uses relative time coverage, estimate stability, independent-study coverage, and a stated threshold rationale.

## Failure and counterexamples

Do not treat a numerical update as substantive change without uncertainty comparison or mix changing estimands into one cumulative series.

## Provenance map

- `concept: knowledge-acquisition/meta-analysis/cumulative-tracking`

