---
name: assumption-excavation
description: Systematic extraction, challenge, and sensitivity analysis of assumptions
  underlying a decision to identify load-bearing beliefs.
execution: tactic
dependencies:
  sops:
  - conclusion-sensitivity
  - convergence-assumption-challenge
  - convergence-assumption-extraction
---

# Assumption Excavation

A three-phase tactic that surfaces hidden assumptions, challenges each one adversarially, and maps which assumptions are load-bearing for the conclusion. Decisions often rest on unstated beliefs — this tactic makes them explicit and tests their strength.

## Stages

1. **Assumption Extraction** — Systematically surface all assumptions underlying the decision, with confidence levels
2. **Assumption Challenge** — For each assumption, construct the strongest counter-argument and identify alternatives
3. **Conclusion Sensitivity** — Map which assumptions, if wrong, would change the conclusion

## Available SOPs

| SOP | Phase | Purpose |
|-----|-------|---------|
| assumption-extraction | Extract | Surface hidden assumptions with confidence |
| assumption-challenge | Challenge | Attack each assumption adversarially |
| conclusion-sensitivity | Sensitivity | Map load-bearing assumptions |

## Execution Guidance

- Extract minimum 5 assumptions per decision
- Challenge ALL assumptions, not just obvious ones
- Confidence levels: HIGH (>80%), MEDIUM (50-80%), LOW (<50%)
- Critical assumption = conclusion changes if assumption is wrong
- Focus mitigation efforts on critical + low-confidence assumptions

## Minimum Yield

- >= 5 assumptions extracted with confidence levels
- Challenge argument for each assumption
- Alternative assumption for each (what if the opposite is true?)
- Sensitivity map showing which assumptions are critical
- List of critical assumptions requiring mitigation

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| conclusion-sensitivity | Map which assumptions are load-bearing by assessing how the conclusion changes if each assumption fails. |
| convergence-assumption-challenge | Construct the strongest counter-argument against a specific assumption and propose alternatives. |
| convergence-assumption-extraction | Systematically surface hidden assumptions underlying a decision with confidence levels. |

<!-- END available-tables (generated) -->
