---
name: weakness-classification
description: Classifies discovered weaknesses into severity tiers (fatal/major/minor/cosmetic)
  with structured justification and exploitability assessment.
execution: subagent
prompt: ./prompt.md
input: raw_finding (string), artifact_context (string)
dependencies:
  sops:
  - spawn-agent
---

# Weakness Classification

Classifies discovered weaknesses into severity tiers.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Classification requires careful reasoning about impact scope and exploitability — dedicated context prevents bias from the discovery process.

## Input

- **raw_finding**: The weakness finding with context from discovery
- **artifact_context**: The original artifact being validated

## Output

- **severity**: `fatal` | `major` | `minor` | `cosmetic`
- **category**: type of weakness (logical, evidential, methodological, scope, assumption, implementation)
- **justification**: why this severity level
- **exploitability**: how easily this weakness could be exploited/triggered in practice

## Classification Scheme

- **fatal**: Invalidates the core claim — artifact cannot be used as-is
- **major**: Significantly undermines validity but not fatal — requires substantial revision
- **minor**: Weakens periphery — addressable without fundamental changes
- **cosmetic**: Presentation/clarity issue only — does not affect validity

## Budget

One unit = one classification. Called per finding.
