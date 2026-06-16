---
name: decision-sensitivity
description: Identify which uncertainties would actually change the research direction
  decision. Compute EVPI to prioritize uncertainty reduction.
dependencies:
  sops:
  - critical-path-identification
  - sensitivity-synthesis
---

# Decision Sensitivity

Focus on uncertainties that change decisions, not just numbers.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 25 | 22–28 |
| web-research | 10 | 9–11 |
| paper-overview | 25 | 22–28 |
| paper-search | 15 | 13–17 |
| paper-research | 10 | 9–11 |

## State Ledger

```
<HARD-GATE>
| SOP | Done | Target | % |
|-----|------|--------|---|
| web-search | ? | 25 | ? |
| web-research | ? | 10 | ? |
| paper-overview | ? | 25 | ? |
| paper-search | ? | 15 | ? |
| paper-research | ? | 10 | ? |
Budget Gate: OPEN/CLOSED (>=80% required to exit)
</HARD-GATE>
```

## Available SOPs

**Import:** web-search, web-research, paper-overview, paper-search, paper-research
**Subagent:** critical-path-identification, sensitivity-synthesis

## Execution Guidance

Identify which uncertainties would actually change the research direction decision. Compute Expected Value of Perfect Information (EVPI) for each uncertain parameter. Focus resources on reducing uncertainty with highest EVPI.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| critical-path-identification | Identify which input uncertainties contribute most to output uncertainty and compute EVPI for research prioritization. |
| sensitivity-synthesis | Synthesize all sensitivity analysis results into a coherent report with prioritized recommendations. |

<!-- END available-tables (generated) -->
