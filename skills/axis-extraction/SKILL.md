---
name: axis-extraction
description: Tactic for systematically extracting axes of variation from literature
  — identify how practitioners compare approaches.
execution: tactic
dependencies:
  sops:
  - axis-validation
  - dimension-page-creation
---

# Axis Extraction

Systematically extract axes of variation from literature. Look for how authors compare methods, what trade-offs they discuss, what design choices they highlight.

## Available SOPs

- dimension-page-creation — create pages for identified dimensions
- axis-validation — verify axes are independent and meaningful
- wiki-search — check for existing dimension coverage

## Guiding Principles

- **Comparison reveals axes.** When authors say "method A is X while method B is Y", X-Y is likely a dimension.
- **Trade-offs are dimensions.** "You can have speed or accuracy" reveals the speed-accuracy dimension.
- **Taxonomies are pre-built axes.** Existing classifications in the field are validated dimensions.
- **Independence test.** If changing one axis always changes another, they're not independent.

## Minimum Yield

<HARD-GATE>
≥2 candidate axes identified per invocation with independence assessment.
</HARD-GATE>

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| axis-validation | SOP for validating that candidate axes are independent and meaningful. |
| dimension-page-creation | SOP for creating a dimension page — documents an axis of variation with its values and semantics. |

<!-- END available-tables (generated) -->
