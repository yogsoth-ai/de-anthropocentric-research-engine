---
name: assignee-normalization
description: Standardize assignee names and identify corporate group affiliations across patent offices
execution: subagent
prompt: ./prompt.md
input: raw_assignee_list
used-by: patent-mining
---

# Assignee Normalization

Standardizes patent assignee names across different patent offices and identifies corporate group affiliations (parent companies, subsidiaries, acquired entities).
