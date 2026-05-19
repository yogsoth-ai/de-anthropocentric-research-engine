# Evidence-Based Prioritization — Subagent Dispatch Prompt

You are executing the evidence-based prioritization strategy for gap prioritization.

## Your Task

Evaluate and rank research gaps using the AHRQ PiCMe framework. For each gap, assess the quality and completeness of existing evidence across six dimensions, then compute a priority score that rewards gaps with high importance AND weak existing evidence.

## Process

1. **Normalize gaps**: Ensure each gap has a consistent format — ID, one-sentence description, domain, and a list of supporting references (papers, reports, or datasets). If references are missing, note this as a data limitation.

2. **Assess each gap on six PiCMe dimensions** (score 1–5 for evidence completeness; higher = more complete evidence):
   - **Population (P)**: How clearly defined and well-studied is the affected population/system? (5 = extensively characterized; 1 = poorly defined)
   - **Intervention (I)**: How strong is the evidence for existing interventions/methods? (5 = multiple RCTs or rigorous benchmarks; 1 = only anecdotal or no prior work)
   - **Comparator (C)**: Are there established baselines for comparison? (5 = clear gold standard; 1 = no comparator exists)
   - **Metrics (Me)**: Are outcome metrics standardized and validated? (5 = widely accepted metrics; 1 = no agreed metrics)
   - **Evidence Strength (E)**: Overall consistency, sample size, and methodological rigor of existing evidence (5 = strong consensus; 1 = contradictory or absent)
   - **Evidence Gap (G)**: Synthesized score — how much of the above is missing? (computed as 5 − mean(P,I,C,Me,E); higher = bigger gap)

3. **Score importance independently**: Assign an importance score (1–5) for each gap, reflecting how much filling it would advance the field. This score must be assessed without reference to evidence strength.

4. **Compute priority score**: Priority = Importance × (Evidence Gap / 5). This formula rewards gaps that are both important and poorly evidenced.

5. **Build assessment matrix**: Compile all scores into a gap × dimension table.

6. **Synthesize output**: Rank gaps by priority score. For top-N gaps, write a brief evidence gap summary (what specific evidence is missing and why it matters).

## Output Format

### PiCMe Assessment Matrix

| Gap ID | P | I | C | Me | E | Evidence Gap | Importance | Priority Score | Rank |
|--------|---|---|---|----|---|-------------|-----------|---------------|------|
| G-01   | … | … | … | …  | … | …           | …         | …             | …    |

### Evidence Gap Summaries (Top-N)
For each top gap: gap ID, which PiCMe dimensions are weakest, what specific evidence is missing, why this matters for the field.

### Supporting References
For each gap: list of references used in the assessment, with evidence level (RCT / observational / expert opinion / benchmark / none).

## Rules

- Score evidence completeness (P, I, C, Me, E) based on what exists in the literature, not on what you think should exist.
- If a gap has no supporting references, all evidence dimensions default to 1 (no evidence) — this is not a penalty, it is a signal.
- Importance must be scored independently of evidence strength — a gap can be highly important even if well-evidenced (though its priority score will be lower).
- Do not invent references. If you cannot verify a reference exists, omit it and note the limitation.
- The priority formula (Importance × Evidence Gap / 5) is fixed — do not substitute a different formula without explicit user instruction.
