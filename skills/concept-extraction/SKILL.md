---
name: concept-extraction
description: Strategy for mining concepts from sources — systematic extraction, page
  creation, alias resolution.
execution: strategy
dependencies:
  tactics:
  - concept-decomposition
  - knowledge-structuring-consistency-checking
  sops:
  - source-gathering
---

# Concept Extraction

Mine source pages for concepts. Create concept pages, resolve aliases, ensure every concept is properly named and connected.

## Guiding Focus

Extract concepts systematically from sources. Prefer precision over recall — it's better to have 20 well-defined concepts than 50 vague ones. Resolve naming conflicts immediately.

## Available Tactics

- concept-decomposition — break compound concepts into atomic parts
- consistency-checking — verify extracted concepts don't conflict

## Budget Slice

| Metric | S | M | L |
|--------|---|---|---|
| Sources processed | 8 | 20 | 40 |
| Concepts extracted | 12 | 30 | 60 |
| Aliases resolved | 3 | 10 | 20 |

## State Ledger Template

```
| Metric              | Target | Current | Status |
|---------------------|--------|---------|--------|
| Sources processed   | X      | 0       | ⬜     |
| Concepts extracted  | X      | 0       | ⬜     |
| Aliases resolved    | X      | 0       | ⬜     |
```

<HARD-GATE>
Cannot exit until 80% of budget met. Print state ledger before each iteration decision.
</HARD-GATE>

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| concept-decomposition | Tactic for breaking compound concepts into atomic parts — split over-broad concepts, identify sub-components, create child pages. |
| knowledge-structuring-consistency-checking | Tactic for verifying ontology consistency — detect contradictions, cycles, orphans, and type violations. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| source-gathering | SOP for gathering source material relevant to the ontology domain — fetch papers and web pages into source pages. |

<!-- END available-tables (generated) -->
