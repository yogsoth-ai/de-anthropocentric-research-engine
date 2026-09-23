---
name: analyze-leaderboard-dynamics
description: "Analyze leaderboard score distributions, compression/saturation, anomalies, selective reporting, and regime shifts."
---

# analyze-leaderboard-dynamics

## Purpose

Analyze leaderboard score distributions, compression or saturation, anomalies, selective reporting, and regime shifts.

## Input contract

```yaml
required: [leaderboard_records, metric_schema, time_or_version_field]
optional: [evaluation_protocols, source_quality, method_metadata]
constraints: [scores require task, metric, condition, source, and observation provenance]
```

## Procedure

1. Normalize scores and evaluation conditions into comparable groups.
2. Inspect distributions, rank movement, compression, and missingness.
3. Identify anomalies, selective reporting, and regime changes.
4. State whether additional evidence is continuing, near-saturated, or saturated.

## Output contract

```yaml
produces: [leaderboard_distribution, regime_segments, anomaly_report, saturation_assessment]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```

## Quality gates

- Every reported regime or anomaly must cite the records and comparison basis.
- Do not compare scores across incompatible protocols without an explicit limitation.

## Failure and counterexamples

Do not treat rank order as progress when metric definitions or evaluation conditions changed; preserve ties and missing observations.

## Provenance map

- `resolved: leaderboard-dynamics-analysis`
