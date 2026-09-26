# ARGUS × EABC — IV-002 Shared Controlled Event

IV-002 is a minimal controlled experiment for testing whether TRACE-shaped evidence and EABC execution-authority evidence can be independently correlated to the same execution event.

This is a new controlled event. It is **not** the original public TRACE fixture and does not claim to reproduce an AgenTrust/TRACE runtime execution.

## Validation question

Can an independent verifier establish the binding between two independently produced evidence artifacts when both sides record a pre-agreed event identifier and independently computable action/payload digests?

## Cases

| Case | Condition | Expected result |
|---|---|---|
| E1 | Shared event ID and consistent digests | CORRELATED |
| E2 | Shared event ID, but EABC post-gate transform changes the governed action | CORRELATED + EXECUTION_DIVERGENCE |
| E3 | TRACE evidence has no matching event binding | UNRESOLVED |

## Claim boundary

IV-002 establishes a **reproducible cross-source event-binding fixture**.

It does not establish:
- that TRACE itself produced the fixture;
- a cryptographically signed TRACE Trust Record;
- production interoperability;
- physical execution;
- security certification or bypass resistance.

The EABC artifact is generated deterministically from the controlled inputs. The TRACE-side artifact, when supplied, must be independently represented as a controlled TRACE-shaped fixture rather than as the original public TRACE `call-material-move-001`.
