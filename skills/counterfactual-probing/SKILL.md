---
name: counterfactual-probing
description: 'Campaign: Counterfactual reasoning to identify load-bearing factors.
  Core question: If key factors were different, would the conclusion still hold? Methods:
  Pearl SCM Three-Step, Lewis Possible Worlds, Tetlock & Belkin, PNS/PS.'
type: campaign
produces: CounterfactualMap
artifact-types:
- gap
- hypothesis
- research-question
- idea
- approach
- experiment-design
- claim
dependencies:
  strategies:
  - closest-worlds
  - factor-removal
  - necessity-sufficiency
  - structural-counterfactual
  - thought-experiment
  tactics:
  - causal-necessity-testing
  - minimal-change-search
  - systematic-factor-ablation
  sops:
  - context-checkpoint
  - context-init
  - stress-test-saturation-detection
  - verdict-synthesis
---

# Counterfactual Probing Campaign

Core question: **If key factors were different, would the conclusion still hold?**

## Methodology Sources

- Pearl (2000) — Structural Causal Models, Three-Step counterfactual procedure
- Lewis (1973) — Possible Worlds semantics for counterfactuals
- Tetlock & Belkin (1996) — Counterfactual thought experiments in world politics
- Fearon (1991) — Counterfactuals and hypothesis testing in political science
- Williamson (2007) — The Philosophy of Philosophy, thought experiment methodology

## Strategy Routing

| Artifact Type | Primary Strategy | Fallback Strategy |
|---|---|---|
| hypothesis, claim | structural-counterfactual | necessity-sufficiency |
| research-question | thought-experiment | closest-worlds |
| idea, approach | factor-removal | closest-worlds |
| experiment-design | necessity-sufficiency | structural-counterfactual |
| gap | closest-worlds | factor-removal |

## Budget Table

| Parameter | S (Quick) | M (Standard) | L (Deep) |
|---|---|---|---|
| Factors examined | 5 | 10 | 20 |
| Counterfactual scenarios | 3 | 8 | 15 |
| Necessity tests | 3 | 6 | 12 |
| Flip-point search depth | 2 | 4 | 8 |

## Tactics

- **systematic-factor-ablation** — Remove factors one at a time, observe conclusion stability
- **minimal-change-search** — Find smallest change that flips the conclusion
- **causal-necessity-testing** — Evaluate necessity and sufficiency of each causal claim

## Context Management

Each subagent operates in isolated context. Factor enumeration precedes all counterfactual reasoning. Scenarios are constructed with minimal deviation from actuality. Fragility measurements aggregate across all tested factors.

## Output

Produces `CounterfactualMap` containing: load-bearing factors ranked by necessity, fragility index per factor, flip-points identified, robustness assessment, and recommended sensitivity analyses.
