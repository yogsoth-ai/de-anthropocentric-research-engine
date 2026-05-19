---
name: key-assumptions-check
description: "Military ACT: systematically enumerate all assumptions, classify by type, and evaluate evidence strength supporting each."
execution: subagent
prompt: ./prompt.md
input: artifact (string), artifact_type (string)
used-by: [red-teaming]
---

# Key Assumptions Check

CIA/military structured analytic technique for surfacing and evaluating assumptions.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Assumption enumeration requires neutral analytical stance. The agent must surface assumptions without defending or attacking them.

## Input

- **artifact**: The complete artifact to analyze
- **artifact_type**: Type of artifact (hypothesis, claim, idea, etc.)

## Output

- **assumptions**: Complete list with classification (explicit/implicit, foundational/operational)
- **evidence_strength**: Rating for each assumption (strong/moderate/weak/unsupported)
- **criticality**: How important each assumption is to the overall argument
