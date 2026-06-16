---
name: gap-normalization
description: 'SOP: Unify gaps from different sources into the standard GapRecord format'
version: 1.0.0
category: hypothesis-formation
type: sop
campaign: gap-prioritization
input: Raw gap entries from different sources (string list, structured objects, or mixed format)
output: GapRecord[] — array of standardized gap records
dependencies:
  skills:
  - subagent-spawning
---

# Gap Normalization

Unify gaps from different sources into the standard GapRecord format.

## HARD-GATE

<HARD-GATE>
- Input must not be empty: must contain at least 1 raw gap entry
- Each output GapRecord must contain non-empty id, title, description, domain, and source fields
- If any required field cannot be extracted, the entry is marked `status: "incomplete"` rather than silently dropped
</HARD-GATE>

## Pipeline

1. **Precondition check**: Verify input is non-empty; count the entries; identify the input format (plain text / JSON / mixed)
2. **Format identification**: Determine the format type of each entry — free-text description, partially structured object, fully structured object
3. **Field extraction**: Extract id (generate or reuse), title, description, domain, source, evidence, context from each raw entry
4. **Normalization**: Denoise and truncate title (≤120 characters); complete description into full sentences; map domain to a controlled vocabulary
5. **Validation**: Check the completeness of required fields for each GapRecord; tag incomplete entries with `status: "incomplete"` and record the missing fields
6. **Output**: Return GapRecord[] and a processing summary (total / complete / incomplete)

## Output Format

```json
{
  "records": [
    {
      "id": "gap_001",
      "title": "Short title (≤120 characters)",
      "description": "Full description (1-3 sentences)",
      "domain": "Domain label",
      "source": "Source identifier",
      "evidence": "Supporting evidence (optional)",
      "context": "Background information (optional)",
      "status": "complete | incomplete",
      "missing_fields": []
    }
  ],
  "summary": {
    "total": 0,
    "complete": 0,
    "incomplete": 0
  }
}
```
