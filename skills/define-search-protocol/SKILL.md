---
name: define-search-protocol
description: Formalize search queries and inclusion/exclusion criteria for systematic
  surveys. Produces a reproducible search protocol document. Used by systematic-survey.
execution: subagent
prompt: ./prompt.md
input: research_question (string), field_context (string)
dependencies:
  sops:
  - spawn-agent
---

# Define Search Protocol

Formalize search queries + inclusion/exclusion criteria for systematic surveys.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Protocol definition requires careful reasoning about query formulation, Boolean operators, database selection, and criteria boundaries. Dedicated context prevents this analytical work from being rushed.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
