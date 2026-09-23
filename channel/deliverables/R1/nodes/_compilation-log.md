# GROUP A compilation log

## Batch 1

10 nodes; A=11, B=1, C=0; unresolved provenance=19.

## Batch 2

10 nodes; A=1, B=9, C=0; unresolved provenance=4.

## Batch 3

10 nodes; A=0, B=10, C=0; unresolved provenance=12.

## Batch 4

10 nodes; A=1, B=9, C=0; unresolved provenance=3.

## Batch 5

4 nodes; A=2, B=2, C=0; unresolved provenance=4.

All 44 R1 GROUP A node bodies are present. No git writes performed.

## Provenance rework

44 existing nodes rechecked against v3 `nodes[].name` using bare, package-name, and package/name forms; 42 previously misclassified entries changed to `resolved`, with real v3 names restored. Remaining `concept`/`intermediate` entries were not found by all three forms.

## Redistribution batches

21 additional SOPs delivered in two batches: HYPOTHESIS 13 and STRUCTURING 8. Batch 1: 10 nodes, A=0/B=10/C=0, provenance resolved=10/concept=0/intermediate=0. Batch 2: 11 nodes, A=0/B=11/C=0, provenance resolved=11/concept=0/intermediate=0. Mechanical gates 1–4 self-check passed for both batches.
