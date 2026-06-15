---
name: systematic-factor-ablation
description: 'Tactic: List all factors, remove one at a time, assess conclusion stability,
  rank factors by load-bearing importance.'
type: tactic
strategies:
- factor-removal
- structural-counterfactual
- necessity-sufficiency
dependencies:
  sops:
  - factor-enumeration
  - fragility-measurement
  - load-bearing-identification
  - single-factor-removal
---

# Systematic Factor Ablation Tactic

Ablation methodology: remove factors individually and measure conclusion degradation.

## Orchestration

1. **factor-enumeration** lists all factors supporting the conclusion
2. **single-factor-removal** removes one factor, reasons about what changes
3. **fragility-measurement** scores degradation (0.0 = no effect, 1.0 = collapse)
4. Repeat steps 2-3 for each factor within budget
5. **load-bearing-identification** ranks factors by degradation score
6. Terminate when all factors tested or budget exhausted

## Scoring

- **0.0–0.2**: Decorative factor (conclusion unaffected)
- **0.2–0.5**: Supporting factor (conclusion weakened but holds)
- **0.5–0.8**: Important factor (conclusion significantly degraded)
- **0.8–1.0**: Load-bearing factor (conclusion collapses without it)

## Subagents Dispatched

- factor-enumeration (initial listing)
- single-factor-removal (per-factor ablation)
- fragility-measurement (degradation scoring)
- load-bearing-identification (final ranking)

## Termination Conditions

- All factors within budget tested
- Early termination if first load-bearing factor found and budget is S
- Saturation: consecutive factors all score below 0.2
