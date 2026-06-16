---
name: claim-extraction
description: Strategy for extracting claims from source material — identify propositions,
  decompose compound claims, classify claim types, create claim pages in the vault.
execution: strategy
dependencies:
  tactics:
  - knowledge-structuring-claim-decomposition
  sops:
  - claim-page-creation
  - rebuttal-documentation
---

# Claim Extraction

Identify and extract claims from source material. Decomposes compound statements into atomic propositions, classifies claim types, and creates structured claim pages in the vault.

## Budget Slice

| Metric | Small | Medium | Large |
|--------|-------|--------|-------|
| Sources processed | 5 | 12 | 25 |
| Claims extracted | 10 | 25 | 50 |
| Compound claims decomposed | 3 | 8 | 15 |

## State Ledger

<HARD-GATE>
Print before every iteration:

| Metric | Target | Current | % |
|--------|--------|---------|---|
| Sources processed | — | — | — |
| Claims extracted | — | — | — |
| Compound claims decomposed | — | — | — |
</HARD-GATE>

## Budget Gate

Cannot exit until 80% of budget targets met.

## Adversarial Completeness Probe

After budget gate passes, self-check:
- Have all major positions in the debate been captured?
- Are there implicit claims that sources assume but don't state?
- Are there claims from minority/dissenting positions?

Max 2 extra iterations if gaps found.

## Tactics Available

- **claim-decomposition** — break compound claims into atomic propositions

## SOPs Available

- **claim-page-creation** — create a claim page in the vault
- **rebuttal-documentation** — document counter-claims and rebuttals

<!-- BEGIN available-tables (generated) -->

## Available Tactics

Optional, no fixed order; the final leaf is always a sop.

| Tactic | When to use |
| --- | --- |
| knowledge-structuring-claim-decomposition | Tactic for decomposing compound claims into atomic propositions — identify logical structure, separate conjunctions, extract implicit assumptions. |

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| claim-page-creation | SOP for creating a claim page in the vault — atomic proposition with type classification, source attribution, and initial confidence. |
| rebuttal-documentation | SOP for documenting rebuttals and counter-claims — create rebuttal pages with typed contradiction edges and source attribution. |

<!-- END available-tables (generated) -->
