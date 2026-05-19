# Stakeholder-Weighted Ranking — Subagent Dispatch Prompt

You are executing the stakeholder-weighted ranking strategy for gap prioritization.

## Your Task

Rank research gaps by first constructing a separate priority ranking for each stakeholder class, then merging the per-stakeholder rankings into a consensus order. Surface both the consensus and the disagreements.

## Process

1. **Normalize gaps**: Ensure each gap has a consistent format — ID, one-sentence description, domain tag.

2. **Identify stakeholder classes**: List all groups that would be affected by or interested in this research. Use the research domain context to infer relevant stakeholders. Typical classes:
   - Academic researchers (value: novelty, rigor, generalizability)
   - Engineers / practitioners (value: feasibility, deployability, cost)
   - Policy makers / funders (value: societal impact, scalability, safety)
   - End users / patients / affected populations (value: direct benefit, accessibility)
   
   Add or remove classes based on the specific research domain. Minimum 2 classes required.

3. **Assign weight vectors per stakeholder**: For each stakeholder class, define a weight vector over the four scoring dimensions (Importance, Feasibility, Novelty, Impact). Weights must sum to 1.0.

   Default weight vectors:
   - Academic researchers: Importance 0.30, Feasibility 0.10, Novelty 0.40, Impact 0.20
   - Engineers: Importance 0.20, Feasibility 0.40, Novelty 0.10, Impact 0.30
   - Policy makers: Importance 0.35, Feasibility 0.15, Novelty 0.05, Impact 0.45
   - End users: Importance 0.40, Feasibility 0.25, Novelty 0.05, Impact 0.30

4. **Score each gap on four dimensions** (1–5 scale, dimension-first to avoid anchoring):
   - Importance, Feasibility, Novelty, Impact

5. **Compute per-stakeholder rankings**: For each stakeholder class, apply that class's weight vector to compute a weighted score per gap, then rank.

6. **Merge rankings via Borda count**: For each gap, sum its rank positions across all stakeholder classes (lower sum = higher Borda score). The consensus ranking is by ascending Borda sum.

7. **Identify divergent gaps**: Flag gaps where the rank spread across stakeholders exceeds 3 positions. For these, note which stakeholder values them highly and which does not.

8. **Synthesize output**: Present the consensus ranking, per-stakeholder rankings, and a divergence analysis.

## Output Format

### Per-Stakeholder Rankings
One table per stakeholder class showing gap ID, weighted score, and rank.

### Consensus Ranking (Borda Count)

| Gap ID | Borda Sum | Consensus Rank | Notes |
|--------|-----------|----------------|-------|
| G-01   | …         | …              | …     |

### Divergence Analysis
List gaps with rank spread > 3. For each: which stakeholder ranks it high, which ranks it low, and the likely reason for the disagreement.

### Top-N Attack Recommendations
For the top gaps by consensus ranking: gap ID, which stakeholders align, which disagree, and a recommended framing that acknowledges the divergence.

## Rules

- Weight vectors must sum to 1.0. If you adjust defaults, state the adjusted values explicitly.
- Score the four dimensions once (not per stakeholder) — stakeholder differences are expressed through weights, not through different dimension scores.
- The Borda count merge is the required consensus method. Do not substitute weighted average of rankings without explicit instruction.
- Divergence is information, not a problem to solve. Do not suppress or smooth over gaps where stakeholders disagree — report them clearly.
- Minimum 2 stakeholder classes. If only 1 class is relevant, switch to multi-criteria-ranking instead.
