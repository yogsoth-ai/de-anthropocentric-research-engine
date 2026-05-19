---
name: snowball
description: Citation-chain-driven literature survey starting from seed papers. Traces research lineage in both forward (who cited this) and backward (what this cited) directions until saturation. High deep-read ratio (67%). Use when the user already has key papers and wants to find everything connected to them — ancestors, descendants, and branch points.
used-by: literature-survey
---

# Snowball

**Purpose**: Seed-first, forward/backward tracing — start from known seed papers and trace the research lineage in both directions.

**When to use**: User already has key papers and wants to find everything connected to them — what they built on, what built on them.

## Budget

| Base SOP | Target | ±10% Range |
|----------|--------|------------|
| web-search | 20 results | 18–22 |
| web-research | 3 pages | 2–4 |
| paper-overview | 30 papers | 27–33 |
| paper-search | 30 papers | 27–33 |
| paper-research | 20 papers | 18–22 |

## State Ledger

Print this table before each major iteration decision:

```
| SOP            | Target | Current | % Complete |
|----------------|--------|---------|------------|
| web-search     | 20     | ???     | ???%       |
| web-research   | 3      | ???     | ???%       |
| paper-overview | 30     | ???     | ???%       |
| paper-search   | 30     | ???     | ???%       |
| paper-research | 20     | ???     | ???%       |
```

Do not exit the strategy until all rows reach ≥90%.

## Available Tactics

- `citation-chaining` — forward/backward citation expansion until saturation

## Available SOPs

**Import** (strict protocol execution):
- `web-search` → web-browsing/skills/web-search/SKILL.md
- `web-research` → web-browsing/skills/web-research/SKILL.md
- `paper-overview` → literature-engine/skills/literature-overview/SKILL.md
- `paper-search` → literature-engine/skills/literature-search/SKILL.md
- `paper-research` → literature-engine/skills/literature-research/SKILL.md

**Subagent** (CC decides when to invoke):
- `seed-selection` — validate and prioritize starting papers
- `saturation-detection` — determine when to stop (diminishing returns)
- `gap-identification` — find what the literature hasn't addressed
- `survey-synthesis` — produce final structured output

## Execution Guidance

- seed-selection validates and prioritizes the starting papers
- citation-chaining is the primary operation — iterate until saturation
- saturation-detection determines when to stop (diminishing returns)
- Minimal web-search (only for context that papers don't provide)
- High paper-research ratio (20/30 = 67% deep-read rate) — trace papers deserve thorough reading
- Build a clear lineage: who influenced whom, how ideas evolved

## Output Format

**Research Lineage Map** containing:
- Seed papers → ancestors (backward trace)
- Seed papers → descendants (forward trace)
- Evolution of ideas across generations
- Key branch points where the field diverged
- Current frontier (most recent descendants)
- Lineage visualization (text-based DAG)
