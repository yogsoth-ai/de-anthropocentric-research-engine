---
name: necessity-sufficiency
description: 'Strategy: Probability of Necessity and Sufficiency (PNS/PS) — systematically
  evaluate whether each factor is necessary, sufficient, both, or neither for the
  conclusion.'
type: strategy
tactics:
- causal-necessity-testing
- systematic-factor-ablation
dependencies:
  tactics:
  - causal-necessity-testing
  - systematic-factor-ablation
  sops:
  - causal-claim-extraction
  - factor-enumeration
  - load-bearing-identification
  - necessity-evaluation
  - single-factor-removal
  - sufficiency-evaluation
---

# Necessity-Sufficiency Strategy

PNS/PS framework: classify each factor by its causal role — necessary, sufficient, both, or neither.

## Method

1. **causal-claim-extraction** identifies all causal claims
2. **factor-enumeration** lists candidate causes
3. **necessity-evaluation** tests: would conclusion fail WITHOUT this factor? (PN)
4. **sufficiency-evaluation** tests: would this factor ALONE produce conclusion? (PS)
5. **single-factor-removal** provides evidence for necessity judgments
6. **load-bearing-identification** classifies factors into quadrants

## Classification Quadrants

- **Necessary + Sufficient**: Load-bearing walls (removal collapses conclusion)
- **Necessary + Not Sufficient**: Required but not enough alone
- **Not Necessary + Sufficient**: Redundant paths to conclusion
- **Neither**: Decorative factors (safe to vary)

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| Factors tested | 5 | 10 | 20 |
| Necessity evaluations | 3 | 6 | 12 |
| Sufficiency evaluations | 3 | 6 | 12 |

## Orchestration

```
causal-claim-extraction → factor-enumeration
→ [for each factor]:
    necessity-evaluation (PN score)
    + sufficiency-evaluation (PS score)
    + single-factor-removal (supporting evidence)
→ load-bearing-identification (quadrant classification)
```

## Subagents

- causal-claim-extraction (claim identification)
- factor-enumeration (candidate listing)
- necessity-evaluation (PN scoring)
- sufficiency-evaluation (PS scoring)
- single-factor-removal (evidence generation)
- load-bearing-identification (classification)

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| causal-necessity-testing | Tactic: Extract causal claims, evaluate probability of necessity (PN) and sufficiency (PS) for each, classify into necessity-sufficiency quadrants. |
| systematic-factor-ablation | Tactic: List all factors, remove one at a time, assess conclusion stability, rank factors by load-bearing importance. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| causal-claim-extraction | Extract all causal claims (X causes Y, X leads to Y, X enables Y) from an artifact, producing a structured list of cause-effect pairs. |
| factor-enumeration | List all key factors, conditions, and assumptions that support or enable the artifact's conclusion. |
| load-bearing-identification | Identify which factors are "load-bearing walls" — factors whose removal would collapse the conclusion. |
| necessity-evaluation | Evaluate the probability of necessity (PN) for a causal factor — would the conclusion fail if this factor were absent? |
| single-factor-removal | Remove one specified factor from the artifact's support structure and reason about how the conclusion changes. |
| sufficiency-evaluation | Evaluate the probability of sufficiency (PS) for a causal factor — would this factor alone be enough to produce the conclusion? |

<!-- END available-tables (generated) -->
