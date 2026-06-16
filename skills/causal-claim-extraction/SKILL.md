---
name: causal-claim-extraction
description: Extract all causal claims (X causes Y, X leads to Y, X enables Y) from
  an artifact, producing a structured list of cause-effect pairs.
execution: subagent
prompt: ./prompt.md
input: artifact (string), artifact_type (string)
dependencies:
  sops:
  - spawn-agent
---

# Causal Claim Extraction

Extracts all explicit and implicit causal claims from an artifact.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Causal claim extraction requires careful linguistic analysis of the entire artifact. Isolated context prevents premature evaluation of claims.

## Input

- **artifact**: The artifact to analyze
- **artifact_type**: Type of artifact (gap, hypothesis, claim, etc.)

## Output

- **causal_claims**: List of {cause, effect, strength, evidence, location}
- **causal_graph**: Directed graph of cause-effect relationships
- **claim_count**: Total number of causal claims found

## Budget

One unit = one extraction pass per artifact.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
