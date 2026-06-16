---
name: contamination-audit
description: Detect train-test data leakage and memorization artifacts
execution: subagent
prompt: ./prompt.md
input: benchmark_name, training_data_sources, test_set_metadata
dependencies:
  sops:
  - spawn-agent
---

# Contamination Audit SOP

Detect evidence of train-test data leakage, benchmark contamination, and memorization artifacts that inflate reported scores beyond genuine capability.

## Input

- **benchmark_name**: Name of the benchmark being audited
- **training_data_sources**: Known or suspected training data sources for models evaluated on this benchmark
- **test_set_metadata**: Information about the test set (size, creation date, source, public availability)

## Procedure

1. Assess temporal contamination risk (test data predates training cutoff?)
2. Check for known contamination disclosures in model papers
3. Search for contamination studies specific to this benchmark
4. Analyze performance patterns indicative of memorization
5. Assess mitigation measures (canary strings, held-out splits, version rotation)

## Output

Contamination risk assessment with evidence and confidence levels.

<!-- BEGIN available-tables (generated) -->

## Available SOPs

Optional, no fixed order; the final leaf is always a sop.

| SOP | When to use |
| --- | --- |
| spawn-agent | Spawn a customized CC subagent with full MCP tool access. Used by SOPs that declare execution: subagent. |

<!-- END available-tables (generated) -->
