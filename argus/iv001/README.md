# PAMIR ARGUS × EABC — IV-001

This directory contains the EABC-side material for the **PAMIR ARGUS × EABC Interoperability Validation 001**.

## Validation question

Can an independent verifier establish, from released evidence alone, that a specific downstream effect corresponds to a specific action that was validly authorized and committed at the EABC execution-authority boundary?

## Boundary

The validation chain is:

```
Exact Governed Action
→ Authorization
→ Commit
→ Observed Effect
→ Reconstruction
```

The ARGUS-side validation package supplies the transaction fixtures and downstream reconstruction procedure. The EABC side supplies the authority/commit evidence overlay and its classification.

The serialized IV-001 corpus is experimental. It is not a new normative EABC schema and does not modify the ARGUS baseline.

## Planned contents

- `mapping/` — bilateral mapping and EABC evidence overlay
- `fixtures/` — validation fixtures received for IV-001
- `evidence/` — released evidence artifacts and manifests
- `verifier/` — independent-verifier procedure and results

## Current EABC-side status

| Element | Status |
|---|---|
| Exact Governed Action | ESTABLISHED |
| Authorization | ESTABLISHED |
| Commit | ESTABLISHED |
| Execution Outcome | ESTABLISHED |
| Evidence Integrity | ESTABLISHED |
| Observed Effect | AVAILABLE EXPERIMENTALLY |
| Exact Effect Correlation | NOT YET ESTABLISHED |
| Downstream Reconstruction | PENDING ARGUS RUN |

The open validation question is deliberately narrow: whether the released evidence independently binds the **exact committed action** to the **observed downstream effect**.

## Evidence rule

```
ALLOW ≠ EXECUTION
EXECUTION ≠ EVIDENCE
MISSING EVIDENCE ≠ EXECUTION FAILURE
UNKNOWN / INCONCLUSIVE = valid result
```
