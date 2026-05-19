---
name: legal-status-assessment
description: Determine patent legal status — active, expired, pending, lapsed, or revoked
execution: subagent
prompt: ./prompt.md
input: patent_identifiers
used-by: patent-mining
---

# Legal Status Assessment

Determines the current legal status of patents (active/granted, pending/application, expired, lapsed, revoked) based on available metadata and filing information.
