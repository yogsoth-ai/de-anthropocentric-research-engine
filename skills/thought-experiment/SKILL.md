---
name: thought-experiment
description: 'Strategy: Williamson-style precise thought experiments — construct carefully
  specified counterfactual scenarios to test whether conclusions depend on contingent
  features.'
type: strategy
tactics:
- minimal-change-search
- causal-necessity-testing
dependencies:
  tactics:
  - causal-necessity-testing
  - minimal-change-search
  sops:
  - causal-claim-extraction
  - counterfactual-scenario-construction
  - factor-enumeration
  - flip-point-detection
  - load-bearing-identification
  - necessity-evaluation
---

# Thought Experiment Strategy

Williamson methodology: construct precise, well-specified counterfactual scenarios that isolate individual variables.

## Method

1. **causal-claim-extraction** identifies the conclusion and its dependencies
2. **factor-enumeration** identifies contingent vs. essential features
3. **counterfactual-scenario-construction** builds precise thought experiments
4. **flip-point-detection** identifies which scenario variations flip the conclusion
5. **necessity-evaluation** determines if flipped factors are genuinely necessary
6. **load-bearing-identification** distinguishes essential from contingent support

## Design Principles

- Scenarios must be internally consistent (no impossible worlds)
- Changes must be minimal and precisely specified
- Background conditions must be held fixed except the target variable
- Conclusions must follow from the scenario, not from intuition pumps

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Thought experiments | 3 | 8 | 15 |
| Variables isolated | 3 | 6 | 12 |
| Scenario precision checks | 1 | 3 | 6 |

## Orchestration

```
causal-claim-extraction → factor-enumeration
→ [for each contingent feature]:
    counterfactual-scenario-construction (precise scenario)
    → flip-point-detection (does conclusion hold?)
    → necessity-evaluation (is this genuinely necessary?)
→ load-bearing-identification (essential vs contingent)
```

## Subagents

- causal-claim-extraction (dependency identification)
- factor-enumeration (contingent feature detection)
- counterfactual-scenario-construction (scenario design)
- flip-point-detection (conclusion testing)
- necessity-evaluation (necessity judgment)
- load-bearing-identification (classification)
