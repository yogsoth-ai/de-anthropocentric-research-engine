---
name: hierarchy-construction
description: Tactic for building is-a and part-of hierarchies — establish parent-child
  relationships, verify transitivity, detect cycles.
execution: tactic
dependencies:
  sops:
  - edge-batch-creation
  - gap-detection
  - hierarchy-visualization
  tactics:
  - knowledge-structuring-consistency-checking
---

# Hierarchy Construction

Build taxonomic hierarchies using component_of and instance_of edges. Ensure hierarchies are acyclic, transitive, and complete.

## Available SOPs

- edge-batch-creation — create hierarchy edges in bulk
- hierarchy-visualization — inspect current hierarchy structure
- gap-detection — find missing intermediate levels
- consistency-checking (tactic, peer) — verify no cycles

## Guiding Principles

- **Acyclic always.** A cycle in a hierarchy is a logical error. Detect and break immediately.
- **Intermediate levels matter.** Jumping from "machine learning" directly to "Adam optimizer" skips useful structure.
- **Multiple inheritance is fine.** A concept can belong to multiple parents (component_of multiple things).
- **Depth ≤ 5.** Hierarchies deeper than 5 levels are usually over-specified.

## Minimum Yield

<HARD-GATE>
≥3 hierarchy edges created per invocation.
If the hierarchy is already complete for the current scope, report and exit.
</HARD-GATE>

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| knowledge-structuring-consistency-checking | Tactic for verifying ontology consistency — detect contradictions, cycles, orphans, and type violations. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| edge-batch-creation | SOP for creating multiple edges in a batch — efficient bulk relationship creation. |
| gap-detection | SOP for finding structural gaps in the ontology — missing concepts, thin branches, disconnected clusters. |
| hierarchy-visualization | SOP for inspecting the current hierarchy structure — query graph to display parent-child relationships. |

<!-- END available-tables (generated) -->
