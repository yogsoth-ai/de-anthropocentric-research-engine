---
name: audit-convergence-independence
description: "Audit claims of independent convergence by tracing shared priors, data, framing, models, prompts, assumptions, or upstream evidence; estimate an effective independent evidence count rather than treating nominal N paths as independent."
---

# audit-convergence-independence
## Purpose
Estimate how much nominally independent convergence remains after shared priors, data, models, prompts, framings, assumptions, and upstream evidence are discounted.
## Input contract
```yaml
required: [evidence_paths, claims, provenance_records]
optional: [dependency_schema, correlation_estimates]
constraints: [each path must be traceable to its inputs and assumptions]
```
## Execution protocol
1. Enumerate paths and provenance (`identify-shared-priors`).
2. Verify independence and mark shared dependencies (`verify-evidence-independence`).
3. Estimate effective evidence count and perturb dependence assumptions (`estimate-effective-evidence-count`, `assess-sensitivity`).
Deviation: use qualitative dependence classes when numeric correlation is unavailable; never count nominal paths as independent by default.
## Output contract
```yaml
produces: [dependency_map, independence_audit, effective_evidence_count, sensitivity_report]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
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
