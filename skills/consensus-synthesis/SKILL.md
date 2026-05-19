---
name: consensus-synthesis
description: Synthesize all rounds into a final consensus report documenting agreements, dissent, and process.
execution: subagent
prompt: ./prompt.md
input: rounds_history, final_judgments
used-by: structured-consensus
---

# Consensus Synthesis

Produce the final consensus report that synthesizes all rounds of iteration into a coherent document. Reports what was agreed, what remains contested, how the process evolved, and the strength of conclusions.

## Execution

Spawn a subagent that takes the full rounds history and final judgments, then produces a comprehensive consensus report.

## Why Subagent

- Synthesis requires integrating information across all rounds
- Report generation is a bounded writing task
- Final deliverable must be well-structured and complete

## HARD-GATE

Output MUST contain: `consensus_report` with sections for `agreements`, `dissent_record`, `process_summary`, and `confidence_assessment`. All items from the process must be accounted for.
