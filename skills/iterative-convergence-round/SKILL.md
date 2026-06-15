---
name: iterative-convergence-round
description: Execute one full Delphi round — collect judgments, distribute anonymous
  feedback, measure consensus, decide whether to continue.
execution: tactic
dependencies:
  sops:
  - consensus-measurement
  - feedback-distribution
  - judgment-collection
  - round-decision
---

# Iterative Convergence Round

Execute one complete iteration of the Delphi convergence cycle: collect independent judgments from all perspectives, distribute anonymized feedback showing the group distribution, allow revision, measure consensus level, and decide whether another round is needed.

## Stages

1. **Collect** — Run `judgment-collection` to gather independent ratings/estimates from each perspective
2. **Feedback** — Run `feedback-distribution` to create anonymized summary of group responses
3. **Measure** — Run `consensus-measurement` to compute agreement level (IQR, % agreement, Kendall's W)
4. **Decide** — Run `round-decision` to determine continue/stop based on threshold and stability

## Available SOPs

| SOP | Role in Tactic |
|-----|---------------|
| judgment-collection | Gather independent judgments from all perspectives |
| feedback-distribution | Create and distribute anonymized feedback report |
| consensus-measurement | Compute consensus score using appropriate method |
| round-decision | Determine whether to run another round or stop |

## Execution Guidance

- Judgments MUST be collected independently (no cross-contamination)
- Feedback MUST be anonymized (no attribution to specific perspectives)
- Consensus measurement method should match data type (IQR for continuous, % for categorical)
- Stop conditions: consensus threshold met OR stability detected OR max rounds reached
- If stopping without consensus, document which items remain unresolved

## Minimum Yield

- Consensus items list (items that reached consensus)
- Non-consensus items (items that did not converge, with reasons)
- Round log (round-by-round progression of scores)
