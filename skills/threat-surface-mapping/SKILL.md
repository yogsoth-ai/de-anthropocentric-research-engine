---
name: threat-surface-mapping
description: Enumerate all attackable surfaces of an artifact — logical, empirical,
  methodological, social, and practical dimensions.
execution: subagent
prompt: ./prompt.md
input: artifact (string), artifact_type (string)
dependencies:
  sops:
  - spawn-agent
---

# Threat Surface Mapping

Enumerates all surfaces of the artifact that could be attacked or challenged.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Surface enumeration requires systematic coverage without bias toward obvious attack points. Isolated context prevents premature focus on specific vulnerabilities.

## Input

- **artifact**: The complete artifact to analyze
- **artifact_type**: Type of artifact (hypothesis, claim, idea, approach, etc.)

## Output

- **surfaces**: List of threat surfaces with category, description, and attack accessibility rating
- **coverage_map**: Matrix of dimensions covered vs. uncovered
- **priority_ranking**: Surfaces ranked by expected vulnerability

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
