---
name: claim-analysis
description: Deep claim scope analysis — decompose independent/dependent claims and assess protection scope breadth. Budget: 30 patent families, 30 claim parses, 20 web searches.
execution: strategy
used-by: patent-mining
---

# Claim Analysis

Deep analysis of patent claim scope. Decomposes claim structure, maps element relationships, and assesses the breadth and strength of patent protection.

## Purpose

Provide detailed claim-level analysis for a set of target patents. Determines protection scope, identifies claim vulnerabilities, and maps the relationship between independent and dependent claims.

## Budget

| Metric | Target |
|--------|--------|
| Patent families analyzed | 30 |
| Claim parses | 30 |
| Web searches completed | 20 |

## State Ledger

| Metric | Target | Current | % |
|--------|--------|---------|---|
| Patent families analyzed | 30 | 0 | 0% |
| Claim parses completed | 30 | 0 | 0% |
| Web searches completed | 20 | 0 | 0% |
| Independent claims parsed | — | 0 | — |
| Claim elements extracted | — | 0 | — |

**HARD-GATE**: Cannot exit iteration loop until 80% of claim parses (24) and patent families (24) budget met.

## Available Tactics

| Tactic | When to Use |
|--------|-------------|
| claim-decomposition | Primary tactic — parse all claims and extract elements |
| patent-family-tracing | Find family members with different claim scope |
| classification-navigation | Understand technical context of claim elements |

## Available SOPs

| SOP | Role in This Strategy |
|-----|----------------------|
| claim-parsing | Core SOP — parse claim syntax and extract elements |
| patent-query-formulation | Find related patents for scope comparison |
| citation-network-analysis | Identify patents that cite or are cited by target |
| legal-status-assessment | Confirm target patents are active |
| quality-scoring | Assess claim quality (breadth, specificity, support) |
| patent-synthesis | Produce claim analysis report |

## Execution Guidance

1. **Target identification** — Identify patents for deep claim analysis
2. **Legal status check** — Confirm targets are active with `legal-status-assessment`
3. **Claim retrieval** — Fetch full claim text via web searches
4. **Claim parsing** — Use `claim-decomposition` tactic for full structural analysis
5. **Element extraction** — Extract all claim elements and map relationships
6. **Scope assessment** — Determine breadth of independent claims
7. **Vulnerability analysis** — Identify potential design-arounds and invalidity arguments
8. **Family comparison** — Check claim scope variations across jurisdictions
9. **Synthesis** — Produce detailed claim analysis report

## Output Format

```markdown
# Claim Analysis Report: [Patent Number(s)]

## Patent Overview
[Title, assignee, filing date, status]

## Claim Structure
### Independent Claims
| Claim # | Type | Element Count | Scope Assessment |
|---------|------|---------------|------------------|

### Claim Tree
[Dependency hierarchy visualization]

## Element-by-Element Analysis
### Claim 1
| Element | Technical Feature | Breadth | Potential Design-Around |
|---------|-------------------|---------|------------------------|

## Scope Assessment
- Broadest claim: [claim #, scope description]
- Narrowest claim: [claim #, scope description]
- Key limitations: [elements that narrow scope]

## Vulnerability Analysis
- Prior art risks: [elements with known prior art]
- Enablement concerns: [overly broad elements]
- Design-around paths: [alternative implementations]

## Cross-Jurisdiction Comparison
[Claim scope differences across patent family members]
```
