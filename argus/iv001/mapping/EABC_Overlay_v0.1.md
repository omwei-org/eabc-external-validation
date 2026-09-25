# IV-001 EABC Authority/Commit Evidence Overlay v0.1

**Status:** Ready for bilateral validation run  
**Scope:** EABC-side authority, commit, execution-outcome and evidence-integrity mapping

## 1. Evidence basis

The EABC-side evidence model records the lifecycle of a governed execution:

```
PREPARE
→ FINAL_AUTHORITY_CHECK
→ COMMIT
→ EXECUTION
```

The concrete evidence record is a `CommitEvidence` object containing:

- `stage`
- `command_id`
- `env_id`
- `action_digest`
- `execution_epoch`
- `authority_epoch`
- `authorization_decision`
- `authorization_reason`
- `safety_decision`
- `safety_reason`
- `commit_decision`
- `commit_reason`
- `execution_outcome`
- `applied`
- `timestamp`
- `prev_hash`
- `record_hash`

## 2. Classification

| Mapped element | Classification | EABC-side statement |
|---|---|---|
| Exact governed action / payload binding | IMPLEMENTED | `action_digest` binds the governed execution object |
| Authorization decision | IMPLEMENTED | Recorded with decision and reason |
| Authority state / epoch | IMPLEMENTED | Execution and authority epochs are recorded |
| Final authority check | IMPLEMENTED | Authority is revalidated immediately before commit |
| Commit decision | IMPLEMENTED | Commit decision and reason are recorded |
| Execution outcome | IMPLEMENTED | Outcome and applied state are recorded |
| Evidence integrity | IMPLEMENTED | Evidence records use an integrity-protected hash chain |
| Observed effect | EXPERIMENTAL | Effect observation can be supplied by the validation fixture |
| Exact commit → observed-effect correlation | GAP | A separate effect-correlation binding is not yet established |
| Downstream reconstruction | PENDING | Performed by the ARGUS-side verifier |

## 3. Important semantic boundary

An authorization decision does not by itself prove execution.

An execution outcome does not by itself prove that the observed downstream effect is the exact effect governed by the committed action.

Therefore IV-001 explicitly tests:

```
Exact Governed Action
→ Authorization
→ Commit
→ Exact Effect Correlation
→ Observed Effect
```

## 4. Evidence integrity

The current evidence implementation uses a SHA-256 hash chain. Each record contains `prev_hash` and `record_hash`; the first record uses a defined genesis value.

This establishes evidence-record integrity within the released evidence sequence. It does not, by itself, establish physical-world effect integrity.

## 5. Effect-correlation requirement for IV-001

The validation lane should preserve a concrete correlation record containing, at minimum:

```text
command_id
effect_digest
observed_at
effect_status
effect_source
integrity_reference
```

The purpose is not to introduce a new normative EABC field set. It is an experimental validation artifact used to determine whether an independent verifier can bind:

```
Exact Governed Action → Authorization → Commit → Observed Effect
```

## 6. Known implementation boundary

Where an execution path transforms the actuator payload after the final commit decision, the EABC-side `action_digest` proves the identity of the governed execution object, but does not automatically prove that the resulting actuator-level effect is byte-identical to that object.

This is therefore treated as an IV-001 validation question rather than silently assumed to be established.

## 7. Verifier interpretation

The verifier should distinguish:

- **ALLOW** — authority/authorization condition was satisfied.
- **EXECUTED** — an execution outcome was recorded.
- **CORRELATED** — released evidence independently binds the committed action to the observed effect.
- **INCONCLUSIVE** — the available evidence is insufficient to establish the requested relationship.

The intended conclusion is the narrowest one supported by the released corpus.
