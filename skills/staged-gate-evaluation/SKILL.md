---
name: staged-gate-evaluation
description: Define gate criteria for each stage, evaluate candidates at each gate, and render go/kill/recycle decisions with evidence.
execution: tactic
used-by: feasibility-assessment
---

# Staged Gate Evaluation

Apply Stage-Gate methodology to evaluate a candidate at defined decision points. Each gate has explicit criteria, and the candidate receives a GO (proceed), KILL (terminate), or RECYCLE (rework and re-evaluate) verdict based on evidence.

## Stages

1. **Gate Criteria Definition** — Define what must be true for a candidate to pass each gate. Deploy `gate-criteria-definition` SOP for each stage gate.

2. **Gate Judgment** — Evaluate the candidate against gate criteria and render a verdict. Deploy `gate-judgment` SOP at each gate.

3. **Feasibility Synthesis** — Combine all gate verdicts and assessments into a final feasibility determination. Deploy `feasibility-synthesis` SOP.

## Available SOPs

| SOP | Stage | Purpose |
|-----|-------|---------|
| gate-criteria-definition | 1 | Define criteria and pass thresholds |
| gate-judgment | 2 | Evaluate and render verdict |
| feasibility-synthesis | 3 | Synthesize into final recommendation |

## Execution Guidance

- Stage 1 should define >= 3 gates (e.g., concept feasibility, technical feasibility, implementation readiness)
- Gate criteria should be specific, measurable, and evidence-based
- Stage 2 evaluates sequentially — a KILL verdict at any gate terminates the evaluation
- A RECYCLE verdict means the candidate returns to a prior stage with specific rework requirements
- Stage 3 runs only after all gates have been evaluated (or a KILL is issued)
- Document the evidence basis for every verdict

## Minimum Yield

- Gate verdicts (GO/KILL/RECYCLE) for each defined gate
- Evidence supporting each verdict
- Conditions for advancement (what would change a KILL to GO)
- Final feasibility synthesis with recommendation
