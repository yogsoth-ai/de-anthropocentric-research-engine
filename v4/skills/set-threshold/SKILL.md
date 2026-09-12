---
name: set-threshold
description: "Define a justified minimum acceptable threshold for each non-compensatory criterion."
---

# set-threshold

## Purpose

Define a justified minimum acceptable threshold for each non-compensatory criterion.

## Input contract

```yaml
required: [criteria, value_domains, decision_context, evidence]
optional: [baseline_distribution, veto_policy, stakeholder_preferences]
constraints: [each threshold lies in the criterion's actual value domain and has an explicit rationale]
```

## Procedure

1. State each criterion's domain, direction, and failure meaning.
2. Gather empirical, structural, and decision-context evidence for a minimum acceptable value.
3. Set the threshold and record rationale, uncertainty, and veto semantics.
4. Return the threshold set for non-compensatory screening.

## Output contract

```yaml
produces: [threshold_set, rationale_by_criterion, veto_policy, uncertainty_notes]
delta_fields: [findings, evidence_updates, decisions, uncertainties]
```

## Quality gates

- Every threshold has a rationale and lies within the criterion's actual value range.
- Thresholds are exposed to downstream screening; they are not hidden in prose.
- Relative thresholds, when used for evidence coverage, declare universe, numerator, denominator, batch increment, stopping reason, source references, direction, and threshold rationale.

## Parameterization

The caller must provide criteria, domains and direction, evidence, baseline distribution if available, minimum-acceptable semantics, and whether the threshold is a veto or ordinary non-compensatory floor.

## Failure and counterexamples

Reject thresholds outside the domain, unsupported by rationale, or treated as compensable weights when the caller specified a veto.

## Provenance map

- resolved: convergence/threshold-setting
- intermediate: Pass4/define-success-criteria

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| convergence/threshold-setting | 13 | gate | Every minimum threshold includes a rationale and lies in the criterion's actual value domain. |

