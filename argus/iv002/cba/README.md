# IV-002 CBA — Shared Controlled Event Verification

This verifier binds independently generated EABC and TRACE-shaped artifacts to the same controlled event.

It does not assert semantic equivalence between TRACE and EABC, and it does not infer physical completion from a TRACE action receipt.

## Binding rule

For IV-002 only:

`TRACE.context.call_id == EABC.command_id == shared_event_id`

The rule is experiment-specific and does not claim that the native identifier models of TRACE and EABC are generally equivalent.

## Checks

1. Recompute SHA-256 of the complete TRACE artifact.
2. Recompute SHA-256 of the complete EABC artifact.
3. Compare both artifact hashes with the values supplied to the verifier.
4. Check `TRACE.context.call_id == EABC.command_id`.
5. Check both identifiers equal `iv002-shared-001`.
6. Report the result without translating TRACE evidence into EABC execution semantics.
