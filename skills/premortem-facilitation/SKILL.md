---
name: premortem-facilitation
description: Execute Klein pre-mortem protocol — assume failure has occurred, generate plausible failure scenarios through prospective hindsight.
execution: subagent
prompt: ./prompt.md
input: artifact (string), artifact_type (string), budget (string)
used-by: [failure-anticipation]
---

# Pre-Mortem Facilitation

Executes the Klein (2007) pre-mortem protocol to generate failure scenarios.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Pre-mortem requires adopting a specific temporal frame (future failure as fact). Isolated context prevents contamination from optimistic bias.

## Input

- **artifact**: The artifact to analyze
- **artifact_type**: Type classification for tailored prompting
- **budget**: S/M/L controlling scenario count

## Output

- **scenarios**: List of plausible failure scenarios with narrative descriptions
- **plausibility_ranking**: Ordered by perceived likelihood
