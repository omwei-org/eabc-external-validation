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


## 10. Cross-repository evidence: Factory Execution Authority MVP

Inspection of `omwei-org/factory-ea-mvp` changes the case assessment: it contains a more developed protected-commit prototype than the standalone `eabc-execution-guard` tests inspected above. The relevant integration is in draft PR [#9](https://github.com/omwei-org/factory-ea-mvp/pull/9), head SHA `0820c2f5a5c4b554cba81d97c91b19f702bc8fd1`, targeting draft PR #5 rather than `main`. It is not merged.

### Evidence actually present

- `ProtectedCommitGate` verifies the signed factory authorization and current protected governance/revocation state, reserves a sequence, and calls the configured capability while holding the governance lock.
- The stacked EGA integration requires a signed EGA envelope, an independently configured EGA trust store and scope policy, and binds the authority to the DecisionRecord digest and AEE evidence snapshot before the factory commit authorization is accepted.
- The OPC UA public method accepts a server-issued opaque `authority_ref`; it resolves server-side to the request and routes through the protected gate rather than accepting caller-supplied payload, principal, trust store, or raw factory authorization.
- `CommitEvidenceLog` appends a `PREPARED` record and fsyncs it before invoking the effect capability, then appends `COMMIT` or `OUTCOME_UNKNOWN`. On startup it verifies the local hash chain and reconstructs commit sequence / replay high-water marks. A PREPARED-only record consumes the sequence conservatively.
- Tests in `tests/test_opcua_atomicity.py`, `tests/test_protected_commit.py`, and `tests/test_commit_evidence.py` cover the integrated public route, synchronous revocation/commit serialization, exact payload binding, rejected requests, replay after restart, failed pre-effect evidence write, and outcome ambiguity for async effects.

### CI evidence at the inspected integration head

For the exact SHA `0820c2f5a5c4b554cba81d97c91b19f702bc8fd1`, GitHub Actions reports all three workflows succeeded on 2026-10-20:

- [Python Tests #109](https://github.com/omwei-org/factory-ea-mvp/actions/runs/39488286309) — success
- [L2 Process Isolation #156](https://github.com/omwei-org/factory-ea-mvp/actions/runs/39488286322) — success
- [WASM Conformance #163](https://github.com/omwei-org/factory-ea-mvp/actions/runs/39488286284) — success

These are commit-specific software CI results. They do not establish a physical actuator test or a hardware non-bypassability claim.

### Gaps explicitly recorded by the project itself

The integration's `docs/SW_IMPERFECTIONS.md` is an important gap register, not a blanket claim of closure:

| Stephen-related concern | Factory EA MVP finding |
|---|---|
| Authority changes before synchronous effect | Closed in software for the synchronous gate effect, with an integrated OPC UA race test |
| Replay / duplicate authorization | Replay is guarded in-process and reconstructed from the local evidence log after restart; tests cover restart replay prevention |
| Evidence-write failure before effect | Fail-closed: if PREPARED cannot be persisted, the effect is not attempted |
| Crash after effect but before terminal evidence | Outcome is fundamentally ambiguous; PREPARED remains, sequence is consumed, and the system must not claim confirmed success or safe retry |
| Asynchronous/remote effect | Returns `OUTCOME_UNKNOWN`; downstream-owned commit point and response/idempotency protocol remain necessary |
| OPC UA caller identity | OPEN: `authority_ref` is a bearer reference, not binding to an authenticated session principal; anonymous-client test is strict-xfail |
| Direct capability / actuator bypass | OPEN: another reference in the same process can call the capability directly; OPC UA-route tests do not prove the absence of alternate paths |
| DownstreamCommitGate integration | OPEN / NOT INTEGRATED: the separate downstream gate is not on the current OPC UA route |
| Audit integrity against host administrator | OPEN: local hash chain detects tampering but a host actor able to rewrite the file can recompute the chain |
| Physical non-bypassability | Not established; requires the L4 effect topology and hardware evidence |

One additional source limitation matters for temporal continuity: the EGA adapter binds the epoch and sequence values supplied by its factory caller. The signature proves what was signed; it does not independently prove that those values were sourced from the current protected governance authority. The commit gate checks its protected current epoch, but provenance of upstream values and deployment trust boundaries must not be conflated.

### Revised case-level assessment after inspecting Factory EA MVP

| Case | Revised assessment |
|---|---|
| C01 — stale / revoked authority before synchronous commit | IMPLEMENTED IN SOFTWARE; CI passed at the exact PR #9 head |
| C03 — payload/action substitution | IMPLEMENTED IN SOFTWARE for signed payload binding; downstream physical effect identity still requires independent evidence |
| C04 — replay / duplicate | IMPLEMENTED IN SOFTWARE for sequence guard and local-log restart recovery at the tested head; local log is not tamper-proof against a privileged host |
| C05 — concurrent governance transition vs synchronous commit | IMPLEMENTED IN SOFTWARE; integrated OPC UA race test and CI passed |
| C06 — partial failure | PARTIALLY HANDLED: durable PREPARED marker and OUTCOME_UNKNOWN avoid false certainty, but cannot reconstruct whether a physical effect occurred after a crash in the critical window |
| C07 — evidence integrity | PARTIALLY HANDLED: hash-chain verification and fsync exist; no independent witness or host-resistant append-only storage |
| C08 — bypass path / hardware isolation | GAP / NOT ESTABLISHED; explicitly acknowledged by the repository |
| C02 — state changes after dispatch to an async/remote actuator | GAP for end-to-end prevention; software returns OUTCOME_UNKNOWN rather than claiming effect-boundary atomicity |
| Independent observed-effect correlation (IV-001) | STILL NOT ESTABLISHED by the reviewed Factory EA artifacts; local commit evidence describes the software gate/effect callback, not an independent downstream observation and reconstruction |

## 11. Updated answer to Stephen

The Factory EA MVP demonstrates more than a simple epoch check. At its inspected draft PR #9 head, it combines signed EGA authority, explicit scope policy, protected commit-time governance checks, sequence replay protection, an OPC UA route through a protected gate, and a durable local PREPARED/COMMIT/OUTCOME_UNKNOWN evidence log. All three CI workflows passed for that exact head.

That is meaningful software-level evidence for continuity up to a synchronous configured effect capability. It is not yet proof of end-to-end continuity to an arbitrary external or physical consequence. The project explicitly leaves open caller identity binding, in-process effect bypass, downstream-gate integration, host-resistant evidence storage, and hardware non-bypassability. For a crash after a possible physical effect but before terminal evidence, it correctly retains uncertainty instead of claiming either success or safe retry.

Therefore the accurate conclusion is: **the synchronous software commit boundary and replay/evidence handling are substantially implemented and CI-tested in the draft Factory EA integration; independent downstream effect reconstruction and the real deployment effect boundary remain unproven.** IV-001 should use this MVP as a candidate implementation under test, pin the exact PR/head SHA, exercise its public path, and separately capture the downstream observed effect and reconstruction. It must not treat the existence of local `COMMIT` evidence as a substitute for independent effect evidence.
