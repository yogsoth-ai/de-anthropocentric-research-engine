# Rapid Triage — Subagent Dispatch Prompt

You are executing the rapid-triage strategy for gap prioritization.

## Your Task

Quickly reduce a large set of gaps (50+) to a manageable candidate set through two fast passes: a binary keep/drop filter, then a lightweight two-dimension scoring of survivors. Speed is the primary constraint — do not over-analyze individual gaps.

## Process

### Pass 1: Binary Filter (Keep / Drop)

For each gap, answer three yes/no questions. Any "No" → Drop immediately. Do not deliberate — if the answer is not clearly "Yes," treat it as "No."

**Q1 — Scope**: Is this gap within the stated research scope? (If no explicit scope is given, use the domain of the majority of gaps as the implicit scope.)

**Q2 — Solvability**: Is this gap technically solvable in principle? (Reject philosophical questions, definitional debates, or gaps that require solving AGI as a prerequisite.)

**Q3 — Novelty**: Is this gap NOT already being actively addressed by recent work (last 2 years)? (If you are uncertain, Keep — false negatives are worse than false positives at this stage.)

Record the drop reason for each dropped gap: "out-of-scope" / "not-solvable" / "already-addressed."

Time budget for Pass 1: approximately 20–30 seconds per gap. Do not exceed this.

### Pass 2: Lightweight Scoring (Survivors Only)

Score each surviving gap on two dimensions using a 1–3 scale only (no 4s or 5s — this is a coarse filter):

**Importance (1–3)**:
- 3: Solving this would be a significant advance recognized across the field
- 2: Solving this would be useful but incremental
- 1: Solving this would have limited field-level impact

**Feasibility (1–3)**:
- 3: Meaningful progress achievable within 6 months with available resources
- 2: Achievable within 1–2 years with moderate resource investment
- 1: Requires major new capabilities, data, or resources not currently available

Compute triage score = Importance × Feasibility (range: 1–9).

Rank survivors by triage score. Take top-K (K per budget tier: S=15, M=20, L=30).

### Pass 3: Output Preparation

Compile the candidate set and prepare a handoff summary for the next strategy (multi-criteria-ranking or portfolio-optimization).

## Output Format

### Pass 1 Summary

| Outcome | Count | Breakdown |
|---------|-------|-----------|
| Keep    | N     | — |
| Drop (out-of-scope) | N | [brief pattern description] |
| Drop (not-solvable) | N | [brief pattern description] |
| Drop (already-addressed) | N | [brief pattern description] |

### Pass 2 Scoring (Survivors)

| Gap ID | Importance | Feasibility | Triage Score | Rank |
|--------|-----------|-------------|-------------|------|
| G-01   | …         | …           | …           | …    |

### Candidate Set (Top-K)
List of gap IDs that advance to the next stage, in triage score order.

### Handoff Note
Recommended next strategy (multi-criteria-ranking for K ≤ 20, portfolio-optimization for K > 20), and any patterns observed in the dropped gaps that might inform the research scope.

## Rules

- Pass 1 is binary — no partial keeps, no "maybe" category. Every gap is either Keep or Drop.
- The 1–3 scale in Pass 2 is intentional. Do not use 4 or 5 — this is a coarse filter, not a precise ranking.
- Do not write detailed justifications for individual gap scores in Pass 2. One-line notes only.
- If more than 80% of gaps are dropped in Pass 1, flag this as a potential scope mismatch and ask whether the scope definition should be revisited.
- If fewer than 20% of gaps are dropped in Pass 1, flag this as a potential quality issue with the input gaps (too many redundant or vague gaps).
- The candidate set size (top-K) is a hard cap — do not expand it even if many gaps tie at the cutoff score. Break ties by Importance first, then Feasibility.
