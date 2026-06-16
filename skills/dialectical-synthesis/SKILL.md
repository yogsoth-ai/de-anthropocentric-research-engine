---
name: dialectical-synthesis
description: Hegelian thesis-antithesis-synthesis cycle — propose position, generate
  opposition, structured debate, synthesize transcending insight. Combines evaporating-cloud
  and polarity-mapping SOPs.
execution: tactic
dependencies:
  sops:
  - deep-insight-paper-search
  - deep-insight-web-research
  - evaporating-cloud
  - polarity-mapping
---

# Dialectical Synthesis

Thesis-antithesis-synthesis cycle for tension resolution.

## Operations

- evaporating-cloud — expose hidden assumptions behind opposing needs
- polarity-mapping — map unresolvable tensions as polarities to manage

## Available SOPs

**Subagent:** evaporating-cloud, polarity-mapping
**Import:** paper-search, web-research

## Execution Guidance

Model conflict as evaporating cloud (expose hidden assumptions behind opposing needs). If tension is a genuine polarity (not resolvable), map it with polarity management framework. Distinguish solvable conflicts from inherent polarities.

## Minimum Yield

```
<HARD-GATE>
- evaporating clouds: >= 1
- assumptions exposed: >= 3
- polarity maps (if applicable): >= 1
</HARD-GATE>
```

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| deep-insight-paper-search | AI-powered paper summary and search. Import of literature-engine/literature-search skill. AI summary level — cite as "AI-extracted" not "paper states". |
| deep-insight-web-research | Deep web research with full page fetching via Apify. Import of web-browsing/web-research skill. Must fetch full page — no conclusions from previews. |
| evaporating-cloud | Model conflicts as Goldratt's Evaporating Cloud — expose hidden assumptions behind opposing needs to dissolve the conflict. |
| polarity-mapping | Map unresolvable tensions as Johnson polarities — 4 quadrants (positive/negative of each pole), early warnings, action steps for managing rather than solving. |

<!-- END available-tables (generated) -->
