---
name: citation-chaining
description: Forward and backward citation tracing tactic — expand paper coverage
  by tracing citation networks in both directions from seed/key papers. Alternates
  forward (who cited this) and backward (what this cited) passes until saturation.
execution: tactic
dependencies:
  sops:
  - knowledge-acquisition-paper-overview
  - knowledge-acquisition-paper-research
  - knowledge-acquisition-paper-search
  - knowledge-acquisition-saturation-detection
---

# Citation Chaining

Expand paper coverage by tracing citation networks in both directions.

## Operations

- **Backward chaining**: ss_references — what does this paper cite?
- **Forward chaining**: ss_citations — what cites this paper?

## Available SOPs

- `paper-overview` (import) — quick scan of discovered papers
- `paper-search` (import) — AI summary of promising papers
- `paper-research` (import) — deep reading of key papers
- `saturation-detection` (subagent) — determine when to stop

## Execution Guidance

- Start from seed/key papers
- Alternate forward and backward passes
- After each pass: filter by relevance, add to reading queue
- Use saturation-detection to stop when new papers aren't adding information
- Track the chain: paper A → cites B → cites C (provenance)
- Deduplicate across passes — same paper may appear in multiple chains

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| knowledge-acquisition-paper-overview | Abstract-level paper scanning for broad coverage. Import of literature-engine/literature-overview skill. Abstract-level only — no methodology conclusions from abstracts. |
| knowledge-acquisition-paper-research | Full-depth paper reading with raw text extraction. Import of literature-engine/literature-research skill. Must read fullText (true) — equations, hyperparameters, specific claims extracted. |
| knowledge-acquisition-paper-search | AI-summarized paper reading for intermediate depth. Import of literature-engine/literature-search skill. Must call get_paper_content for every analyzed paper. |
| knowledge-acquisition-saturation-detection | Determine when additional searching yields diminishing returns. Analyzes the latest expansion batch against existing corpus to judge continue/near-saturation/saturated. Used by snowball and systematic-survey. |

<!-- END available-tables (generated) -->
