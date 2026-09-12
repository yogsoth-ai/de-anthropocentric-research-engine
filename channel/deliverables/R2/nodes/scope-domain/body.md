# scope-domain
## Purpose
Define ontology or model scope, inclusion boundaries, granularity, and intended use before structural extraction.
## Input contract
```yaml
required: [domain_question, seed_concepts, intended_use]
optional: [source_corpus, granularity_target, exclusion_rules, resource_budget]
constraints: [scope boundaries, inclusion criteria, granularity, and intended use are explicit]
```
## Procedure
1. State the domain question, seed concepts, intended users, and decisions the model must support.
2. Set inclusion/exclusion boundaries and the target granularity for entities and relations.
3. Test boundary examples, record out-of-scope items, and freeze the initial scope ledger.
4. Emit the scoped domain specification and a trigger for reopening it.
## Output contract
```yaml
produces: [domain_scope, inclusion_rules, exclusion_rules, granularity_spec, scope_ledger]
delta_fields: [findings, assumption_updates, uncertainties, decisions, open_questions]
```
## Quality gates
- Scope includes a question, seed concepts, boundary rule, granularity, and intended use.
- Out-of-scope examples are recorded so later extraction cannot silently widen the domain.
## Failure and counterexamples
Do not let the available corpus define the domain boundary. If granularity changes the intended decision, stop and reopen scope.
## Provenance map
- resolved: domain-scoping
