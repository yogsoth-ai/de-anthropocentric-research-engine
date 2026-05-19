---
name: quality-assessment-protocol
description: Methodological quality and bias risk assessment of included studies using validated tools
execution: tactic
used-by: meta-analysis
---

# Quality Assessment Protocol Tactic

Systematically assess methodological quality and risk of bias for each included study using domain-appropriate validated tools.

## Stages

### Stage 1: Tool Selection

Select the appropriate quality assessment tool based on study design.

| Study Design | Tool | Domains |
|--------------|------|---------|
| RCT | RoB 2.0 | Randomization, deviations, missing data, measurement, selection |
| Non-randomized interventions | ROBINS-I | Confounding, selection, classification, deviations, missing, measurement, reporting |
| Diagnostic accuracy | QUADAS-2 | Patient selection, index test, reference standard, flow/timing |
| Prediction models | PROBAST | Participants, predictors, outcome, analysis |
| Observational | Newcastle-Ottawa | Selection, comparability, outcome/exposure |

**Decision**: Match tool to study design. Use one tool consistently within a meta-analysis.

### Stage 2: Per-Study Assessment

Apply the selected tool to each included study.

- Assess each domain independently
- Use signaling questions to guide domain judgments
- Assign domain-level judgment (Low/Some Concerns/High risk)
- Document supporting rationale for each judgment
- Resolve disagreements with explicit criteria

**SOPs**: risk-of-bias-assessment

### Stage 3: Summary and Visualization Planning

Plan the summary presentation of quality assessments.

- Traffic light plot (per-study, per-domain)
- Summary bar chart (proportion at each risk level per domain)
- Overall risk-of-bias judgment per study
- Sensitivity analysis groupings (low-risk only vs all)
- GRADE certainty assessment contribution

**SOPs**: sensitivity-analysis-design

## Minimum Yield

Per execution of this tactic:
- At least 5 studies assessed
- All domains of the selected tool evaluated per study
- Supporting rationale documented for each judgment
- Summary visualization plan produced
- Sensitivity groupings defined

## Output Format

```yaml
quality_assessment:
  tool_used: [RoB2/ROBINS-I/QUADAS-2/PROBAST/NOS]
  assessments:
    - study_id: [identifier]
      domains:
        - domain: [name]
          judgment: [Low/Some Concerns/High]
          rationale: [supporting text]
      overall: [Low/Some Concerns/High]
  summary:
    low_risk_count: [N]
    some_concerns_count: [N]
    high_risk_count: [N]
    problematic_domains: [most common high-risk domains]
  sensitivity_groups:
    low_risk_only: [study list]
    excluding_high_risk: [study list]
```
