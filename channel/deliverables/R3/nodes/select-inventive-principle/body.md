# select-inventive-principle
## Purpose
Select TRIZ inventive principles appropriate to a contradiction or transformation objective and state why each applies.
## Input contract
```yaml
required: [contradiction_statement, improvement_parameter, worsening_parameter]
optional: [system_components, operating_conditions, candidate_principles]
constraints: [selection must cite the contradiction and a concrete transformation rationale]
```
## Procedure
1. Normalize the contradiction and identify the improving and worsening parameters.
2. Consider the full 40-principle TRIZ vocabulary individually: 1 Segmentation; 2 Taking out; 3 Local quality; 4 Asymmetry; 5 Merging; 6 Universality; 7 Nested doll; 8 Counterweight; 9 Preliminary anti-action; 10 Preliminary action; 11 Beforehand cushioning; 12 Equipotentiality; 13 The other way round; 14 Spheroidality/curvature; 15 Dynamics; 16 Partial or excessive action; 17 Another dimension; 18 Mechanical vibration; 19 Periodic action; 20 Continuity of useful action; 21 Skipping; 22 Blessing in disguise; 23 Feedback; 24 Mediator; 25 Self-service; 26 Copying; 27 Cheap short-living objects; 28 Mechanics substitution; 29 Pneumatics/hydraulics; 30 Flexible shells/thin films; 31 Porous materials; 32 Color changes; 33 Homogeneity; 34 Discarding and recovering; 35 Parameter changes; 36 Phase transitions; 37 Thermal expansion; 38 Strong oxidants; 39 Inert atmosphere; 40 Composite materials.
3. For each principle, mark applicable, rejected, or not testable and state the contradiction-specific reason.
4. Rank applicable principles and pass the selected set to transformation.
## Output contract
```yaml
produces: [principle_applicability_matrix, selected_principles, selection_rationale]
delta_fields: [findings, hypothesis_updates, uncertainties, decisions, recommended_jumps]
```
## Quality gates
- All 40 principles appear individually; every selected principle has a contradiction-specific rationale and every rejected principle has a recorded reason.
## Failure and counterexamples
Reject “appropriate principle” summaries, selections without parameter mapping, or principle names detached from a proposed transformation.
## Provenance map
- `triz/contradiction-matrix`: concept (no exact pool entry).
- `inventive-principle-selection`: concept (no exact pool entry).
