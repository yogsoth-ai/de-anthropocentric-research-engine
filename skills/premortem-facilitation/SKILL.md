---
name: premortem-facilitation
description: Execute Klein pre-mortem protocol — assume failure has occurred, generate
  plausible failure scenarios through prospective hindsight.
execution: subagent
prompt: ./prompt.md
input: artifact (string), artifact_type (string), budget (string)
dependencies:
  sops:
  - spawn-agent
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

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
