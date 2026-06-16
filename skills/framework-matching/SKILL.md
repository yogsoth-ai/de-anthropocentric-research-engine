---
name: framework-matching
description: 'SOP: Match the most suitable RQ framework based on research type'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: research-question
input: Research type + domain + hypothesis characteristics
output: Recommended framework + rationale + candidate framework comparison
dependencies:
  skills:
  - subagent-spawning
---

# Framework Matching

Match the most suitable RQ framework based on research type.

## HARD-GATE

<HARD-GATE>
Input must contain: research direction/hypothesis + research type (or enough information to infer the research type).
</HARD-GATE>

## Pipeline

1. **Precondition check**: Is the research direction and type clear
2. **Type determination**: Determine the research type (quantitative intervention / qualitative exploration / evaluation / mixed)
3. **Framework matching**: Match candidate frameworks based on type
4. **Applicability assessment**: Assess the applicability of each candidate framework
5. **Recommendation**: Select the most suitable framework + rationale
6. **Output**: Recommended framework + candidate comparison table

## Framework Knowledge Base

| Framework | Applicable research type | Core components | Strengths | Limitations |
|------|------------|---------|------|------|
| PICO/PICOTS | Quantitative/intervention | P-I-C-O(-T-S) | Clear structure, widely recognized | Not suitable for qualitative research |
| SPIDER | Qualitative | S-PI-D-E-R | Designed specifically for qualitative | Not suitable for intervention research |
| SPICE | Evaluation | S-P-I-C-E | Evaluation-oriented | Narrower scope |
| ECLIPSE | Mixed methods | E-C-L-I-P-S-E | Comprehensive, suitable for complex research | Many components, may be excessive |

## Output Format

```
{
  recommended: "PICO",
  rationale: "...",
  candidates: [
    { framework: "PICO", fit_score: 9, reason: "..." },
    { framework: "SPIDER", fit_score: 4, reason: "..." }
  ]
}
```
