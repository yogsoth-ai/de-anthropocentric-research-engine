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

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| boundary-probing | Map parameter space, generate extreme values, test at boundaries, detect breakpoints, synthesize validity envelope. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| breakpoint-detection | Test a claim at extreme parameter values and detect the precise point where it breaks down. |
| extreme-value-generation | Generate boundary and extreme test values for a given parameter dimension to stress-test claims. |
| parameter-space-mapping | Identify all parameter dimensions along which a claim's validity might vary. |
| stress-test-validity-envelope-construction | Synthesize breakpoints across dimensions into a coherent validity envelope for a claim. |

<!-- END available-tables (generated) -->
