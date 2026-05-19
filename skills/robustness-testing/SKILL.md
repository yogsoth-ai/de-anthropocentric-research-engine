---
name: robustness-testing
description: Test conclusion robustness via multi-model convergence — enumerate assumptions, generate alternatives, compare results, flag fragile conclusions.
used-by: boundary-analysis
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
