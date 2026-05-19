---
name: meta-analysis-synthesis
description: Produce final meta-analysis protocol document assembling all planning outputs into PRISMA-compliant protocol
execution: subagent
prompt: ./prompt.md
input: all_planning_outputs
used-by: meta-analysis
---

# Meta-Analysis Synthesis SOP

Assemble all planning outputs into a complete, PRISMA-compliant meta-analysis protocol document ready for registration (PROSPERO) and execution.

## When to Use

- Final step in any meta-analysis strategy
- After all component planning is complete (PICO, criteria, extraction, quality, synthesis plan)
- When producing the deliverable protocol document

## Input

- `all_planning_outputs`: Combined outputs from all preceding SOPs (PICO, inclusion criteria, effect size plan, extraction form, RoB plan, heterogeneity plan, bias plan, sensitivity plan, and optionally network construction)

## Output

Complete meta-analysis protocol document in PRISMA-P format, suitable for PROSPERO registration.
