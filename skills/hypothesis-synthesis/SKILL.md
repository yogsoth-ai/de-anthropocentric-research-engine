---
name: hypothesis-synthesis
description: 'SOP: synthesize all intermediate products into a final structured hypothesis set'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: All intermediate products (theories, mechanisms, variables, relationships, boundary conditions, falsifiability, competing hypotheses, comparison matrix)
output: Final hypothesis document (complete 6-component structure + ranking + relationship notes)
dependencies:
  skills:
  - subagent-spawning
---

# Hypothesis Synthesis
Collect and integrate all intermediate products to produce a complete, deduplicated, ranked final hypothesis set.

## HARD-GATE
<HARD-GATE>
Preconditions (all must hold before starting):
1. There are ≥2 hypothesis candidates (from any upstream step)
2. Each hypothesis has at least statement + mechanism + falsification_scenario

Not met → stop, return error: insufficient hypothesis candidates or missing required components.
</HARD-GATE>

## Pipeline
1. Precondition check: verify completeness of all intermediate products
2. Collect all hypothesis candidates: aggregate every hypothesis from the deductive/inductive/abductive paths
3. Deduplication and merging: identify and merge hypotheses with the same mechanism (keep the most complete version)
4. Completeness check: ensure each hypothesis contains all 6 components (statement/variables/mechanism/boundary_conditions/falsification/measurability)
5. Ranking: rank comprehensively by evidence support + testability + theoretical importance
6. Relationship notes: annotate the relationships between hypotheses (complementary/competing/independent/hierarchical)
7. Format and output the final hypothesis document

## Output Format
```json
{
  "summary": {
    "total_hypotheses": 3,
    "primary_hypothesis": "H1",
    "reasoning_path": "deductive | inductive | abductive | mixed"
  },
  "hypotheses": [
    {
      "hypothesis_id": "H1",
      "priority": 1,
      "statement": "If X then Y under conditions Z",
      "variables": {
        "independent": "X",
        "dependent": "Y",
        "mediators": [],
        "moderators": [],
        "controls": []
      },
      "mechanism": "Causal chain explanation",
      "boundary_conditions": {
        "temporal": "...",
        "spatial": "...",
        "population": "...",
        "conditional": [],
        "exclusions": []
      },
      "falsification": {
        "scenario": "...",
        "testability": "high | medium | low"
      },
      "measurability": {
        "iv_measure": "...",
        "dv_measure": "..."
      },
      "evidence_support": "strong | moderate | weak | none",
      "theoretical_basis": "Theory name(s)"
    }
  ],
  "hypothesis_relationships": [
    {
      "pair": "H1 and H2",
      "relationship": "complementary | competing | independent | hierarchical",
      "notes": "..."
    }
  ],
  "recommended_next_step": "Which hypothesis to develop into a research question first, and why"
}
```
