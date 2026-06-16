---
name: gate-criteria-definition
description: Define gate criteria and pass thresholds for a specific stage in the
  Stage-Gate process.
execution: subagent
prompt: ./prompt.md
input: stage, context
dependencies:
  sops:
  - spawn-agent
---

# Gate Criteria Definition

Define explicit, measurable criteria that a candidate must satisfy to pass through a specific stage gate. Each criterion has a pass threshold and evidence requirements.

## Execution

Spawns a subagent that:
1. Receives stage definition and implementation context
2. Identifies appropriate criteria for this gate
3. Sets measurable pass thresholds for each criterion
4. Defines what evidence is required to demonstrate passage
5. Returns structured gate criteria specification

## Why Subagent

Gate criteria must be defined independently of the candidate being evaluated to avoid bias. A dedicated subagent ensures criteria are set based on the stage requirements, not tailored to make a specific candidate pass.

## HARD-GATE

Output MUST include: at least 3 gate criteria, measurable pass threshold for each, and evidence requirements. Reject if criteria are vague or unmeasurable.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
