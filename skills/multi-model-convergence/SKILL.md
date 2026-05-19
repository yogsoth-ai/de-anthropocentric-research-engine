---
name: multi-model-convergence
description: Wimsatt-style multi-method cross-validation — enumerate assumptions, generate alternative models, compare results, flag divergences.
execution: tactic
used-by: robustness-testing
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
