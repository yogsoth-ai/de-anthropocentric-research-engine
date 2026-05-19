---
name: taxonomy-mapping
description: Construct a hierarchical field map from paper collection — multi-level taxonomy with parent/child relationships, paper counts per node, and maturity indicators. Used by scoping-survey.
execution: subagent
prompt: ./prompt.md
input: paper_collection (string), field_context (string)
used-by: literature-survey
---

# Taxonomy Mapping

Construct a hierarchical field map from a paper collection.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Taxonomy construction requires holding the entire paper collection in context and iteratively refining hierarchical relationships. Dedicated context for this structural analysis.
