---
name: validity-envelope-mapping
description: Map the complete validity envelope of a claim across all relevant dimensions,
  synthesizing breakpoints into a bounded region.
type: strategy
dependencies:
  tactics:
  - boundary-probing
  - contradiction-derivation
  sops:
  - breakpoint-detection
  - extreme-value-generation
  - parameter-space-mapping
  - stress-test-validity-envelope-construction
---

# Validity Envelope Mapping

## Tactics

- boundary-probing
- contradiction-derivation

## Method

1. Identify all dimensions where claim validity may vary
2. For each dimension, probe from center outward to find boundaries
3. Record transition points (valid -> invalid)
4. Construct multi-dimensional validity envelope
5. Identify the weakest dimensions (narrowest valid range)
6. Report envelope with confidence levels per boundary

## Budget

| Size | Envelope dimensions | Probes per dimension | Resolution |
|---|---|---|---|
| S | 2 | 5 | Coarse |
| M | 4 | 8 | Medium |
| L | 6 | 12 | Fine |

## Orchestration

1. Dispatch `parameter-space-mapping` for full dimension inventory
2. For each dimension, dispatch `extreme-value-generation`
3. Dispatch `breakpoint-detection` with binary search refinement
4. Dispatch `validity-envelope-construction` for final synthesis

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
| contradiction-derivation | Negate a claim, derive logical consequences step by step, detect whether a genuine contradiction or absurdity emerges. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| breakpoint-detection | Test a claim at extreme parameter values and detect the precise point where it breaks down. |
| extreme-value-generation | Generate boundary and extreme test values for a given parameter dimension to stress-test claims. |
| parameter-space-mapping | Identify all parameter dimensions along which a claim's validity might vary. |
| stress-test-validity-envelope-construction | Synthesize breakpoints across dimensions into a coherent validity envelope for a claim. |

<!-- END available-tables (generated) -->
