# characterize-anomaly

## Purpose

Characterize an observation that departs from an expected pattern and separate signal from measurement or protocol artifact.

## Input contract

```yaml
required: [observation, reference_pattern, condition_records]
optional: [uncertainty_estimates, replication_records, artifact_hypotheses]
constraints: [anomaly status requires a defined comparison and condition context]
```

## Procedure

1. Define the expected pattern and comparison basis.
2. Quantify the departure with uncertainty and condition alignment.
3. Test plausible data, protocol, and mechanism explanations.
4. Classify the anomaly and identify discriminating follow-up evidence.

## Output contract

```yaml
produces: [anomaly_description, comparison_basis, explanation_set, discriminating_evidence]
delta_fields: [findings, evidence_updates, uncertainties, recommended_jumps]
```

## Quality gates

- The reference pattern and departure measure are explicit.
- Artifact explanations are checked before causal interpretations.

## Failure and counterexamples

Do not label a rare value anomalous without a comparison distribution or ignore changed measurement conditions.

## Provenance map

- `resolved: characterize-anomaly`

