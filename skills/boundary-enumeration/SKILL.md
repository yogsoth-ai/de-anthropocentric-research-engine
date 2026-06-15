---
name: boundary-enumeration
description: 'Systematic Boundary Value Analysis: identify parameter boundaries, test
  at and beyond limits, detect breakpoints.'
type: strategy
dependencies:
  tactics:
  - boundary-probing
  sops:
  - breakpoint-detection
  - extreme-value-generation
  - parameter-space-mapping
  - stress-test-validity-envelope-construction
---

# Boundary Enumeration

## Tactics

- boundary-probing

## Method

1. Identify all parameter dimensions of the artifact
2. For each dimension, determine nominal range and boundaries
3. Generate test values at boundaries (min, max, min-1, max+1)
4. Test claim validity at each boundary value
5. Record breakpoints where claim fails
6. Synthesize into validity envelope

## Budget

| Size | Parameter dimensions | Values per dimension | Total probes |
|---|---|---|---|
| S | 3 | 4 | 12 |
| M | 6 | 6 | 36 |
| L | 10 | 8 | 80 |

## Orchestration

1. Dispatch `parameter-space-mapping` to identify dimensions
2. Dispatch `extreme-value-generation` for each dimension
3. Dispatch `breakpoint-detection` at each extreme
4. Dispatch `validity-envelope-construction` to synthesize

## Subagents

- parameter-space-mapping
- extreme-value-generation
- breakpoint-detection
- validity-envelope-construction
