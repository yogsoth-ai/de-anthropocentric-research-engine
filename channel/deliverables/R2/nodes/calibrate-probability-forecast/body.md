# calibrate-probability-forecast
## Purpose
Aggregate probabilistic forecasts, compare them with outcomes, and recalibrate without hiding unresolved forecaster disagreement.
## Input contract
```yaml
required: [forecast_records, outcome_records, calibration_rule]
optional: [forecaster_metadata, prior_calibration, aggregation_method]
constraints: [each forecast has a target, probability, timestamp, horizon, and provenance]
```
## Procedure
1. Align forecasts with realized outcomes at the declared horizon and freeze the evaluation set.
2. Compute calibration evidence by probability band and forecaster, preserving sample size and missing outcomes.
3. Update the aggregation or calibration rule only where outcome-linked error supports the change.
4. Emit recalibrated probabilities, calibration diagnostics, disagreement intervals, and the next review trigger.
## Output contract
```yaml
produces: [calibrated_forecasts, calibration_diagnostics, disagreement_report, review_trigger]
delta_fields: [findings, evidence_updates, hypothesis_updates, uncertainties, decisions, open_questions]
```
## Quality gates
- A-class gate: declared universe = all closed forecasts in the evaluation horizon; numerator = forecasts with outcome linkage and valid timestamp/probability; batch increment = one closed forecast; stopping reason = calibration error stabilizes or the closed set is exhausted; source references = forecast/outcome IDs and calibration runs; direction/threshold reason = recalibration moves probabilities toward observed frequencies only when the declared scoring rule shows systematic error.
- Never collapse unresolved disagreement into a single certainty value.
## Failure and counterexamples
Do not score forecasts whose outcomes are not yet observable. A changed probability without new outcome-linked evidence is a model revision, not calibration.
## Provenance map
- resolved: futures-calibration
