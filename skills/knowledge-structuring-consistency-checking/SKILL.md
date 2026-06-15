---
name: consistency-checking
description: Tactic for verifying ontology consistency — detect contradictions, cycles,
  orphans, and type violations.
execution: tactic
dependencies:
  sops:
  - gap-detection
  - merge-candidates
---

# Consistency Checking

Verify the ontology is internally consistent. No contradictions, no cycles in hierarchies, no orphaned concepts, no type violations.

## Available SOPs

- wiki-lint-fix — run structural validation
- wiki-graph-query — explore suspicious neighborhoods
- gap-detection — find structural holes
- merge-candidates — identify near-duplicates

## Guiding Principles

- **Contradictions are urgent.** Two edges that contradict each other (A supports B, A contradicts B) must be resolved immediately.
- **Orphans are warnings.** A concept with no edges is suspicious but not necessarily wrong — it may just need connection.
- **Type violations are errors.** An edge type that doesn't make semantic sense (e.g., "question" component_of "source") indicates a classification mistake.
- **Fix root causes.** Don't just remove the symptom — understand why the inconsistency arose.

## Minimum Yield

<HARD-GATE>
≥1 inconsistency identified and resolved per invocation.
If vault_lint returns zero issues and graph inspection finds no problems, report clean state.
</HARD-GATE>
