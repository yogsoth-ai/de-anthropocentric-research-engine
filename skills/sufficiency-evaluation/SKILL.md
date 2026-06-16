---
name: sufficiency-evaluation
description: Evaluate the probability of sufficiency (PS) for a causal factor — would
  this factor alone be enough to produce the conclusion?
execution: subagent
prompt: ./prompt.md
input: artifact (string), factor (string), conclusion (string)
dependencies:
  sops:
  - spawn-agent
---

# Sufficiency Evaluation

Scores probability of sufficiency: P(Y would hold | only X present).

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Sufficiency evaluation requires reasoning about isolated factor power, separate from necessity judgments.

## Input

- **artifact**: The original artifact
- **factor**: The factor to evaluate for sufficiency
- **conclusion**: The conclusion to test

## Output

- **ps_score**: Probability of sufficiency (0.0–1.0)
- **reasoning**: Why this factor is/isn't sufficient alone
- **missing_requirements**: What else would be needed
- **confidence**: Confidence in the PS estimate

## Budget

One unit = one sufficiency evaluation per factor.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
