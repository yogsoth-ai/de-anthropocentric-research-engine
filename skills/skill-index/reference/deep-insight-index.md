# Deep Insight — Skill Hierarchy

## Hierarchy

```mermaid
graph TD
    C1[insight]
    C2[gap-analysis]
    C3[boundary-analysis]
    C4[sensitivity-analysis]
    C5[problem-reformulation]

    S1[root-cause-drilling]
    S2[stakeholder-mapping]
    S3[tension-mining]
    S4[question-reformulation]
    S5[assumption-audit]
    C1 --> S1 & S2 & S3 & S4 & S5

    S6[gap-identification]
    S7[gap-classification]
    S8[gap-validation]
    S9[gap-prioritization]
    S10[gap-synthesis-strategy]
    C2 --> S6 & S7 & S8 & S9 & S10

    S11[validity-envelope-mapping]
    S12[robustness-testing]
    S13[boundary-critique]
    S14[failure-mode-analysis]
    S15[scaling-frontier]
    C3 --> S11 & S12 & S13 & S14 & S15

    S16[parameter-screening]
    S17[variance-decomposition]
    S18[assumption-criticality]
    S19[uncertainty-propagation]
    S20[decision-sensitivity]
    C4 --> S16 & S17 & S18 & S19 & S20

    S21[dominant-idea-escape]
    S22[multi-perspective-reframing]
    S23[dialectical-reformulation]
    S24[wickedness-assessment]
    S25[appreciative-reframing]
    C5 --> S21 & S22 & S23 & S24 & S25

    T1[causal-tree-building]
    T2[dialectical-synthesis]
    T3[boundary-unfolding]
    T4[assumption-stress-test]
    C1 --> T1 & T2 & T3 & T4

    T5[evidence-mapping]
    T6[cross-validation]
    T7[prioritization-scoring]
    C2 --> T5 & T6 & T7

    T8[multi-model-convergence]
    T9[systematic-perturbation]
    T10[failure-mode-cataloging]
    C3 --> T8 & T9 & T10

    T11[screening-then-decomposition]
    T12[assumption-perturbation]
    T13[uncertainty-cascade]
    C4 --> T11 & T12 & T13

    T14[lateral-escape]
    T15[multi-worldview-comparison]
    T16[dialectical-escalation]
    C5 --> T14 & T15 & T16
```

## Complete Skill Table

| Level | Skill | Description |
|-------|-------|-------------|
| campaign | insight | Deep root-cause analysis of why gaps persist |
| campaign | gap-analysis | Identify, classify, validate, prioritize gaps |
| campaign | boundary-analysis | Probe where methods fail, map validity |
| campaign | sensitivity-analysis | Identify most critical assumptions by impact |
| campaign | problem-reformulation | Question the problem itself |
| strategy | root-cause-drilling | Drill from symptoms to root causes |
| strategy | stakeholder-mapping | Map affected parties, identify exclusions |
| strategy | tension-mining | Identify opposing forces keeping gaps open |
| strategy | question-reformulation | Reframe questions via laddering/HMW/Socratic |
| strategy | assumption-audit | Surface, classify, validate assumptions |
| strategy | gap-identification | Find what literature has NOT addressed |
| strategy | gap-classification | Classify gaps via Miles/AHRQ frameworks |
| strategy | gap-validation | Validate gap authenticity cross-database |
| strategy | gap-prioritization | Score/rank gaps on importance/feasibility |
| strategy | gap-synthesis-strategy | Compile gap analysis into final report |
| strategy | validity-envelope-mapping | Map multi-dimensional validity envelopes |
| strategy | robustness-testing | Test conclusion robustness multi-model |
| strategy | boundary-critique | CSH boundary critique, included/excluded |
| strategy | failure-mode-analysis | Catalog failure modes systematically |
| strategy | scaling-frontier | Analyze behavior across scales |
| strategy | parameter-screening | Morris method quick screening |
| strategy | variance-decomposition | Sobol indices for variance attribution |
| strategy | assumption-criticality | Measure conclusion change per negation |
| strategy | uncertainty-propagation | Monte Carlo propagation through model |
| strategy | decision-sensitivity | EVPI for research prioritization |
| strategy | dominant-idea-escape | Escape paradigm lock-in via lateral PO |
| strategy | multi-perspective-reframing | CATWOE from multiple viewpoints |
| strategy | dialectical-reformulation | Double-loop learning, governing variables |
| strategy | wickedness-assessment | Rittel criteria, tame/complex/wicked |
| strategy | appreciative-reframing | Positive deviants, asset-based reframing |
| tactic | causal-tree-building | Build logical causal trees to root causes |
| tactic | dialectical-synthesis | Thesis-antithesis-synthesis cycle |
| tactic | boundary-unfolding | Expose hidden system boundaries via CSH |
| tactic | assumption-stress-test | Surface, classify, attack assumptions |
| tactic | evidence-mapping | Systematic evidence map construction |
| tactic | cross-validation | Multi-source gap authenticity verification |
| tactic | prioritization-scoring | Multi-dimensional gap scoring/ranking |
| tactic | multi-model-convergence | Wimsatt-style cross-validation |
| tactic | systematic-perturbation | Multi-axis validity probing |
| tactic | failure-mode-cataloging | Systematic failure taxonomy |
| tactic | screening-then-decomposition | Morris screen then Sobol decomposition |
| tactic | assumption-perturbation | One-at-a-time negation and re-derivation |
| tactic | uncertainty-cascade | Monte Carlo propagation, critical paths |
| tactic | lateral-escape | Identify dominant idea, provoke, escape |
| tactic | multi-worldview-comparison | CATWOE multi-perspective + reframing |
| tactic | dialectical-escalation | Double-loop learning escalation |
| sop | five-whys-drilling | Iterative Why? to actionable root cause |
| sop | ishikawa-decomposition | 6M fishbone diagram decomposition |
| sop | current-reality-tree | TOC sufficient-cause logic to root causes |
| sop | csh-12-question | Ulrich's 12 questions, is vs ought |
| sop | jtbd-mapping | Stakeholder Jobs-to-be-Done mapping |
| sop | salience-classification | Mitchell Power/Legitimacy/Urgency |
| sop | evaporating-cloud | Goldratt conflict dissolution |
| sop | polarity-mapping | Johnson polarities, 4 quadrants |
| sop | abstraction-laddering | Move between concrete/abstract framings |
| sop | hmw-formulation | How Might We at different scope levels |
| sop | socratic-probing | 6 types of Socratic questions |
| sop | abp-vulnerability-classification | Load-bearing x vulnerable 2-axis classify |
| sop | clr-validation | Goldratt 8 Categories of Legitimate Reservation |
| sop | evidence-synthesis | Multi-source evidence into argumentation |
| sop | assumption-surfacing | Extract implicit assumptions |
| sop | gap-keyword-extraction | Extract gap-indicating sentences |
| sop | concept-matrix-construction | Articles x concepts coverage matrix |
| sop | egm-construction | Build structured Evidence Gap Maps |
| sop | gap-typology-classification | Miles 7-type taxonomy classification |
| sop | ahrq-reason-classification | AHRQ 4-reason framework classification |
| sop | cross-database-verification | Verify gap across multiple databases |
| sop | false-gap-filtering | Detect false gaps masquerading as real |
| sop | temporal-sensitivity-testing | Test gap persistence across time windows |
| sop | multi-criteria-scoring | Weighted multi-criteria decision analysis |
| sop | stakeholder-confirmation | Simulate stakeholder gap validation |
| sop | evidence-grading | GRADE/SOE framework quality assessment |
| sop | gap-synthesis | Final gap report with research agenda |
| sop | assumption-enumeration | Identify all assumptions systematically |
| sop | alternative-model-generation | Generate alternative model formulations |
| sop | convergence-assessment | Compare results across model variants |
| sop | fragility-flagging | Identify assumption changes causing divergence |
| sop | variation-axis-definition | Identify orthogonal validity axes |
| sop | controlled-perturbation | Vary parameters, record degradation |
| sop | validity-envelope-construction | Combine perturbation into validity surface |
| sop | edge-case-generation | Generate boundary/adversarial inputs |
| sop | failure-clustering | Group failures by mechanism |
| sop | scaling-regime-detection | Detect regime changes in scaling |
| sop | boundary-synthesis | Compile boundary analysis report |
| sop | morris-screening | Elementary effects for parameter importance |
| sop | sobol-decomposition | First/total-order sensitivity indices |
| sop | interaction-detection | Detect significant parameter interactions |
| sop | assumption-extraction | Extract all assumptions from method |
| sop | negation-definition | Define strongest plausible alternatives |
| sop | re-derivation | Re-derive conclusions under negation |
| sop | conclusion-sensitivity-measurement | Quantify conclusion change across negations |
| sop | distribution-assignment | Assign probability distributions |
| sop | monte-carlo-sampling | Design/execute Monte Carlo sampling |
| sop | critical-path-identification | Identify highest-contributing uncertainties |
| sop | sensitivity-synthesis | Synthesize sensitivity results into report |
| sop | dominant-idea-identification | Identify paradigms constraining thinking |
| sop | provocation-generation | de Bono PO provocations |
| sop | consequence-following | Follow provocation consequences |
| sop | catwoe-analysis | Checkland CATWOE from stakeholder view |
| sop | reframing-matrix | 4 professional perspectives reframing |
| sop | governing-variable-surfacing | Argyris governing variables |
| sop | counter-assumption-generation | Dialectical opposites for variables |
| sop | wickedness-scoring | Score against Rittel's 10 criteria |
| sop | appreciative-discovery | Positive deviants, transferable principles |
| sop | reformulation-synthesis | Compile reformulation into report |
| sop | multi-stakeholder-simulation | Simulate multiple stakeholder perspectives |
| sop (import) | web-search | Quick web scanning for landscape |
| sop (import) | web-research | Full-page web reading |
| sop (import) | paper-overview | Abstract-level paper scanning |
| sop (import) | paper-search | AI-summarized paper reading |
| sop (import) | paper-research | Full-depth paper reading |
