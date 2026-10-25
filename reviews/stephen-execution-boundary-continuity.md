# Stephen's Execution-Boundary Continuity Question — Validation Audit

**Status:** AUDIT / PROPOSED VALIDATION PLAN  
**Scope:** EABC External Validation, especially PAMIR ARGUS × EABC IV-001  
**Normative effect:** None. This document does not change the normative EABC contract or claim that the proposed cases have passed.

## 1. Question under review

Stephen asks what independently establishes that the authority and evidence being evaluated still represent the conditions governing the actual consequence, and whether continuity between evidence, decision, and effect is demonstrated under changing conditions and failure.

This is two related but distinct claims:

1. **Evidentiary continuity:** an independent verifier can bind the exact governed action, authorization, commit, observed downstream effect, and reconstruction using released evidence.
2. **Preventive continuity:** if governing conditions change or authority becomes invalid before an effect can occur, the execution path rejects or inhibits that effect.

External validation can establish or falsify the first claim. It can test the second only when the execution system and its actual effect-control boundary are part of the experiment. Correlation after the fact is not itself a physical interlock.

## 2. What the current IV-001 record establishes

The current `argus/iv001/README.md` records the following EABC-side status:

| Element | Recorded status |
|---|---|
| Exact Governed Action | ESTABLISHED |
| Authorization | ESTABLISHED |
| Commit | ESTABLISHED |
| Execution Outcome | ESTABLISHED |
| Evidence Integrity | ESTABLISHED |
| Observed Effect | AVAILABLE EXPERIMENTALLY |
| Exact Effect Correlation | NOT YET ESTABLISHED |
| Downstream Reconstruction | PENDING ARGUS RUN |

The fixture README describes the expected case set as nominal transaction, authorization failure, execution failure, evidence failure, exact-effect correlation mismatch, and temporal divergence. It also says the received ARGUS corpus and its hashes must be recorded when the source package is available.

**Audit conclusion:** the repository already names the correct commit-to-effect evidence boundary. The current IV-001 record does *not* establish exact effect correlation or completed independent reconstruction. The fixture README describes expected coverage; that is not evidence that the cases have run or passed. The available records do not yet establish preventive behavior when conditions change at the execution boundary.

## 3. Proposed adversarial validation matrix

These are proposed cases, not reported test results. Bind each case to a concrete fixture, raw output, verifier result, and artifact digest before classifying it as IMPLEMENTED or EXPERIMENTAL.

| ID | Perturbation | Required verifier / system observation | Expected classification if evidence is insufficient |
|---|---|---|---|
| C01 — stale authority | Authorization is valid at issuance but expires or is revoked before commit | Commit must be rejected by an enforcing implementation; evidence must show the authority version and validation point | GAP if the implementation's enforcement or trace cannot be demonstrated |
| C02 — state changes before effect | Relevant governing state changes after commit but before downstream effect | Establish whether the contract requires revalidation at that boundary; if required, effect is inhibited or explicitly marked as outside the guarantee | GAP if the design has no defined effect-boundary rule |
| C03 — action substitution | Commit evidence for action A is paired with observed effect B | Independent verifier rejects the binding; matching timestamps alone must not suffice | UNKNOWN / INCONCLUSIVE when identifiers or evidence are missing |
| C04 — replay / duplicate | Old authorization, commit evidence, or effect record is replayed | Replay is detected through action-bound identifiers, freshness / sequence constraints, and idempotency rules where applicable | GAP if replay cannot be distinguished from a fresh event |
| C05 — concurrent mutation | Governing state changes concurrently with authorization or commit | Record the ordering/linearization point and show which state governed the decision | GAP if the trace cannot establish ordering |
| C06 — partial failure | Failure occurs between commit, downstream execution, effect, observation, and evidence release | Distinguish committed-but-not-executed, executed-but-unobserved, and observed-but-unproven outcomes; do not infer one from another | UNKNOWN / INCONCLUSIVE where the evidence cannot distinguish them |
| C07 — missing or corrupted evidence | A required event is absent, truncated, or fails integrity verification | Verifier reports inconclusive or evidence failure, not an invented execution success/failure | UNKNOWN / INCONCLUSIVE or evidence failure, as defined by the verifier |
| C08 — bypass path | A downstream effect can occur without passing through the claimed guard/interlock | Demonstrate the bypass in a controlled test and identify the guarantee boundary | GAP for any claim that assumes all effects traverse the guard |
| C09 — observed-state mismatch | Reported observed state disagrees with the effect record or trusted measurement | Verifier identifies the mismatch and preserves raw observations and provenance | UNKNOWN / INCONCLUSIVE until resolved |
| C10 — recovery / retry | Crash or retry occurs around commit/effect and recovery replays work | Demonstrate deduplication or explicitly document possible repeated effects; reconstruct the final state | GAP if retries can create an untracked or ambiguous effect |

### Acceptance discipline

- A case is **IMPLEMENTED** only when the referenced system behavior and its evidence are directly available.
- A case is **EXPERIMENTAL** only after the experiment has actually run and the run artifacts are linked.
- A case is **GAP** when it is necessary for the stated claim but not established by the available evidence.
- Use **UNKNOWN / INCONCLUSIVE** for an individual run whose evidence cannot support a conclusion. Do not convert missing evidence into proof of either execution or non-execution.
- Preserve source fixtures as received. Record source release/version, hashes, test command, run identifier, raw output, and verifier output.

## 4. Evidence envelope needed for independent correlation

For each governed action and downstream effect, the experiment should expose or map, where the source system supports them:

- stable action / transaction identifier;
- authorization reference and authority version;
- relevant conditions or state version at authorization and commit;
- commit identifier and commit time / ordering evidence;
- downstream execution identifier;
- effect identifier and target/resource identity;
- observed-state source, observation time, provenance, and integrity digest;
- links among the records, including explicit missing-link handling;
- verifier version, input manifest, decision, reason code, and reproducible run reference.

Timestamps alone are not a safe join key. If a source system lacks a stable identifier or trustworthy ordering evidence, record that as a limitation rather than synthesizing a stronger guarantee.

## 5. Enforcement boundary and non-claim

Evidence correlation can demonstrate whether the available record supports the claimed relationship. It does not, by itself, prevent a stale or invalid action from taking effect.

A preventive claim requires evidence from the actual enforcement point: for example, a guard that revalidates the relevant authority/state at the required boundary, or an independent effect-boundary interlock. The exact mechanism depends on the system and must not be assumed from the presence of an audit trail.

For a physical or otherwise irreversible consequence, the validation must identify the last controllable boundary and the measurement that establishes the effect. A software-level commit must not be described as proof that the physical effect occurred or was prevented.

## 6. Next steps

1. Obtain and preserve the actual IV-001 source corpus and manifest; record hashes and release identity.
2. Complete the pending ARGUS run and independent reconstruction, including the exact-effect mismatch and temporal-divergence cases.
3. Link the original HALOS / ComOS Run002 implementation and raw results from `omwei-org/halos-1.3-atl-analysis`; do not duplicate its tests here.
4. Determine whether the referenced execution-guard implementation has tests for C01, C02, C04, C05, and C08. Cite the exact test and run output rather than infer coverage from repository descriptions.
5. Publish a case-by-case status table with evidence links and limitations. Keep unresolved preventive claims explicitly marked GAP.

## 7. Current answer to Stephen

EABC External Validation already treats commit-to-effect correlation and independent reconstruction as an explicit validation boundary. The IV-001 status currently available, however, leaves exact effect correlation unestablished and downstream reconstruction pending. It therefore identifies the right question but does not yet demonstrate a complete answer.

The next proof must show both (a) whether independent evidence binds the exact committed action to the observed effect and (b), where a prevention guarantee is claimed, whether the actual enforcement boundary rejects or inhibits the effect when governing conditions change. These are separate claims and should receive separate test results.


## 8. Follow-up source inspection: Execution Guard

The public default-branch source in `omwei-org/eabc-execution-guard` adds a more precise result than the README alone:

- `tests/test_guard.py::test_stale_epoch` asserts that an object prepared before revocation is blocked with `STALE_EPOCH` and no permit.
- `tests/test_guard.py::test_revoked_authority` asserts that inactive authority is blocked with `REVOKED`.
- `tests/test_guard.py::test_reauthorization_does_not_revive_old_object` asserts that revocation followed by reauthorization does not revive an old prepared object.
- `tests/test_guard.py::test_payload_mutation_is_blocked` asserts that payload substitution is blocked with `INVALID_BINDING`.
- `tests/test_guard.py::test_effect_commit_is_serialized_against_revocation` uses two threads and a synchronous callback to assert that revocation waits while the effect callback holds the authority lock, then observes authority as inactive.

The implementation in `eabc_guard/authority.py::Authority.commit_if_current` holds the authority lock, checks that authority is active and the epoch matches, and runs the callback before releasing the lock. The code comments explicitly limit this guarantee to synchronous in-process callbacks: the callback must cross the effect boundary synchronously and must not enqueue work that can execute after it returns. The implementation explicitly does not claim hardware or cross-process enforcement.

### Revised case-level assessment

| Case | Source-level evidence found | Assessment |
|---|---|---|
| C01 — stale / revoked authority before commit | Named tests assert stale-epoch and revoked-authority blocking | IMPLEMENTED IN REFERENCE TESTS; runtime CI status not verified in this audit |
| C03 — payload/action substitution | Named test asserts changed payload binding is blocked | IMPLEMENTED IN REFERENCE TESTS for payload bytes; not proof of downstream effect identity |
| C05 — concurrent revocation vs synchronous effect callback | Named threaded test asserts callback/revocation serialization | IMPLEMENTED IN REFERENCE TESTS for this in-process synchronization case |
| C02 — relevant world/state changes after commit but before an asynchronous or external effect | No evidence found in the inspected guard source that the guard controls a separately queued or external effect after the callback returns | GAP for any broader guarantee beyond the synchronous callback boundary |
| C04 — replay / duplicate execution opportunity | The inspected `test_guard.py` does not establish single-use sequence/replay prevention | NOT ESTABLISHED by the inspected test file; inspect other implementation paths before making a repository-wide claim |
| C06 — partial failure and recovery | The inspected source/test does not establish crash recovery or reconciliation across commit, external effect, and evidence release | NOT ESTABLISHED by the inspected test file |
| C08 — bypass path / hardware isolation | README and source comments disclaim process-level, cross-process, and hardware enforcement | OUT OF SCOPE for this software reference implementation; must be tested at deployment boundary |

These statuses describe what the inspected source asserts, not a fresh test execution. The GitHub combined status query for the audit commit returned no status entries; this is not equivalent to a passing CI run. Repository search did not return indexed matches for the requested HALOS/ComOS Run002 details, so this audit does not claim that those artifacts were independently inspected.

## 9. Updated answer to Stephen

The execution guard's reference implementation does contain a meaningful preventive mechanism: it binds the payload to an authority epoch, blocks stale/revoked authority, and serializes a synchronous in-process effect callback against revocation. Its own contract is narrower than a general claim of continuity to any real-world consequence.

That mechanism does not alone establish that an asynchronous device command, remote service, physical actuator, or bypass path remains governed after the callback returns. Nor does it supply the missing IV-001 evidence binding the exact commit to the observed downstream effect. The external validation and the execution guard therefore address complementary parts of Stephen's question; the end-to-end claim remains unproven until the ARGUS reconstruction and the actual effect-boundary behavior are evidenced.
