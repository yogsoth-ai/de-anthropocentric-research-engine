---
name: debate-architect
description: Designs debate structure based on artifact type — selects attack vectors, assigns perspectives, determines escalation ladder, and configures round parameters.
execution: subagent
prompt: ./prompt.md
input: artifact (string), artifact_type (string), budget_size (string), strategy (string)
used-by: [multiagent-debate]
---

# Debate Architect

Designs debate structure and parameters before execution begins.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Structure design requires analyzing the artifact holistically to determine optimal attack angles. Isolated context ensures design is not biased by premature judgment.

## Input

- **artifact**: The artifact to be debated
- **artifact_type**: Type (gap, hypothesis, research-question, idea, approach, experiment-design, claim)
- **budget_size**: S/M/L determining round count and agent count
- **strategy**: Which strategy will execute (critic-defender-judge, society-of-mind, etc.)

## Output

- **attack_vectors**: Ordered list of angles to probe
- **perspectives**: Assigned perspectives (for rotation strategies)
- **escalation_ladder**: Level definitions (for escalation strategies)
- **round_config**: Number of rounds, agents per round, termination thresholds

## Budget

One unit = one structure design per debate.
