---
name: concept-decomposition
description: Tactic for breaking compound concepts into atomic parts — split over-broad
  concepts, identify sub-components, create child pages.
execution: tactic
dependencies:
  sops:
  - alias-resolution
  - concept-page-creation
  - edge-batch-creation
---

# Concept Decomposition

Break compound or over-broad concepts into their atomic constituents. A concept that means too many things should become multiple focused concepts connected by edges.

## Available SOPs

- wiki-search — find existing sub-concepts
- concept-page-creation — create new atomic concept pages
- edge-batch-creation — connect parent to children
- alias-resolution — ensure no naming conflicts

## Guiding Principles

- **Atomic means testable.** If you can't write a one-sentence definition, the concept is too broad.
- **Preserve the parent.** Decomposition creates children; the parent becomes a container (component_of edges).
- **Stop at utility.** Don't decompose below the level where distinctions matter for the research.

## Minimum Yield

<HARD-GATE>
≥2 child concepts created per decomposition invocation.
If a concept cannot be meaningfully decomposed, report it as atomic and exit.
</HARD-GATE>

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| alias-resolution | SOP for detecting and resolving concept aliases — merge duplicate pages, redirect edges. |
| concept-page-creation | SOP for creating a new concept page with proper frontmatter, content, and initial edges. |
| edge-batch-creation | SOP for creating multiple edges in a batch — efficient bulk relationship creation. |

<!-- END available-tables (generated) -->
