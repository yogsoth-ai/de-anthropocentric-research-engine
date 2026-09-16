---
name: audit-convergence-independence
description: "Audit claims of independent convergence by tracing shared priors, data, framing, models, prompts, assumptions, or upstream evidence; estimate an effective independent evidence count rather than treating nominal N paths as independent."
---

# audit-convergence-independence
## Purpose
Estimate how much nominally independent convergence remains after shared priors, data, models, prompts, framings, assumptions, and upstream evidence are discounted.
## Input contract
```yaml
mode_contracts:
  evidence-paths: &convergence_audit_input
    required: [evidence_paths, claims, provenance_records]
    optional: [dependency_schema, correlation_estimates]
    constraints: [each_path_must_be_traceable_to_its_inputs_and_assumptions]
  agents: *convergence_audit_input
  models: *convergence_audit_input
  methods: *convergence_audit_input
```
## Execution protocol
Do not perform called SOP operations inline; each loaded SOP owns its contract and thresholds.

1. You MUST load skill `identify-shared-priors` to enumerate paths, provenance, and shared priors.
2. You MUST load skill `verify-evidence-independence` to verify independence and mark shared dependencies.
3. You MUST load skill `estimate-effective-evidence-count` to estimate the effective evidence count. You MUST load skill `assess-sensitivity` to perturb dependence assumptions.
Deviation: use qualitative dependence classes when numeric correlation is unavailable; never count nominal paths as independent by default.
## Output contract
```yaml
mode_contracts:
  evidence-paths: &convergence_audit_output
    produces: [independence_ledger, effective_evidence_count, common_cause_framing, independent_path_result_or_design, correlated_errors, corrected_confidence_statement]
    delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
  agents: *convergence_audit_output
  models: *convergence_audit_output
  methods: *convergence_audit_output
```
## Thresholds and quality gates
- A-class sufficiency: declared universe = all claimed evidence/reasoning paths; numerator = paths with complete provenance and independence assessment; batch increment = one newly traced path; stopping reason = effective count stabilizes or remaining paths are dependent/irrelevant; source references = path IDs, source IDs, model/prompt IDs; direction/threshold reason = lower effective count when shared dependencies increase.
- Report nominal N and N_eff separately.
## Failure and counterexamples
Do not call repeated use of the same dataset, model, prompt, or source independent. Mark N_eff uncertain when dependence cannot be resolved.
## Provenance map
- resolved: independent-convergence-audit
## Preserved source criteria ledger
| source | source line | kind | source criterion |
|---|---:|---|---|
| v4 architecture | node desc | textual | Trace shared priors and estimate effective independent evidence count. |
## Context checkpoint / Delta notes
Append path provenance, shared dependencies, N, N_eff, uncertainty, and sensitivity assumptions.

## Mode branches
- `evidence-paths`: compare source and reasoning paths.
- `agents`: compare agent-level dependence.
- `models`: compare model/prior dependence.
- `methods`: compare methodological dependence.
