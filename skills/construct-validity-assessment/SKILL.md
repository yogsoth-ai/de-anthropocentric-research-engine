---
name: construct-validity-assessment
description: Evaluate whether benchmark measures its claimed capability
execution: subagent
prompt: ./prompt.md
input: benchmark_name, claimed_capability, task_examples
used-by: benchmark-archaeology
---

# Construct Validity Assessment SOP

Evaluate whether a benchmark actually measures the capability it claims to measure, using psychometric validity frameworks adapted for AI evaluation.

## Input

- **benchmark_name**: Name of the benchmark
- **claimed_capability**: What the benchmark authors claim it measures
- **task_examples**: Representative examples from the benchmark

## Procedure

1. Define the construct (claimed capability) precisely
2. Analyze task requirements — what skills are actually needed to solve examples?
3. Assess content validity — do items representatively sample the construct?
4. Check convergent validity — correlation with other measures of same construct
5. Check discriminant validity — independence from unrelated constructs
6. Identify construct-irrelevant variance (confounds)

## Output

Validity verdict with evidence for each validity dimension.
