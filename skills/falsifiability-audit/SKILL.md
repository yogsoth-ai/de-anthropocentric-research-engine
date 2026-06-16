---
name: falsifiability-audit
description: 'Tactic: hypothesis quality assurance — check falsifiability, repair failing hypotheses, complete operationalization and boundary-condition specification'
version: 1.0.0
category: hypothesis-formation
type: tactic
campaign: hypothesis-formulation
sops:
- falsifiability-check
- operationalization
- boundary-condition-specification
dependencies:
  sops:
  - boundary-condition-specification
  - falsifiability-check
  - operationalization
---

# Falsifiability Audit

Hypothesis quality assurance — check each hypothesis in the set for falsifiability, repair failing hypotheses, complete operational definitions, and specify boundary conditions, ensuring every hypothesis can be tested by experiment or observation.

## Orchestration Intent

The final gate of hypothesis formation. No matter how good the theoretical foundation, if the resulting hypotheses cannot be falsified, they are not scientific hypotheses. This tactic's job is "quality control," not "generation": the input is a set of existing hypothesis candidates, and the output is the proof document that each hypothesis has passed QC.

The three SOPs form a pipeline: falsifiability-check identifies problems → operationalization converts variables into measurable form → boundary-condition-specification delimits the range within which the hypothesis holds. No step skipping is allowed, and advancing directly when falsifiability-check fails is not allowed.

## Available SOPs

| SOP | Responsibility | When to call |
|-----|------|---------|
| falsifiability-check | Run a falsifiability check on each hypothesis, identify unfalsifiable hypotheses, and propose fixes | Required in all modes, executed first; if any hypothesis fails, iterate the fix and re-check |
| operationalization | Provide operational definitions for each hypothesis's variables — how to measure, with what instrument, under what conditions | Required in all modes, executed after falsifiability-check passes |
| boundary-condition-specification | Specify the preconditions, scope of applicability, and known limitations under which the hypothesis holds | Required in all modes, executed last |

## Orchestration Pattern

**Simplified (S tier, ≤3 hypotheses)**
- Sequential execution: falsifiability-check → operationalization → boundary-condition-specification
- If any hypothesis fails falsifiability-check, CC immediately repairs and re-checks it (at most 2 iterations)
- Suited to: few hypotheses, expected to be of higher quality

**Standard (M tier, 4-6 hypotheses)**
- falsifiability-check runs in batch over all hypotheses, compiling a failure list; CC repairs in batch; re-check the repaired hypotheses
- operationalization and boundary-condition-specification run in series
- Suited to: medium-sized hypothesis sets needing systematic QC

**Deep (L tier, ≥7 hypotheses)**
- All 3 SOPs run; falsifiability-check additionally outputs the "strongest counterexample scenario" for each hypothesis; operationalization additionally requires ≥2 measurement methods per variable (primary + alternative); boundary-condition-specification additionally requires listing known exceptions
- Suited to: large hypothesis sets needing production-grade quality assurance

## Minimum Yield

- Every input hypothesis has passed falsifiability-check (or has been repaired until it passes)
- Every variable of every hypothesis has an operational definition (including measurement instrument/method)
- Every hypothesis has explicit boundary conditions (the preconditions under which it holds + the situations where it does not apply)
- A complete QC record: which hypotheses passed on the first try, which passed after repair, and what the repairs were

## Yield Report

After execution, report to the calling strategy:
- Number of input hypotheses / first-pass count / post-repair pass count / final fail count
- The most common type of falsifiability problem (to help the upstream strategy improve hypothesis generation)
- Operationalization difficulty: which variables are hard to measure (requiring special instruments or datasets)
- Boundary-condition coverage: which hypotheses have a narrow scope of applicability (high risk, easily overturned by counterexamples)

<!-- BEGIN available-tables (generated) -->

## Available SOPs

可选,无固定顺序;最终叶子终为 sop。

| SOP | 何时用 |
| --- | --- |
| boundary-condition-specification | SOP: 指定假设成立的边界条件 |
| falsifiability-check | SOP: 检验假设是否满足可证伪性标准 |
| operationalization | SOP: 将抽象概念操作化为可测量的指标和方法 |

<!-- END available-tables (generated) -->
