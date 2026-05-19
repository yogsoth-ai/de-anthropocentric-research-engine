---
name: writing-specs
description: Generate a complete, executable Research Spec from North Star + user input. Strategy-level skill that orchestrates questioning, outline, and spec writing.
execution: sequential
used-by: de-anthropocentric-research-engine
---

# Writing Specs

You are generating a Research Spec — a document that is simultaneously human-readable and machine-executable. Another CC session will later read this spec and execute it step by step.

## Prerequisites

Before invoking this skill, the following MUST exist:
- A confirmed North Star statement
- A structured ResearchBrief
- Both preserved in a context-checkpoint file

## Flow

### Step 1: Read Research Catalog

Read `skills/research-catalog/SKILL.md` in its entirety. Internalize:
- All available campaigns and their strategies
- The dependency relationships between campaigns
- Pre-conditions for each campaign

### Step 2: Structured Questioning

Invoke these 3 SOPs sequentially. Each asks 2-3 focused questions:

1. `scope-clarification` — research boundaries, depth vs breadth
2. `campaign-selection` — which campaigns to include/emphasize/skip
3. `constraint-elicitation` — time budget, existing knowledge, hard constraints

### Step 3: Pipeline Outline

Synthesize the North Star, ResearchBrief, and user answers into a 5-10 line outline:

```
Stage 1: [campaign] ([strategies]) — [topic/focus]
Stage 2: [campaign] ([strategies]) — [topic/focus]
...
Stage N: experiment-execution (experiment-design) — [topic]
```

Present this outline to the user. Wait for confirmation. User may adjust stages, reorder, add, or remove.

### Step 4: Write Full Spec

Expand the confirmed outline into a complete Research Spec. Follow this schema exactly:

#### Spec Header
```
# Research Spec: <Topic>

> Generated: YYYY-MM-DD
> North Star: <one sentence>
> Scope: <N> stages, estimated <M> sessions
> Source: de-anthropocentric-research-engine
```

#### Global Sections
- Global Context Protocol (context-init/checkpoint rules)
- Global Execution Rules (±10% deviation, backtrack confirmation)
- Global Backtrack Conditions

#### Per-Stage Structure
For EACH stage, write ALL of these fields:
- **Objective**: What this stage accomplishes
- **Expected Input**: What context is available from prior stages
- **Focus Areas**: Specific aspects to emphasize
- **Recommended Combination**: campaign → strategy-A, strategy-B
- **Completion Criteria**: Quantified threshold (numeric or objectively verifiable)
- **Backtrack Condition**: if [condition], → Stage N (requires user confirmation)
- **Execution Steps**: Checkbox items (context-init, each strategy, checkpoints)

#### Granularity Rules
- Name specific strategies (not tactics/SOPs — those are CC's choice at execution time)
- Describe what topic/aspect each strategy addresses
- Specify what prior context is available and how to use it
- Quantify ALL completion criteria (no vague "sufficient" or "adequate")
- Focus Areas tell CC what to prioritize within the campaign's scope

### Step 5: Spec Self-Review

Invoke `spec-self-review` SOP. This is MANDATORY and cannot be skipped.

### Step 6: User Review

Present the completed spec to the user for review. Wait for approval or change requests. If changes requested, revise and re-run self-review.

## Output

Save the spec to: `docs/de-anthropocentric/specs/YYYY-MM-DD-<topic>-spec.md`

Inform the user: "Spec complete. To execute, invoke `executing-specs` with the path to this spec file."
