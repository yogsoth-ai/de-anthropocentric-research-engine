---
name: writing-specs
description: Generate a complete, executable Research Spec from North Star + user
  input. Strategy-level skill that orchestrates questioning, outline, and spec writing.
execution: sequential
dependencies:
  sops:
  - campaign-selection
  - constraint-elicitation
  - research-catalog
  - scope-clarification
  - spec-self-review
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
   When the outline includes an experiment-execution stage, default to SUGGESTING
   `ara-from-context` as a closing stage (compile the results into an ARA); the user
   may decline. Without experiment-execution, still offer it if the user wants the
   research packaged. ara-from-context is the 10th optional package — never a forced tail.

### Step 3: Pipeline Outline

Synthesize the North Star, ResearchBrief, and user answers into a 5-10 line outline:

```
Stage 1: [campaign] ([strategies]) — [topic/focus]
Stage 2: [campaign] ([strategies]) — [topic/focus]
...
Stage N: experiment-execution (experiment-design) — [topic]
Stage N+1: ara-from-context — compile the research into an ARA (OPTIONAL closing stage; include only if the user wants the results packaged for agent reproduction; user may remove)
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

#### ARA Closing Stage (when present)

When the outline includes an `ara-from-context` stage, write its Execution Steps so the
stage opens with an explicit user-decision gate, NOT an automatic transition:

- First step: after experiment-execution's evaluation reports PASS, present to the user:
  "实验评估通过,是否进入 ARA 成文?(compile results into an ARA)" — proceed only on approval.
- Do NOT hard-code which EE evaluation skill produces that PASS; the executing agent reads
  the spec's experiment-execution stage and the research-catalog to choose it at run time.
- The gate is an ordinary natural-language Execution Step (spec = trace). Do not invent a
  new spec field, and do not reuse the Backtrack Condition mechanism (that is for retreat,
  this is a forward go/no-go decision).
- Remaining steps: invoke `ara-from-context` (context-review → compile-and-review), producing
  `ara/` + `ara/level2_report.json`. Note the external prerequisite: `npx @ara-commons/ara-skills`
  must be installed (compiler + rigor-reviewer).

### Step 5: Spec Self-Review

Invoke `spec-self-review` SOP. This is MANDATORY and cannot be skipped.

### Step 6: User Review

Present the completed spec to the user for review. Wait for approval or change requests. If changes requested, revise and re-run self-review.

## Output

Save the spec to: `docs/de-anthropocentric/specs/YYYY-MM-DD-<topic>-spec.md`

Inform the user: "Spec complete. To execute, invoke `executing-specs` with the path to this spec file."

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| campaign-selection | Structured questioning SOP to determine which campaigns to include, emphasize, or skip. Used during spec generation. |
| constraint-elicitation | Structured questioning SOP to identify practical constraints that shape the research spec. Used during spec generation. |
| research-catalog | Capability menu for the research engine. Lists the 10 freely-composable research packages, what each does, when to reach for it, and a pointer to its full skill table. Read this after north-star crystallization to decide which packages to use — no fixed order. Also serves as the skill-index (capability map). |
| scope-clarification | Structured questioning SOP to determine research boundaries, depth, and breadth. Used during spec generation. |
| spec-self-review | Quality gate for Research Specs. Checks for placeholders, consistency, scope, ambiguity, context protocol, and quantification. Mandatory before user review. |

<!-- END available-tables (generated) -->
