---
name: variable-identification
description: 'SOP: identify variables and their roles within a hypothesis'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: Mechanism description (from mechanism-extraction output)
output: 'Variable list + role annotation (IV/DV/mediator/moderator/control) + operationalizability assessment'
dependencies:
  skills:
  - subagent-spawning
---

# Variable Identification
Identify all variables from a mechanism description and annotate their roles within the hypothesis structure.

## HARD-GATE
<HARD-GATE>
Preconditions (all must hold before starting):
1. At least 1 causal mechanism chain has been provided
2. The mechanism chain contains identifiable variable names

Not met → stop, return error: mechanism description is insufficient to identify variables.
</HARD-GATE>

## Pipeline
1. Precondition check: verify mechanism chain completeness
2. Variable extraction: enumerate all variables from every mechanism chain (including implicit variables)
3. Role classification: assign a role to each variable (IV/DV/mediator/moderator/control/confound)
4. Deduplication and merging: when the same variable appears in different mechanisms, merge it and annotate multiple roles
5. Operationalizability assessment: evaluate whether each variable can be measured (high/medium/low/unclear)
6. Output a structured variable list

## Output Format
```json
[
  {
    "name": "Variable name",
    "role": "IV | DV | mediator | moderator | control | confound",
    "description": "What this variable represents",
    "source_mechanism": ["mechanism name(s) where this variable appears"],
    "operationalizable": "high | medium | low | unclear",
    "operationalization_notes": "How it might be measured or manipulated"
  }
]
```
Identify at least 2 variables (1 IV + 1 DV).
