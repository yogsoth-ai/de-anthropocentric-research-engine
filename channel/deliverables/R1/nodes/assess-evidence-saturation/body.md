# assess-evidence-saturation

## Purpose

Compare the marginal information gain of a new evidence batch with the comparable prior batch and classify acquisition as continuing, near-saturation, or saturated.

## Input contract

```yaml
required: [current_corpus, prior_comparable_batch, novelty_schema]
optional: [topic_schema, quality_weights, stopping_policy]
constraints: [batches must share a declared universe and comparable novelty calculation]
```

## Procedure

1. Declare the eligible evidence universe, novelty dimensions, and current/prior batch boundaries.
2. Compute new topic, independent-source, condition, or mechanism coverage for each comparable batch.
3. Compare marginal information gain and record the evidence supporting the comparison.
4. Classify continuing, near-saturation, or saturated and state the stopping rationale.

## Output contract

```yaml
produces: [declared_universe, batch_comparison, marginal_gain, saturation_state, stopping_rationale]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- Numerator, denominator, batch increment, source references, direction, and rationale are reproducible.
- The comparison uses the same novelty schema for both batches.
- Saturation is not declared from corpus size alone.

## Failure and counterexamples

Do not compare incomparable batches, count duplicate sources as new information, or treat a low-quality batch as evidence of saturation.

## Provenance map

- `resolved: knowledge-acquisition-saturation-detection`

