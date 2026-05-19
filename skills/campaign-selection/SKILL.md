---
name: campaign-selection
description: Structured questioning SOP to determine which campaigns to include, emphasize, or skip. Used during spec generation.
execution: sequential
used-by: writing-specs
---

# Campaign Selection

Ask the user 2-3 questions about which campaigns to include in the research pipeline.

## Context

Before asking, you have already read `research-catalog` and know all available campaigns. Present the default pipeline as a starting point.

## Questions (select 2-3 most relevant)

1. **Default Pipeline Review**
   - Present the 7-stage default pipeline:
     ```
     1. Knowledge Acquisition (lit-survey)
     2. Deep Insight (gap-analysis + insight)
     3. Hypothesis Formation
     4. Creative Ideation (2-3 campaigns)
     5. Convergence (scoring + steel-manning)
     6. Stress Test (red-teaming + failure-anticipation)
     7. Experiment Design
     ```
   - "Does this pipeline fit your needs, or would you adjust it?"
   - Options: (A) Looks good as-is (B) I want to skip some stages (C) I want to emphasize certain stages (D) I have a different structure in mind

2. **Emphasis Selection** (if user wants to emphasize)
   - "Which stages should get extra depth?"
   - Options: list the 7 stages, allow multi-select

3. **Ideation Campaign Preference** (if reaching ideation stage)
   - "For creative ideation, any preference on approach?"
   - Options: (A) Let CC choose based on topic (B) I want cross-domain/biomimicry focus (C) I want systematic methods (TRIZ/morphological) (D) I want divergent methods (SCAMPER/lateral)

## Rules

- Ask ONE question at a time
- Default pipeline is the starting assumption — user only needs to specify deviations
- Record selections for pipeline composition
