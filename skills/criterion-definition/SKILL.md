---
name: criterion-definition
description: Extract evaluation criteria from research goals and candidate alternatives.
execution: subagent
prompt: ./prompt.md
input: research_goal (string), candidates (string[])
used-by: multi-criteria-scoring
---

# Criterion Definition

Extract structured evaluation criteria from research goals and candidate alternatives, ensuring criteria are complete, mutually exclusive, and measurable.

## Execution

Subagent receives research goals and candidate list, outputs a standardized set of evaluation criteria.

## Why Subagent

Criteria extraction requires domain knowledge reasoning and completeness checking; independent context avoids interference from candidate details.

## HARD-GATE

Output criteria count must be between 3-12, and each criterion must include name, definition, unit of measurement, and direction (higher-is-better / lower-is-better).
