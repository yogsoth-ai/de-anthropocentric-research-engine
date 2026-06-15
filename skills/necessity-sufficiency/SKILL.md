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
