---
name: argument-synthesis
description: Strategy for synthesizing argument positions — aggregate evidence, resolve
  contradictions, produce synthesis reports identifying which claims survive scrutiny.
execution: strategy
dependencies:
  tactics:
  - knowledge-structuring-claim-decomposition
  - strength-assessment
  sops:
  - argument-visualization
  - synthesis-report
---

# Argument Synthesis

Synthesize coherent positions from the argument graph. Aggregates evidence across claims, resolves contradictions where possible, and produces synthesis reports that identify which claims survive scrutiny and which are undermined.

## Budget Slice

| Metric | Small | Medium | Large |
|--------|-------|--------|-------|
| Claims synthesized | 10 | 25 | 50 |
| Contradictions resolved | 2 | 6 | 12 |
| Synthesis reports | 1 | 3 | 5 |

## State Ledger

<HARD-GATE>
Print before every iteration:

| Metric | Target | Current | % |
|--------|--------|---------|---|
| Claims synthesized | — | — | — |
| Contradictions resolved | — | — | — |
| Synthesis reports | — | — | — |
</HARD-GATE>

## Budget Gate

Cannot exit until 80% of budget targets met.

## Adversarial Completeness Probe

After budget gate passes, self-check:
- Does the synthesis address all major contradictions?
- Are surviving claims genuinely supported or just uncontested?
- Does the report acknowledge remaining uncertainty?

Max 2 extra iterations if gaps found.

## Tactics Available

- **claim-decomposition** — decompose complex positions for analysis
- **strength-assessment** — final strength evaluation for synthesis

## SOPs Available

- **argument-visualization** — generate argument structure visualization
- **synthesis-report** — produce the final synthesis document

<!-- BEGIN available-tables (generated) -->

## Available Tactics

可选,无固定顺序;最终叶子终为 sop。

| Tactic | 何时用 |
| --- | --- |
| knowledge-structuring-claim-decomposition | Tactic for decomposing compound claims into atomic propositions — identify logical structure, separate conjunctions, extract implicit assumptions. |
| strength-assessment | Tactic for assessing argument strength — evaluate evidence quality, count independent sources, check for defeaters, assign calibrated confidence scores. |

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| argument-visualization | SOP for generating argument structure visualization — query graph for argument chains, format as mermaid diagram or indented tree, write to vault. |
| synthesis-report | SOP for producing argument synthesis reports — aggregate evidence, resolve contradictions, identify surviving claims, write structured summary. |

<!-- END available-tables (generated) -->
