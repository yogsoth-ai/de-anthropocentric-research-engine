---
name: anomaly-characterization
description: 'SOP: Describe and classify anomalous phenomena that existing theory cannot explain'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: hypothesis-formulation
input: Anomalous observation description (data, experimental results, literature contradictions)
output: Structured anomaly description (phenomenon + deviation quantification + classification + exclusion of known explanations)
dependencies:
  skills:
  - subagent-spawning
---

# Anomaly Characterization
Systematically describe and classify anomalous phenomena to provide a precise starting point for abductive reasoning.

## HARD-GATE
<HARD-GATE>
Preconditions (all must hold before starting):
1. A concrete anomalous observation description is available (not a vague "the result is strange")
2. A reference baseline exists (expected result or theoretical prediction) for quantifying deviation

Not satisfied → stop and return error: anomaly description insufficient, concrete observation and reference baseline required.
</HARD-GATE>

## Pipeline
1. Precondition check: verify completeness of anomaly description and reference baseline
2. Phenomenon description: restate the anomaly in precise language (what was observed vs. what was expected)
3. Quantify deviation from expectation: quantify or qualitatively describe the degree of deviation (magnitude, direction, frequency)
4. Exclude known explanations: enumerate and rule out possible trivial explanations one by one (measurement error, sampling bias, known effects)
5. Anomaly classification: categorize the anomaly (unexpected absence / unexpected presence / unexpected magnitude / unexpected pattern / unexpected timing)
6. Output structured anomaly description

## Output Format
```json
{
  "anomaly_id": "A1",
  "phenomenon": "Precise description of what was observed",
  "expected": "What theory or prior evidence predicted",
  "deviation": {
    "direction": "higher | lower | absent | present | different_pattern",
    "magnitude": "Quantitative or qualitative estimate",
    "frequency": "Isolated | recurring | systematic"
  },
  "excluded_explanations": [
    {"explanation": "...", "reason_excluded": "..."}
  ],
  "anomaly_type": "unexpected_absence | unexpected_presence | unexpected_magnitude | unexpected_pattern | unexpected_timing",
  "severity": "minor | moderate | major",
  "notes": "Additional context"
}
```
</output>
