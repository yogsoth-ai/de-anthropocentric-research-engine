---
name: robustness-testing
description: Test conclusion robustness via multi-model convergence — enumerate assumptions,
  generate alternatives, compare results, flag fragile conclusions.
dependencies:
  tactics:
  - multi-model-convergence
  sops:
  - alternative-model-generation
  - convergence-assessment
  - deep-insight-assumption-enumeration
  - fragility-flagging
---

# Robustness Testing

Test whether conclusions survive across different modeling choices.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 20 | 18–22 |
| web-research | 10 | 9–11 |
| paper-overview | 30 | 27–33 |
| paper-search | 25 | 22–28 |
| paper-research | 15 | 13–17 |

## State Ledger

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 20 | ? |
| web-research | ? | 10 | ? |
| paper-overview | ? | 30 | ? |
| paper-search | ? | 25 | ? |
| paper-research | ? | 15 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available Tactics

- multi-model-convergence

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** assumption-enumeration, alternative-model-generation, convergence-assessment, fragility-flagging

## Execution Guidance

Enumerate modeling assumptions, generate alternative models by relaxing each, compare results across alternatives, flag results that depend on specific assumptions (fragile).

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| multi-model-convergence | Wimsatt-style multi-method cross-validation — enumerate assumptions, generate alternative models, compare results, flag divergences. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| alternative-model-generation | Generate alternative model formulations by relaxing, replacing, or generalizing specific assumptions. |
| convergence-assessment | Compare results across multiple model variants — quantitative agreement metrics and qualitative conclusion stability. |
| deep-insight-assumption-enumeration | Systematically identify all assumptions in a method/model — structural, parametric, distributional, and scope assumptions. |
| fragility-flagging | Identify which specific assumption changes cause conclusion divergence. Rates fragility severity and plausibility of alternatives. |

<!-- END available-tables (generated) -->
