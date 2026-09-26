# IV-002 Shared Controlled Event

## Purpose

IV-002 tests whether independently produced TRACE-shaped evidence and EABC execution-authority evidence can be correlated to one controlled event through an explicit deterministic binding rule.

## Controlled event

`shared_event_id = iv002-shared-001`

- EABC uses `command_id`.
- TRACE uses `context.call_id`.
- CBA binds them using `call_id == command_id`.

This experiment-local rule does not claim general semantic equivalence between the two identifier models.

## Evidence boundary

EABC records its own authorization, execution-authority, commit, and effect fields.

TRACE follows the public action-receipt conformance shape and records an accepted controller decision. Its evidence explicitly makes no physical-completion claim.

CBA does not translate one evidence model into the other.

## E1 acceptance criteria

- TRACE artifact integrity matches its supplied SHA-256.
- EABC artifact integrity matches its supplied SHA-256.
- TRACE `call_id` equals EABC `command_id`.
- Both identifiers equal `iv002-shared-001`.

If all conditions hold, CBA returns `PASS`.

## Negative binding case

A negative case changes only the TRACE `call_id` to another identifier. The artifacts may remain individually intact, but CBA must return `FAIL` because the controlled-event binding no longer matches.
