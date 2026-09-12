---
name: analyze-temporal-trajectory
description: "Analyze an ordered temporal trajectory, including persistence/narrowing/widening tests, regime changes, inflection points, and optional extrapolation with uncertainty. Entity type, window, and forecast mode are parameters."
---

# analyze-temporal-trajectory

## Purpose

Analyze an ordered temporal trajectory for persistence, narrowing or widening, regime changes, inflection points, and optional uncertain extrapolation.

## Input contract

```yaml
required: [time_indexed_records, entity_type, metric, window]
optional: [forecast_mode, uncertainty_model, grouping_keys, event_markers]
constraints: [records are ordered by time; metric direction is explicit; extrapolation is optional and must carry uncertainty]
```

## Procedure

1. Normalize records by entity, metric, and time index and identify the observed frontier.
2. Fit the caller-selected trajectory representation and inspect residuals and regime changes.
3. Detect inflection points, persistence, narrowing, widening, or stable segments.
4. If forecast mode is enabled, extrapolate with confidence bands and explicit caveats.
5. Return trajectory data, regime annotations, and uncertainty.

## Output contract

```yaml
produces: [trajectory_series, fitted_model, inflection_points, regime_labels, forecast, uncertainty_notes]
delta_fields: [findings, evidence_updates, decisions, uncertainties]
```

## Quality gates

- Preserve source minimum yield where the progress-curve mode applies: 2 progress curves, 3 years of history, 1 inflection point, and 2 headroom estimates.
- Retain filing time series, lifecycle/S-curve fitting, historical SOTA curve fitting, milestone projection with confidence intervals, and 2/5/10-year persistence-window comparisons when those modes are requested.
- Forecasts must state model, time window, confidence band, and uncertainty; do not turn a trend into a causal claim.

## Parameterization

The caller must provide the entity schema, time window, metric and direction, grouping keys, frontier rule, model/forecast mode, uncertainty method, and event markers. For persistence testing provide the requested windows; for filing or SOTA analysis provide dates and comparable score records.

## Failure and counterexamples

Reject unsorted or incomparable records, forecasts without uncertainty, or regime labels unsupported by the observed series. Do not infer a future milestone when the metric definition changes across time.

## Provenance map

- resolved: knowledge-acquisition/trend-analysis
- resolved: knowledge-acquisition/progress-curve-fitting
- resolved: knowledge-acquisition/progress-curve-fitting
- resolved: knowledge-acquisition/progress-curve-construction
- resolved: experiment-execution/timeline-projection
- intermediate: Pass3/analyze-filing-trend
- intermediate: Pass3/fit-research-progress-curve
- intermediate: Pass3/project-research-timeline
- resolved: deep-insight/temporal-sensitivity-testing

## Verbatim source criteria excerpts

- `progress-curve-construction` lines 66-69: Progress curves constructed 2; years of history covered 3; inflection points identified 1; headroom estimates produced 2.
- `progress-curve-construction` lines 50 and 60: Annotated inflection points with causal attribution; headroom estimates with confidence intervals.

## Preserved source criteria ledger

| source | physical line | kind | source criterion |
|---|---:|---|---|
| knowledge-acquisition/progress-curve-construction | 46 | numeric | Minimum yield: 2 progress curves, 3 years history, 1 inflection point, 2 headroom estimates. |
| deep-insight/temporal-sensitivity-testing | 12 | structural | Test persistence across the caller-supplied time windows and classify narrowing, widening, or stable. |
