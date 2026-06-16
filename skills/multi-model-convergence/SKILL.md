---
name: multi-model-convergence
description: Wimsatt-style multi-method cross-validation — enumerate assumptions,
  generate alternative models, compare results, flag divergences.
execution: tactic
dependencies:
  sops:
  - alternative-model-generation
  - convergence-assessment
  - deep-insight-assumption-enumeration
  - deep-insight-paper-research
  - fragility-flagging
---

# Multi-Model Convergence

Test robustness by checking if conclusions survive across different modeling choices.

## Operations

- assumption-enumeration → alternative-model-generation → convergence-assessment → fragility-flagging

## Available SOPs

**Subagent:** assumption-enumeration, alternative-model-generation, convergence-assessment, fragility-flagging
**Import:** paper-research

## Execution Guidance

For each key assumption, generate at least one alternative model. Run all models, compare outputs. Results that converge are robust; results that diverge are fragile.

## Minimum Yield

```
<HARD-GATE>
- assumptions enumerated: >= 5
- alternative models generated: >= 3
- convergence assessments: >= 1
- fragility flags: assessed
</HARD-GATE>
```

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| alternative-model-generation | Generate alternative model formulations by relaxing, replacing, or generalizing specific assumptions. |
| convergence-assessment | Compare results across multiple model variants — quantitative agreement metrics and qualitative conclusion stability. |
| deep-insight-assumption-enumeration | Systematically identify all assumptions in a method/model — structural, parametric, distributional, and scope assumptions. |
| deep-insight-paper-research | Full-text paper reading via three-pass Keshav method. Import of literature-engine/literature-research skill. Authoritative source for claims about paper content. |
| fragility-flagging | Identify which specific assumption changes cause conclusion divergence. Rates fragility severity and plausibility of alternatives. |

<!-- END available-tables (generated) -->
