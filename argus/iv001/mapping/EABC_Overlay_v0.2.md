# IV-001 EABC Authority/Commit Evidence Overlay v0.2

**Source release:** PAMIR ARGUS × EABC — IV-001 Fixture Bundle v0.2  
**Source repository:** yigitcan-ozturk/pamir-argus-iv001-validation  
**Purpose:** bilateral validation mapping; not a normative EABC schema

## 1. Overlay rule

The v0.2 ARGUS fixtures are synthetic validation fixtures. The EABC overlay must not promote fixture assertions into EABC evidence merely because the fixture contains fields such as `authorization_decision`, `commit_state`, or `effect_digest`.

For each case, the verifier must distinguish:

```
Fixture assertion
    ≠
EABC-produced evidence
```

The EABC side therefore supplies only evidence actually supported by the EABC implementation/released evidence artifacts. Where the implementation cannot establish a requested relationship, the classification remains **GAP** or **INCONCLUSIVE**.

## 2. Common EABC mapping

| IV-001 element | EABC evidence / basis | Classification |
|---|---|---|
| `command_id` | `CommitEvidence.command_id` | IMPLEMENTED |
| `env_id` | `CommitEvidence.env_id` | IMPLEMENTED |
| Exact governed action | `action_digest` over governed execution object | IMPLEMENTED |
| Authorization | `authorization_decision` + reason | IMPLEMENTED |
| Authority state | `execution_epoch`, `authority_epoch` | IMPLEMENTED |
| Final authority check | final revalidation immediately before commit | IMPLEMENTED |
| Commit | `commit_decision` + reason | IMPLEMENTED |
| Execution outcome | `execution_outcome` + `applied` | IMPLEMENTED |
| Evidence integrity | `prev_hash` + `record_hash` SHA-256 chain | IMPLEMENTED |
| Observed effect | fixture observation | EXPERIMENTAL |
| Exact commit → observed-effect binding | requires concrete EABC-supported correlation evidence | GAP |
| Downstream reconstruction | ARGUS-side verifier | PENDING |

## 3. Case-by-case overlay

### A — IV001-A-NOMINAL

Fixture states:

- action digest: `sha256:1fb46e970e6acae7dac361a330bf3574e96152aa1582698f47f37fd5fbf31571`
- authorization: ALLOW
- commit: COMMITTED
- execution: COMPLETED
- observed effect: `RETURN_TO_BASE`
- effect digest: `sha256:ad40f1720490c49909404762b5009b8cd1e6f5c47911955b55196a13bdcb0071`
- temporal state: CONSISTENT

**EABC overlay status:** AUTHORIZATION/COMMIT SIDE MAPPABLE.  
**Open requirement:** concrete evidence binding the exact committed action to the observed effect.

The fixture's `integrity_reference` is `TO_BE_SUPPLIED_BY_EABC_OVERLAY`; it must not be replaced with an invented or merely semantic reference.

**Expected verifier posture:** do not declare the transaction fully correlated until the EABC-side evidence establishes the commit → effect relationship.

### B — IV001-B-AUTH-FAIL

Fixture states:

- authorization: DENY
- commit: NOT_COMMITTED
- execution: NOT_EXECUTED
- no observed effect

**EABC overlay:** the authorization-denial path is consistent with the EABC semantic model. Concrete EABC evidence must establish the denial and absence of commit/execution for the mapped command.

**Expected verifier posture:** AUTHORIZATION_DENIED if the released EABC evidence supports those facts.

No commit → effect correlation is required because the fixture does not claim a committed effect.

### C — IV001-C-EXEC-FAIL

Fixture states:

- authorization: ALLOW
- commit: FAILED
- execution: FAILED
- no observed effect

**EABC overlay:** authorization and attempted commit are mappable; the exact failure semantics require the concrete EABC execution evidence.

**Expected verifier posture:** EXECUTION_FAILED only if the EABC evidence supports the recorded failure. Do not infer a physical effect from ALLOW.

### D — IV001-D-EVIDENCE-FAIL

Fixture states:

- authorization: ALLOW
- commit: COMMITTED
- observed effect: `RETURN_TO_BASE`
- execution outcome: UNKNOWN
- evidence state: INCOMPLETE
- `integrity_reference`: null

**EABC overlay:** the fixture deliberately removes evidence needed for a stronger conclusion.

**Expected verifier posture:** INCONCLUSIVE unless independent EABC evidence outside the failed evidence path can establish the missing relationship.

This case is important because an observed effect does not repair missing execution/evidence integrity.

### E — IV001-E-CORRELATION-MISMATCH

Fixture states:

- authorized action requests `RETURN_TO_BASE`
- commit: COMMITTED
- execution: COMPLETED
- observed effect: `LAND`
- effect digest differs from nominal `RETURN_TO_BASE` effect

**EABC overlay:** authorization and commit can be established independently of the effect claim. The mismatch must remain visible.

**Expected verifier posture:** CORRELATION_MISMATCH, provided the effect observation and its digest are themselves trusted as validation evidence.

The case must not be normalized into a successful execution merely because authorization and commit were ALLOW/COMMITTED.

### F — IV001-F-TEMPORAL-DIVERGENCE

Fixture states:

- request: 04:00:06.000Z
- authorization: 04:00:06.010Z
- commit: 04:00:06.020Z
- observed effect: 03:59:06.900Z
- temporal state: INCONSISTENT

**EABC overlay:** the EABC lifecycle timestamps may establish ordering for EABC-side events, but cannot retroactively make an earlier observed effect occur after the commit.

**Expected verifier posture:** TEMPORAL_INTEGRITY_FAILURE unless an independently justified timestamp interpretation resolves the apparent divergence.

## 4. Critical evidence distinction

The v0.2 corpus contains an experimental `effect_correlation` object. Its presence is itself part of the synthetic fixture; it is **not proof that EABC has produced the corresponding integrity reference**.

Therefore:

- `action_digest` proves only what the EABC evidence model actually binds it to.
- `authorization_decision` proves only the recorded authorization decision.
- `commit_decision` proves only the recorded commit decision.
- `execution_outcome` proves only the recorded execution outcome.
- hash-chain integrity protects the evidence sequence.
- none of these, by themselves, establishes exact physical/downstream effect identity.

## 5. Current EABC-side result

**AUTHORITY/COMMIT OVERLAY:** READY  
**EXACT COMMIT → OBSERVED-EFFECT CORRELATION:** OPEN VALIDATION QUESTION  
**DOWNSTREAM RECONSTRUCTION:** PENDING ARGUS VERIFIER RUN

The bilateral result must be determined from the combined released evidence corpus, not from the expected verifier-result labels embedded in the synthetic fixtures.
