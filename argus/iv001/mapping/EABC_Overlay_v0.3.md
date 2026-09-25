# EABC Authority / Commit Evidence Overlay v0.3
## PAMIR ARGUS × EABC — IV-001

**Status:** Experimental bilateral validation artifact  
**Source implementation:** `omwei-org/halos-1.3-atl-analysis`  
**Source branch:** `eabc-effect-correlation-004`  
**Validated CI commit:** `31d84ba7d911dbf7d2c9d355fe4eb290c537fdf3`  
**Run:** 004 — effect-correlation-and-transformation-detection

## Purpose

This overlay records the EABC-side evidence now available for the open IV-001 question:

> Can an independent verifier establish an exact binding between a governed action that was authorized and committed at the EABC boundary and the downstream effect observation?

Run 004 adds an integrity-protected `EffectCorrelationEvidence` record to the same append-only SHA-256 evidence chain used by `CommitEvidence`.

This is an **experimental implementation evidence artifact**. It does not modify the normative EABC schema and does not constitute physical-world attestation.

## Evidence fields

The Run 004 correlation record contains:

- `command_id`
- `env_id`
- `committed_action_digest`
- `actuator_payload_digest`
- `observation`
- `effect_digest`
- `effect_status`
- `observed_at`
- `effect_source`
- `prev_hash`
- `record_hash`

The correlation record is appended to the same integrity chain as the preceding EABC commit evidence.

## Case A — nominal

Command: `run004-a-001`

- governed action digest = actuator payload digest
- actuator observation reports the same applied-payload digest
- observed relay state = `true`
- effect status = `OBSERVED`
- evidence record is hash-chain linked

Resulting EABC-side evidence establishes a cryptographically linked PoC observation whose payload digest matches the governed action digest.

It still does **not**, by itself, establish that the observed relay state represents an independently attested physical-world effect.

## Case B — post-gate transformation

Command: `run004-b-001`

The governed action remains `RELAY:ON`, while the commit payload factory transforms the actuator payload to `RELAY:OFF`.

- committed action digest: `d9caaff4f46b50d88ef0d397bb0451f21972602f834cf7383a3796a23ba5fc07`
- actuator payload digest: `1bffb64d1d310eaa9f58fd25385989b9ad5befa24fd01675f68b4ae6d04422f2`
- observation applied-payload digest matches the actuator payload digest
- resulting relay state = `false`

This demonstrates that the evidence makes a post-gate transformation visible as a mismatch between the governed action and the actual actuator payload observed by the PoC adapter.

## Classification

| Element | Classification | Evidence |
|---|---|---|
| Command / lifecycle identity | IMPLEMENTED | `CommitEvidence.command_id` and Run 004 correlation record |
| Exact governed action binding | IMPLEMENTED | `action_digest` / `committed_action_digest` |
| Authorization decision | IMPLEMENTED | `CommitEvidence` |
| Authority epoch | IMPLEMENTED | `CommitEvidence.authority_epoch` |
| Final authority check | IMPLEMENTED | `FINAL_AUTHORITY_CHECK` |
| Commit decision | IMPLEMENTED | `CommitEvidence.commit_decision` |
| Execution outcome | IMPLEMENTED | `CommitEvidence.execution_outcome` |
| Evidence integrity | IMPLEMENTED | shared SHA-256 append-only chain |
| Actuator payload identity | EXPERIMENTAL | `actuator_payload_digest` |
| Observed effect material | EXPERIMENTAL | `observation` |
| Exact commit → observed-effect correlation | EXPERIMENTAL / OPEN VALIDATION | Run 004 correlation record |
| Physical-world attestation | GAP | outside current PoC adapter boundary |
| ARGUS downstream reconstruction | PENDING | independent ARGUS verifier |

## Important boundary

The new evidence closes an important **PoC evidence seam**:

`Exact Governed Action → Authorization → Commit → Actuator Payload → Observed Effect`

But the final step remains dependent on the trust properties of the effect source.

`RecordingRelay` is an instrumented test adapter. Its observation is deterministic and integrity-protected within the experiment, but it is not an independent physical-world attestation mechanism.

Therefore the appropriate IV-001 question for ARGUS is now narrower:

> Given the frozen v0.2 corpus plus this EABC-side Run 004 evidence, can an independent verifier establish the exact commit-to-observed-effect correlation required for Case A?

No PASS result is asserted by this overlay.

## Reproducibility

Run 004 CI:

- workflow run: 36097144900
- conclusion: SUCCESS
- artifact: `run-004-evidence`
- artifact SHA-256: `4c4548fb432782392cbc51797f10d45f1874abe9d8e516e9f84aec40c5b133b7`

Extracted evidence file SHA-256:

`a77c7ceef53e76a71668d6751a3bfd13c8056d52206297eada7f1e6421aab3dd`

The artifact and evidence file are retained here as validation references; the implementation remains sourced from `halos-1.3-atl-analysis`.

## Non-claims

This overlay does not claim:

- completed ARGUS interoperability;
- physical-world attestation;
- production deployment;
- security certification;
- regulatory approval;
- conformance to a normative ARGUS schema;
- that Case A is already validated end-to-end.
