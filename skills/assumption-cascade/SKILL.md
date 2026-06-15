---
name: assumption-cascade
description: 'Tactic: Surface assumptions, sort by dependency, attack root assumptions
  first, then trace cascade failures through the dependency graph.'
type: tactic
strategies:
- assumption-challenge
- systematic-probing
- groupthink-mitigation
dependencies:
  sops:
  - assumption-cascade-tracer
  - devils-advocacy
  - finding-aggregation
  - key-assumptions-check
  - probe-execution
---

# Assumption Cascade Tactic

Attack assumptions at their roots and trace how failures propagate through dependency chains.

## Orchestration

1. **key-assumptions-check** surfaces all assumptions (explicit and implicit)
2. **assumption-cascade-tracer** builds dependency graph (which assumptions depend on which)
3. Root assumptions identified (those with no upstream dependencies)
4. **devils-advocacy** constructs strongest attack against each root assumption
5. **probe-execution** tests root assumptions — if root fails, trace downstream cascade
6. **assumption-cascade-tracer** maps full cascade: which conclusions collapse if root fails
7. **finding-aggregation** reports cascade paths and total impact scope

## Subagents Dispatched

- key-assumptions-check (1 call for enumeration)
- assumption-cascade-tracer (2 calls: dependency build + cascade trace)
- devils-advocacy (1 call per root assumption)
- probe-execution (1 call per root attack)
- finding-aggregation (1 call at end)

## Termination Conditions

- All root assumptions tested (budget permitting)
- Cascade found that invalidates >50% of conclusions (critical finding)
- All assumptions survive attack (artifact resilient at assumption level)
- Budget exhausted (report partial coverage)
