---
name: devils-advocacy
description: Construct the strongest possible counter-argument against a position,
  steelmanning the opposition before attacking.
execution: subagent
prompt: ./prompt.md
input: position (string), context (string)
dependencies:
  sops:
  - spawn-agent
---

# Devil's Advocacy

Constructs the strongest possible case against a given position or assumption.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Devil's advocacy requires full commitment to the opposing position. The agent must genuinely argue against the position without hedging or pulling punches.

## Input

- **position**: The position or assumption to argue against
- **context**: Surrounding context (artifact, domain, prior findings)

## Output

- **counter_argument**: The strongest case against the position
- **evidence**: Supporting evidence for the counter-argument
- **confidence**: How strong the counter-argument actually is (0.0-1.0)
- **fatal_if_true**: Whether the counter-argument would be fatal to the artifact
