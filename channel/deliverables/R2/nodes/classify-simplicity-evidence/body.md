# classify-simplicity-evidence
## Purpose
Classify explanatory compression as earned, weak, or decorative.
## Input contract
```yaml
required: [explanation, covered_facts, alternatives, predictions]
optional: [evidence]
constraints: [facts and alternatives must be independently listed]
```
## Procedure
1. Check whether independent facts are compressed.
2. Check whether alternatives are forbidden and predictions constrained.
3. Classify earned, weak, or decorative and preserve rationale.
## Output contract
```yaml
produces: [simplicity_class, compression_evidence, missing_constraints]
delta_fields: [findings, evidence_updates, uncertainties, decisions]
```
## Quality gates
- Decorative simplicity is a relabeling with no independent compression or risky prediction.
## Failure and counterexamples
Do not classify by description length or elegance alone.
## Provenance map
- resolved: elegance-trap-probe
