---
name: artifact-detection
description: Detect annotation artifacts and shortcuts in benchmarks
execution: tactic
used-by: benchmark-archaeology
---

# Artifact Detection Tactic

Systematically probe benchmarks for annotation artifacts, dataset shortcuts, and spurious correlations that allow models to achieve high scores without the intended capability.

## Stages

### Stage 1: Hypothesis-Only Baseline Test

Search literature for evidence that partial-input baselines achieve unexpectedly high performance:
- Hypothesis-only baselines (NLI without premise)
- Question-only baselines (QA without context)
- Label-word frequency baselines
- Majority-class and surface-pattern baselines

**Search queries**: "[benchmark] annotation artifacts", "[benchmark] hypothesis only", "[benchmark] spurious correlations", "[benchmark] dataset bias"

If published partial-input results exist, record performance gap between partial and full input. Gap < 10 points above random indicates severe artifacts.

### Stage 2: Contrast Set Construction

Identify whether contrast sets or adversarial evaluations exist:
- Search for "[benchmark] contrast sets", "[benchmark] adversarial examples"
- Check if CheckList-style behavioral tests have been applied
- Look for counterfactual data augmentation studies

Record performance drops on contrast sets. Drops > 20 points indicate reliance on surface patterns.

### Stage 3: Format Manipulation Probes

Search for evidence of format sensitivity:
- Prompt template sensitivity studies
- Label name/ordering effects
- Verbalization effects in classification
- Input length correlations with labels

Record whether minor format changes cause disproportionate score changes.

### Stage 4: Conclusion Synthesis

Aggregate evidence into artifact severity assessment:

| Severity | Criteria |
|----------|----------|
| Critical | Partial-input baseline within 5 points of full model |
| High | Contrast set drop >20 points OR format sensitivity >10 points |
| Medium | Known artifacts documented but partial mitigations exist |
| Low | Minor artifacts, full-input still required for high performance |
| None | No evidence of artifacts (may indicate insufficient probing) |

## Output

```yaml
artifact_report:
  benchmark: string
  overall_severity: critical|high|medium|low|none
  partial_input_baselines:
    - input_type: string  # e.g., "hypothesis only"
      performance: float
      full_model_performance: float
      gap: float
      source: string
  contrast_set_results:
    - contrast_set: string
      original_performance: float
      contrast_performance: float
      drop: float
      source: string
  format_sensitivity:
    - manipulation: string
      score_range: string
      source: string
  shortcuts_identified:
    - shortcut: string
      mechanism: string
      exploitability: high|medium|low
  evidence_completeness: thorough|partial|minimal
```

## Yield Report

| Metric | Minimum |
|--------|---------|
| Literature sources checked | 5 |
| Artifact categories probed | 3 |
| Evidence items collected | 4 |
| Severity classification produced | 1 |
