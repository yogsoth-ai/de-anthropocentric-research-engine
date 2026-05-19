---
name: citation-chaining
description: Forward and backward citation tracing tactic — expand paper coverage by tracing citation networks in both directions from seed/key papers. Alternates forward (who cited this) and backward (what this cited) passes until saturation.
execution: tactic
used-by: literature-survey, patent-mining, baseline-establishment
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
