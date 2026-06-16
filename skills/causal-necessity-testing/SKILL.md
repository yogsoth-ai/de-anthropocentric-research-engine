---
name: causal-necessity-testing
description: 'Tactic: Extract causal claims, evaluate probability of necessity (PN)
  and sufficiency (PS) for each, classify into necessity-sufficiency quadrants.'
type: tactic
strategies:
- necessity-sufficiency
- structural-counterfactual
- thought-experiment
dependencies:
  sops:
  - causal-claim-extraction
  - load-bearing-identification
  - necessity-evaluation
  - sufficiency-evaluation
---

# Causal Necessity Testing Tactic

PNS evaluation: for each causal claim, determine whether the cause is necessary, sufficient, both, or neither.

## Orchestration

1. **causal-claim-extraction** extracts all X→Y causal claims from the artifact
2. **necessity-evaluation** asks: if X had NOT occurred, would Y still hold? (PN)
3. **sufficiency-evaluation** asks: if X occurred in isolation, would Y follow? (PS)
4. Classify each claim into quadrant:
   - PN high + PS high → INUS condition (load-bearing)
   - PN high + PS low → necessary but not sufficient
   - PN low + PS high → sufficient but redundant
   - PN low + PS low → spurious or decorative
5. **load-bearing-identification** synthesizes quadrant assignments

## Scoring

- PN and PS scored 0.0–1.0 (probability estimates)
- Threshold for "high": >= 0.7
- Threshold for "low": < 0.3
- Middle range (0.3–0.7): uncertain, flag for deeper investigation

## Subagents Dispatched

- causal-claim-extraction (claim identification)
- necessity-evaluation (PN scoring per claim)
- sufficiency-evaluation (PS scoring per claim)
- load-bearing-identification (quadrant synthesis)

## Termination Conditions

- All extracted claims evaluated within budget
- Early termination if INUS condition found and budget is S
- All claims score PN < 0.3 (no necessary factors found — conclusion may be overdetermined)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| causal-claim-extraction | Extract all causal claims (X causes Y, X leads to Y, X enables Y) from an artifact, producing a structured list of cause-effect pairs. |
| load-bearing-identification | Identify which factors are "load-bearing walls" — factors whose removal would collapse the conclusion. |
| necessity-evaluation | Evaluate the probability of necessity (PN) for a causal factor — would the conclusion fail if this factor were absent? |
| sufficiency-evaluation | Evaluate the probability of sufficiency (PS) for a causal factor — would this factor alone be enough to produce the conclusion? |

<!-- END available-tables (generated) -->
