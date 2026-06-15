---
name: attack-vector-generation
description: Generate specific attack strategies for a given threat surface, producing
  concrete probes that can be executed.
execution: subagent
prompt: ./prompt.md
input: surface (string), artifact (string), prior_findings (string)
dependencies:
  sops:
  - spawn-agent
---

# Attack Vector Generation

Generates concrete, executable attack vectors targeting a specific threat surface.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Vector generation requires creative adversarial thinking without defensive contamination. Each surface needs fresh attack ideation.

## Input

- **surface**: The specific threat surface to target (from threat-surface-mapping)
- **artifact**: The artifact being attacked
- **prior_findings**: Results from previous probes (to avoid repetition)

## Output

- **vectors**: List of specific attack vectors with description, expected outcome, and severity estimate
- **priority_order**: Recommended execution order (highest-impact first)
- **follow_up_triggers**: Conditions that should trigger deeper investigation

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
