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

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
