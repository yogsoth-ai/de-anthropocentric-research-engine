---
name: necessity-evaluation
description: Evaluate the probability of necessity (PN) for a causal factor — would
  the conclusion fail if this factor were absent?
execution: subagent
prompt: ./prompt.md
input: artifact (string), factor (string), conclusion (string)
dependencies:
  sops:
  - spawn-agent
---

# Necessity Evaluation

Scores probability of necessity: P(Y would not hold | X absent).

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Necessity evaluation requires careful counterfactual reasoning about absence, isolated from sufficiency judgments.

## Input

- **artifact**: The original artifact
- **factor**: The factor to evaluate for necessity
- **conclusion**: The conclusion that may depend on this factor

## Output

- **pn_score**: Probability of necessity (0.0–1.0)
- **reasoning**: Why this factor is/isn't necessary
- **alternative_paths**: Other ways the conclusion could hold without this factor
- **confidence**: Confidence in the PN estimate

## Budget

One unit = one necessity evaluation per factor.
