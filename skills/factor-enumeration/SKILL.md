---
name: factor-enumeration
description: List all key factors, conditions, and assumptions that support or enable
  the artifact's conclusion.
execution: subagent
prompt: ./prompt.md
input: artifact (string), causal_claims (list)
dependencies:
  sops:
  - spawn-agent
---

# Factor Enumeration

Lists all factors that the conclusion depends on — explicit conditions, implicit assumptions, and background requirements.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Comprehensive factor enumeration requires systematic scanning without being biased by which factors seem most important.

## Input

- **artifact**: The artifact to analyze
- **causal_claims**: Previously extracted causal claims (optional)

## Output

- **factors**: List of {name, type, explicit/implicit, suspected_importance}
- **factor_count**: Total factors identified
- **categories**: Grouping of factors by type

## Budget

One unit = one enumeration pass per artifact.
