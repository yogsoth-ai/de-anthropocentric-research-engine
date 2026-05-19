---
name: boundary-probing
description: "Map parameter space, generate extreme values, test at boundaries, detect breakpoints, synthesize validity envelope."
type: tactic
used-by: [adversarial-stress-testing]
strategies: [boundary-enumeration, validity-envelope-mapping, critical-case-design]
---

# Boundary Probing

## Orchestration Steps

1. Receive claim and parameter context from strategy
2. Dispatch `parameter-space-mapping` to identify all dimensions
3. For each dimension, dispatch `extreme-value-generation`:
   - Minimum, maximum, zero, negative, overflow
   - Type boundaries (empty, null, singleton, infinite)
4. Dispatch `breakpoint-detection` at each extreme value
5. Record pass/fail for each probe point
6. Dispatch `validity-envelope-construction` to synthesize boundaries

## Subagents

- parameter-space-mapping
- extreme-value-generation
- breakpoint-detection
- validity-envelope-construction

## Termination Conditions

- All dimensions probed at all boundary values (complete)
- Breakpoint found in critical dimension (early report)
- Budget exhausted (report partial envelope)
- Dimension count exceeds budget (prioritize by sensitivity)
