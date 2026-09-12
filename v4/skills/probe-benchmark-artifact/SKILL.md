---
name: probe-benchmark-artifact
description: "Probe whether benchmark performance can be explained by shortcuts, artifacts, leakage, annotation cues, metric gaming, or non-target capabilities."
---

# probe-benchmark-artifact

## Purpose

Probe whether benchmark performance is explained by shortcuts, artifacts, leakage, annotation cues, metric gaming, or non-target capability.

## Input contract

```yaml
required: [benchmark, performance_records, construct_claim]
optional: [artifact_hypotheses, perturbation_set, contamination_audit]
constraints: [each probe has a target artifact, comparison, and interpretation rule]
```

## Procedure

1. Enumerate plausible shortcut and artifact pathways from the benchmark and construct.
2. Design matched perturbations or controls that isolate each pathway.
3. Compare performance and error patterns across target and control conditions.
4. Classify artifact evidence and update construct-validity uncertainty.

## Output contract

```yaml
produces: [artifact_hypotheses, probe_results, shortcut_evidence, construct_implications]
delta_fields: [findings, evidence_updates, uncertainties, decisions, open_questions]
```

## Quality gates

- Each probe has a declared control and interpretation rule.
- Artifact evidence is separated from ordinary variance.
- Acquisition sufficiency is reported as relative coverage of independent probes and artifact classes, with batch increment, stopping reason, source references, direction, and threshold rationale.

## Failure and counterexamples

Do not call a benchmark invalid because one perturbation lowers scores, and do not use a probe that changes the target capability and artifact simultaneously without qualification.

## Provenance map

- `resolved: artifact-detection`
