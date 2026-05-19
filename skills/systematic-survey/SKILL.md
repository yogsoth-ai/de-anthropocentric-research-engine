---
name: systematic-survey
description: Exhaustive PRISMA-style literature survey — comprehensive coverage of all related work on a specific question. Multi-stage screening, citation chaining, quality assessment, and structured data extraction. Use when the user needs to demonstrate complete literature coverage or conduct rigorous gap analysis.
used-by: literature-survey
---

# Systematic Survey

**Purpose**: Deep and exhaustive — exhaustive coverage of all related work on a specific question. PRISMA-style rigor.

**When to use**: User needs to demonstrate comprehensive literature coverage (e.g., for a survey paper's related work section, or gap analysis requiring complete picture).

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 50 results | 45–55 |
| web-research | 5 pages | 4–6 |
| paper-overview | 60 papers | 54–66 |
| paper-search | 40 papers | 36–44 |
| paper-research | 30 papers | 27–33 |

## State Ledger

Print this table before each major iteration decision:

```
| SOP            | Target | Current | % Complete |
|----------------|--------|---------|------------|
| web-search     | 50     | ???     | ???%       |
| web-research   | 5      | ???     | ???%       |
| paper-overview | 60     | ???     | ???%       |
| paper-search   | 40     | ???     | ???%       |
| paper-research | 30     | ???     | ???%       |
```

Do not exit the strategy until all rows reach ≥90%.

## Available Tactics

- `prisma-screening` — multi-stage filtering (identification → screening → eligibility → inclusion)
- `citation-chaining` — forward/backward citation expansion until saturation

## Available SOPs

**Import** (strict protocol execution):
- `web-search` → web-browsing/skills/web-search/SKILL.md
- `web-research` → web-browsing/skills/web-research/SKILL.md
- `paper-overview` → literature-engine/skills/literature-overview/SKILL.md
- `paper-search` → literature-engine/skills/literature-search/SKILL.md
- `paper-research` → literature-engine/skills/literature-research/SKILL.md

**Subagent** (CC decides when to invoke):
- `define-search-protocol` — formalize queries + inclusion/exclusion criteria
- `extract-data` — structured comparison tables from deep-read papers
- `quality-assessment` — methodological rigor scoring
- `prisma-flowchart` — PRISMA-compliant flow documentation
- `saturation-detection` — determine when to stop expanding
- `gap-identification` — find what the literature hasn't addressed
- `survey-synthesis` — produce final structured output

## Execution Guidance

- Start with define-search-protocol (formalize queries + inclusion/exclusion criteria)
- Use prisma-screening tactic for multi-stage filtering
- citation-chaining to catch papers missed by keyword search
- saturation-detection to know when to stop expanding
- extract-data for structured comparison tables
- quality-assessment for methodological rigor scoring
- This is the most resource-intensive strategy — budget reflects depth

## Output Format

**Comprehensive Systematic Review** containing:
- PRISMA flow diagram (identification → screening → eligibility → inclusion counts)
- Structured comparison tables (method × dataset × metric)
- Quality assessment scores per paper
- Identified gaps with evidence
- Synthesis narrative connecting findings
