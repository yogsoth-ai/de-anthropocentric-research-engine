---
name: estimate-effective-evidence-count
description: "Estimate an effective number of independent evidence/reasoning paths after discounting dependence/correlation; report nominal N, dependence structure, and N_eff."
---

# estimate-effective-evidence-count
## Purpose
Estimate independent evidence count after discounting dependence and correlation.
## Input contract
```yaml
required: [evidence_paths, dependence_structure]
optional: [correlation_estimates, nominal_count]
constraints: [dependence assumptions and uncertainty must be explicit]
```
## Procedure
1. Count nominal paths and trace shared dependencies.
2. Assign dependence classes or correlations.
3. Estimate N_eff and sensitivity to dependence assumptions.
## Output contract
```yaml
produces: [nominal_count, dependence_map, effective_count, sensitivity_range]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Report N and N_eff separately; include a range when dependence is uncertain.
## Failure and counterexamples
Do not inflate N_eff by counting repeated sources or shared models as independent.
## Provenance map
- resolved: independent-convergence-audit
