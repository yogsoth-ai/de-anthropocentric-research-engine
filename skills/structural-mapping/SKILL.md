---
name: structural-mapping
description: Map source→target structural correspondences. Identifies corresponding, missing, and extra elements between domains.
execution: subagent
prompt: ./prompt.md
input: source_structure (string), target_domain (string)
used-by: cross-domain-discovery, analogical-transfer, design-by-analogy, bridge-validation
---

# Structural Mapping

Map source→target structural correspondences.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent skill.

## Why Subagent

Structure-mapping requires systematic alignment of relational systems, tracking correspondences at multiple levels simultaneously. Benefits from dedicated working memory to maintain the full mapping table.
