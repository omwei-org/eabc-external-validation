# IV-002 Run 004 — Frozen Independent-Ingest Fixtures

This directory freezes six controlled EABC/TRACE source-fixture pairs for independent ARGUS ingestion.

**Important provenance boundary:** these are controlled replay fixtures derived from the IV-002 controlled event. They are not a recovered copy of the unrecovered public TRACE runtime artifact `call-material-move-001`. The TRACE inputs use the public TRACE action-receipt conformance shape; the EABC inputs use the controlled IV-002 EABC artifact shape.

## Cases

| Case | Controlled perturbation | Expected classification |
|---|---|---|
| E1 | Nominal shared event | CORRELATED |
| E2 | TRACE `call_id` and receipt binding changed | UNRESOLVED |
| E3 | TRACE `action_ref` changed | TRACE_INTEGRITY_FAILURE |
| E4 | EABC governed-action digest changed | EXECUTION_DIVERGENCE |
| E5 | EABC execution authority invalidated | AUTHORITY_FAILURE |
| E6 | EABC commit removed | COMMIT_FAILURE |

Each case contains exactly two source inputs: `eabc.json` and `trace.json`.

The independent ARGUS ingest must read these files as source inputs and derive its own result. The table above is the frozen experimental expectation, not an ARGUS result.

## Integrity identifiers

`MANIFEST.sha256` is reserved for byte-level SHA-256 values. The current manifest records the Git blob SHA-1 for every frozen file as an additional repository-level integrity identifier. Independent consumers should compute SHA-256 directly over the checked-out file bytes before ingestion.

## Claim boundary

A passing independent ingest demonstrates reproducibility of this controlled experiment. It does not establish recovery of the original public TRACE artifact, production runtime provenance, or semantic equivalence between TRACE and EABC.
