---
name: domain-scoping
description: Strategy for defining ontology boundaries — identify seed concepts, classify
  topic size, establish scope constraints.
execution: strategy
dependencies:
  tactics:
  - concept-decomposition
  - hierarchy-construction
  sops:
  - seed-concept-search
---

# Domain Scoping

Define the boundaries of the ontology. What's in scope, what's out, what are the seed concepts that anchor the domain.

## Guiding Focus

Establish clear boundaries before extraction begins. An unbounded ontology grows without purpose. Seed concepts define the center of gravity; scope constraints define the edges.

## Available Tactics

- concept-decomposition — break broad domains into tractable sub-areas
- hierarchy-construction — establish initial top-level categories

## Budget Slice

| Metric | S | M | L |
|--------|---|---|---|
| Seed concepts identified | 5 | 10 | 20 |
| Scope boundaries defined | 3 | 5 | 8 |
| Source pages surveyed | 5 | 15 | 30 |

## State Ledger Template

```
| Metric              | Target | Current | Status |
|---------------------|--------|---------|--------|
| Seed concepts       | X      | 0       | ⬜     |
| Scope boundaries    | X      | 0       | ⬜     |
| Sources surveyed    | X      | 0       | ⬜     |
```

<HARD-GATE>
Cannot exit until 80% of budget met. Print state ledger before each iteration decision.
</HARD-GATE>

## Adversarial Completeness Probe

After budget gate passes, ask:
- Are there obvious sub-domains I haven't considered?
- Would an expert in this field agree with my scope boundaries?
- Are my seed concepts truly central, or peripheral?

Max 2 extra iterations if gaps found.
