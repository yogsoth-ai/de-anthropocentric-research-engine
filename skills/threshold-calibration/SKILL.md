---
name: threshold-calibration
description: Systematically sweep consensus thresholds to observe which items achieve consensus at what level, producing a threshold-consensus curve.
execution: tactic
used-by: structured-consensus
---

# Threshold Calibration

Systematically vary the consensus threshold to understand the sensitivity of consensus classification. Rather than picking a single arbitrary threshold, sweep across a range to see which items are robust consensus (agree at any threshold) vs. fragile (only consensus at lenient thresholds).

## Stages

1. **Sweep** — Run `threshold-sweep` to compute consensus status at multiple threshold levels
2. **Classify** — Run `consensus-classification` to categorize items at the chosen operating threshold
3. **Measure** — Run `consensus-measurement` to validate final consensus scores

## Available SOPs

| SOP | Role in Tactic |
|-----|---------------|
| threshold-sweep | Compute consensus at multiple threshold levels, produce curve |
| consensus-classification | Classify items as consensus/dissensus at operating threshold |
| consensus-measurement | Validate final consensus scores with appropriate method |

## Execution Guidance

- Sweep range should cover 50%–90% agreement (or IQR 0.5–2.0)
- Identify "knee" in the curve where many items flip classification
- Robust consensus items (agree at strict thresholds) are highest confidence
- Fragile items (only consensus at lenient thresholds) need flagging
- Report both the curve and the classification at the chosen operating point

## Minimum Yield

- Threshold-consensus curve (threshold vs. number-of-consensus-items curve)
- Classification results (classification at operating threshold: consensus items, dissensus items)
