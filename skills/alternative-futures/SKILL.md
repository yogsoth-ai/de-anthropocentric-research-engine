---
name: alternative-futures
description: Generate 2-4 divergent scenarios from the same evidence base, each representing
  a plausible alternative to the artifact's conclusions.
execution: subagent
prompt: ./prompt.md
input: artifact (string), evidence_base (string)
dependencies:
  sops:
  - spawn-agent
---

# Alternative Futures

Generates multiple competing scenarios to challenge the dominant narrative.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Alternative generation requires creative divergent thinking without anchoring on the artifact's conclusions. Isolated context prevents confirmation bias.

## Input

- **artifact**: The artifact whose conclusions are being challenged
- **evidence_base**: The evidence available (same evidence, different interpretations)

## Output

- **alternatives**: 2-4 divergent scenarios, each internally consistent
- **discriminators**: Observable indicators that would distinguish between alternatives
- **plausibility_ranking**: Relative plausibility of each alternative vs. the artifact's conclusion
