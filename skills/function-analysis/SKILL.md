---
name: function-analysis
description: 'FMEA Step 3: Decompose artifact into function tree — identify what each
  component is supposed to do before analyzing how it can fail.'
execution: subagent
prompt: ./prompt.md
input: artifact (string), artifact_type (string), analysis_mode (string)
dependencies:
  sops:
  - spawn-agent
---

# Function Analysis

Decomposes artifact into a hierarchical function tree per FMEA Step 3.

## Execution

Subagent — spawned via subagent-spawning/spawn-agent.

## Why Subagent

Function decomposition requires systematic analytical thinking without premature failure identification. Isolated context prevents jumping to conclusions.

## Input

- **artifact**: The artifact to decompose
- **artifact_type**: Type for tailored decomposition
- **analysis_mode**: "design" (what it should do) or "process" (how it executes)

## Output

- **function_tree**: Hierarchical list of functions and sub-functions
- **function_requirements**: What each function must achieve to succeed
