# map-productive-polarity
## Purpose
Map a persistent two-pole tension where both poles contain value and require managed balance.
## Input contract
```yaml
required: [polarity_statement, pole_a, pole_b]
optional: [stakeholder_views, warning_signs, current_practices]
constraints: [each pole must have a valued upside and a harmful overuse pattern]
```
## Procedure
1. State the upside and downside of over-focusing each pole.
2. Identify warning signs that the system has over-corrected toward either pole.
3. Map practices that manage the polarity without falsely resolving it.
## Output contract
```yaml
produces: [polarity_map, upside_downside_register, warning_signs, management_practices]
delta_fields: [findings, assumption_updates, uncertainties, decisions]
```
## Quality gates
- Both poles remain legitimate; management practices are conditional and observable.
## Failure and counterexamples
Reject a polarity map that treats one pole as the correct answer or collapses tension into a compromise slogan.
## Provenance map
- `deep-insight/polarity-mapping`: resolved.
- `tension-mining`: resolved.
