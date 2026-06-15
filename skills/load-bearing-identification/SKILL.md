---
name: load-bearing-identification
description: Identify which factors are "load-bearing walls" — factors whose removal
  would collapse the conclusion.
execution: subagent
prompt: ./prompt.md
input: ablation_results (list), necessity_scores (list), sufficiency_scores (list)
dependencies:
  sops:
  - spawn-agent
---

# Load-Bearing Identification

Synthesizes ablation, necessity, and sufficiency results to identify critical factors.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Final synthesis requires weighing multiple evidence streams to produce a definitive ranking.

## Input

- **ablation_results**: Degradation scores from factor removal
- **necessity_scores**: PN scores per factor
- **sufficiency_scores**: PS scores per factor

## Output

- **load_bearing_factors**: Ranked list of critical factors
- **classification**: Each factor classified into necessity-sufficiency quadrant
- **confidence**: Confidence in each classification
- **summary**: Overall structural assessment

## Budget

One unit = one synthesis per campaign run.
