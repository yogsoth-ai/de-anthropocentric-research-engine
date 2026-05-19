---
name: categorize-papers
description: Cluster papers by theme, method, or timeline. Produces natural groupings from a paper collection. Used by scoping-survey and narrative-review.
execution: subagent
prompt: ./prompt.md
input: paper_list (string)
used-by: literature-survey, meta-analysis, baseline-establishment
---

# Categorize Papers

Cluster papers by theme/method/timeline into natural groupings.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Categorization requires holding the entire paper collection in context simultaneously to identify patterns and groupings. Subagent provides dedicated space for this comparative analysis.
