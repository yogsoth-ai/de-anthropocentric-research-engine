---
name: claim-decomposition
description: Tactic for decomposing compound claims into atomic propositions — identify
  logical structure, separate conjunctions, extract implicit assumptions.
execution: tactic
dependencies:
  sops:
  - claim-page-creation
  - rebuttal-documentation
---

# Claim Decomposition

Decompose compound claims into atomic propositions that can be independently evaluated.

## Minimum Yield

<HARD-GATE>
Must produce ≥2 atomic claims per compound claim processed.
</HARD-GATE>

## Protocol

1. Identify the logical structure of the compound claim (conjunction, disjunction, conditional, etc.)
2. Separate each independent proposition into its own atomic claim
3. Extract implicit assumptions that the claim relies on but doesn't state
4. For each atomic claim, verify it is:
   - Falsifiable (could in principle be shown wrong)
   - Self-contained (understandable without the parent claim)
   - Non-redundant (not restating another extracted claim)
5. Create claim pages for each atomic proposition via `claim-page-creation`
6. Add `derived_from` edges from atomic claims back to the source compound claim

## SOPs Used

- **claim-page-creation** — create individual claim pages
- **rebuttal-documentation** — document counter-claims discovered during decomposition

## Yield Report

Returns: `{ compound_claims_processed: number, atomic_claims_produced: number, implicit_assumptions_found: number }`

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| claim-page-creation | SOP for creating a claim page in the vault — atomic proposition with type classification, source attribution, and initial confidence. |
| rebuttal-documentation | SOP for documenting rebuttals and counter-claims — create rebuttal pages with typed contradiction edges and source attribution. |

<!-- END available-tables (generated) -->
