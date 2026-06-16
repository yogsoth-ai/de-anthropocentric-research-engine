---
name: mechanism-extraction
description: 'SOP: extract causal mechanism chains from a theory'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: 'Theory description (from theory-identification output)'
output: 'List of causal mechanism chains (X → mediator → Y) + mechanism diagram'
dependencies:
  skills:
  - subagent-spawning
---

# Mechanism Extraction
Extract structured causal mechanisms from a theory description, providing a skeleton for variable identification and hypothesis construction.

## HARD-GATE
<HARD-GATE>
Preconditions (all must hold before starting):
1. At least 1 theory description is provided (including core_claim)
2. The theory description is specific enough to identify at least 2 variables

Not satisfied → stop, return error: the theory description is too vague to extract a mechanism.
</HARD-GATE>

## Pipeline
1. Precondition check: verify completeness of the theory description
2. Causal chain identification: identify X → Y causal-relation statements in the theory text
3. Mediator extraction: identify intermediate variables (mediators) between X and Y
4. Mechanism naming: give each mechanism chain a short descriptive name
5. Mechanism diagram construction: represent as a directed graph (text ASCII or JSON nodes/edges)
6. Output a structured mechanism list

## Output Format
```json
[
  {
    "name": "Mechanism name",
    "chain": "X → mediator → Y",
    "variables": {
      "cause": "X description",
      "mediator": "mediator description (null if direct)",
      "effect": "Y description"
    },
    "source_theory": "Theory name this was extracted from",
    "direction": "positive | negative | conditional",
    "notes": "Any caveats or conditions"
  }
]
```
Extract at least 1 mechanism chain per theory; at least 2 in total.
