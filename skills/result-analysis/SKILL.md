---
name: result-analysis
description: Statistically analyze collected results, verify reproducibility, and
  synthesize findings
version: 1.0.0
category: experiment-execution
type: strategy
sops:
- statistical-testing
- reproducibility-verification
- execution-synthesis
tactics:
- result-validation-loop
dependencies:
  sops:
  - execution-synthesis
  - reproducibility-verification
  - statistical-testing
  tactics:
  - result-validation-loop
---

# Strategy: Result Analysis

**Key Question**: What do the results tell us?

## Methodology

Three-layer analysis combining frequentist, resampling, and Bayesian approaches:

1. **Statistical Testing** — Bootstrap CI, Permutation tests, Bayesian ROPE judgment
2. **Effect Size Calculation** — Cohen's d, Cliff's delta, or domain-appropriate measure
3. **Reproducibility Verification** — Re-run with different seeds, compare distributions
4. **Synthesis** — Integrate findings into actionable conclusions

## Execution Flow

```
[Collected results from experiment-running]
    → statistical-testing (bootstrap/permutation/Bayesian)
        → effect size calculation
            → reproducibility-verification (re-run, compare)
                → execution-synthesis (comprehensive report)
                    → OUTPUT: validated findings with confidence levels
```

## Budget Gate

| Step | Max Budget | Output |
|------|-----------|--------|
| Statistical testing | 8% | Test results with p-values/CIs |
| Reproducibility | 8% | Re-run comparison |
| Synthesis | 4% | Final report |

## Key Decisions

- **Test selection**: 
  - Known distribution → parametric (t-test, ANOVA)
  - Unknown/non-normal → bootstrap CI or permutation test
  - Need practical significance → Bayesian ROPE
- **Reproducibility threshold**: Results must agree within 1 SE across re-runs
- **Effect size interpretation**:
  - Small: d < 0.2 (may not be practically significant)
  - Medium: 0.2 ≤ d < 0.8 (likely meaningful)
  - Large: d ≥ 0.8 (strong effect)
- **ROPE (Region of Practical Equivalence)**: Define before testing, not after

## Integration with Knowledge System

Results feed back into:
- Wiki vault (claims with evidence)
- Future experiment design (what worked, what didn't)
- North star progress tracking

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| result-validation-loop | Validate results through statistical testing, ROPE judgment, reproducibility re-runs, and final synthesis |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| execution-synthesis | Synthesize complete execution report from all results, tests, and reproducibility data |
| reproducibility-verification | Verify result reproducibility via re-runs with different seeds and ICC comparison |
| statistical-testing | Execute statistical tests — bootstrap, permutation, Bayesian ROPE — on experiment results |

<!-- END available-tables (generated) -->
