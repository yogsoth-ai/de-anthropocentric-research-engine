---
name: minimal-change-search
description: 'Tactic: Generate candidate changes, detect flip-points where conclusion
  reverses, measure fragility as distance to nearest flip.'
type: tactic
strategies:
- closest-worlds
- thought-experiment
- factor-removal
dependencies:
  sops:
  - causal-claim-extraction
  - counterfactual-scenario-construction
  - factor-enumeration
  - flip-point-detection
  - fragility-measurement
---

# Minimal Change Search Tactic

Find the smallest perturbation that flips the conclusion — closer flip-points mean higher fragility.

## Orchestration

1. **causal-claim-extraction** identifies the conclusion to test
2. **factor-enumeration** generates candidate change dimensions
3. **counterfactual-scenario-construction** builds scenarios with graduated changes
4. **flip-point-detection** binary-searches for the minimal change that flips
5. **fragility-measurement** computes distance from actuality to flip-point
6. Repeat for each dimension within budget
7. Report: nearest flip-point, fragility index, most vulnerable dimension

## Search Strategy

- Start with large changes (clearly flips or clearly holds)
- Binary search between hold/flip boundary
- Record the minimal change magnitude per dimension
- Fragility = 1 / (distance to nearest flip-point)

## Subagents Dispatched

- causal-claim-extraction (conclusion identification)
- factor-enumeration (dimension generation)
- counterfactual-scenario-construction (graduated scenarios)
- flip-point-detection (binary search)
- fragility-measurement (distance computation)

## Termination Conditions

- All dimensions searched within budget
- Flip-point found with distance < threshold (extremely fragile)
- No flip-point found after maximum search depth (robust)
