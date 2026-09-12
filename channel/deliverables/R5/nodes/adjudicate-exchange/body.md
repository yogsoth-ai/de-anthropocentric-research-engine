# adjudicate-exchange
## Purpose
Evaluate competing arguments against stated criteria and produce a reasoned verdict with uncertainty.
## Input contract
```yaml
required: [arguments, critique_set, adjudication_criteria]
optional: [evidence_records, burden_of_proof, verdict_vocabulary]
constraints: [each argument and critique receives an explicit disposition]
```
## Procedure
1. Normalize claims, warrants, evidence, and objections.
2. Map each objection to the argument component it tests.
3. Weigh support and weaknesses against the supplied criteria.
4. Emit ACCEPT, REJECT, or REVISE with conditions and uncertainty.
## Output contract
```yaml
produces: [verdict, argument_dispositions, conditions, uncertainty_statement]
delta_fields: [decisions, findings, uncertainties]
```
## Quality gates
- Every argument and critique is addressed explicitly.
- Evidence is weighed without prior commitment to either side.
- Verdict vocabulary and conditions are caller-visible.
## Parameterization
Caller supplies argument schema, critique schema, criteria, burden of proof, and verdict vocabulary.
## Failure and counterexamples
Reject verdicts that omit objections, rely on prior commitment, or collapse uncertainty into confidence.
## Provenance map
- concept: stress-test/debate-judge
- concept: convergence/judge-verdict
