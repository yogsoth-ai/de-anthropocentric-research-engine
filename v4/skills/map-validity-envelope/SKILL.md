---
name: map-validity-envelope
description: "Map where a claim, method, or design remains valid by defining variation axes, probing systematic or adversarial/boundary values, detecting breakpoints, and constructing a multidimensional validity envelope. Critical-case selection is an optional inference-maximizing mode."
---

# map-validity-envelope
## Purpose
Map where a claim, method, or design remains valid by defining axes, probing values, detecting breakpoints, and constructing a multidimensional validity envelope.
## Input contract
```yaml
required: [claim_or_method, validity_target, analysis_dimensions]
optional: [baseline_conditions, critical_case_rule, perturbation_budget]
constraints: [axes, values, outcome measure, and breakpoint rule must be explicit]
```
## Execution protocol
1. Define dimensions and values (`define-analysis-dimensions`, `enumerate-dimension-values`).
2. Apply perturbations and select decisive cases (`apply-perturbation`, `select-critical-case`).
3. Detect breakpoints and construct the envelope (`detect-breakpoint`, `construct-validity-envelope`).
4. Analyze scale-dependent regime changes (`analyze-scaling-regime`).
Deviation: use `critical-case` when a decisive case can replace broad probing; otherwise use `systematic-perturbation` or `boundary-value-stress` according to the declared mode and evidence.
## Output contract
```yaml
produces: [dimension_schema, perturbation_records, breakpoints, validity_envelope, critical_case_report, scaling_regime]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```
## Thresholds and quality gates
- Breakpoints require an explicit outcome criterion and before/after evidence.
- Envelope claims must state untested regions and uncertainty.
## Failure and counterexamples
Do not infer an envelope from a single favorable case. Mark extrapolation outside sampled axes as unsupported.
## Provenance map
- concept: validity-envelope-mapping [strategy]
- resolved: systematic-perturbation
- resolved: variation-axis-definition
- resolved: controlled-perturbation
- concept: validity-envelope-construction [sop]
- resolved: adversarial-stress-testing
- concept: validity-envelope-mapping [stress strategy]
- resolved: parameter-space-mapping
- resolved: extreme-value-generation
- resolved: breakpoint-detection
- intermediate: Pass5/validity-envelope-analysis
- intermediate: Pass5/boundary-stress-test
## Preserved source criteria ledger
| source | source line | kind | source criterion |
|---|---:|---|---|
| v4 architecture | modes/calls | structural | Actual modes are `systematic-perturbation`, `boundary-value-stress`, `critical-case`; alias labels are not used. |
## Context checkpoint / Delta notes
Append axes, values, perturbations, breakpoints, envelope, critical cases, scaling findings, and untested regions.

## Mode branches
- `systematic-perturbation`: broad controlled variation across declared axes.
- `boundary-value-stress`: emphasize boundary, pathological, and adversarial values.
- `critical-case`: select inference-maximizing cases and document selection logic.
