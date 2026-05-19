---
name: define-search-protocol
description: Formalize search queries and inclusion/exclusion criteria for systematic surveys. Produces a reproducible search protocol document. Used by systematic-survey.
execution: subagent
prompt: ./prompt.md
input: research_question (string), field_context (string)
used-by: literature-survey
---

# Define Search Protocol

Formalize search queries + inclusion/exclusion criteria for systematic surveys.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Protocol definition requires careful reasoning about query formulation, Boolean operators, database selection, and criteria boundaries. Dedicated context prevents this analytical work from being rushed.
