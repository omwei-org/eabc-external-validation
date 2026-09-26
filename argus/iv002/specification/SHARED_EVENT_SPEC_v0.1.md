# IV-002 Shared Event Specification v0.1

## 1. Purpose

Define the smallest shared event contract needed to test cross-source evidence correlation between TRACE-shaped action evidence and EABC execution-authority evidence without changing either system's normative semantics.

## 2. Controlled event identity

The experiment pre-agrees the literal value:

`shared_event_id = iv002-shared-001`

The identifier is not derived from either evidence system. Each side independently records it in its own artifact.

TRACE side:
- `call_id = iv002-shared-001`

EABC side:
- `command_id = iv002-shared-001`

Binding rule:

`TRACE.call_id == EABC.command_id`

## 3. Action identity

The controlled action is:
- agent: `did:web:agent.example:cell-a:planner-1`
- action type: `material.move`
- action scope: `cell-a.material.move`
- timestamp: `2026-09-26T06:00:00Z`

`action_ref` is SHA-256 over the canonical JSON representation of exactly those four fields, using lexicographic key ordering and compact JSON serialization for this fixture.

Result:
`sha256:76a6810296c2ad284a189b9554a71b6080d20d47bdf6e4e6c7882f4b265c5165`

## 4. Governed payload

The controlled payload is:

{"action":"material.move","from":"buffer-a","material":"MAT-001","target":"did:web:factory.example:cell-a:material-station-1","to":"station-1"}

Its independently computed SHA-256 is:
`sha256:4b2f794eb15342940c5ffef9dba480383587ef2cb49b8e39f021f63099a52b2c`

## 5. Evidence binding

The verifier checks independently:
1. TRACE `call_id` equals EABC `command_id`.
2. The EABC action reference recomputes to the declared `action_ref`.
3. The EABC payload digest recomputes to the declared governed-action digest.
4. Event timestamps satisfy the declared controlled temporal window.
5. Any CBA is treated as a statement to verify, not as an authority for correlation.

The CBA therefore does not establish correlation by assertion; it records the result of checks performed against both source artifacts.

## 6. Cases

### E1 — nominal correlation
Both artifacts independently contain `iv002-shared-001`, and action/payload digests are consistent.
Expected: `CORRELATED`.

### E2 — execution divergence
Both artifacts contain the same shared event identifier, but the EABC governed action is transformed after the authority gate.
Expected: `CORRELATED + EXECUTION_DIVERGENCE`.

The shared event identity establishes that the evidence refers to the same controlled event; the digest mismatch establishes that the committed execution diverged from the originally evidenced action.

### E3 — unresolved binding
The TRACE artifact has no matching `call_id`, or records a different event identifier.
Expected: `UNRESOLVED`.

## 7. Anti-circularity rule

No verifier may accept correlation solely because a CBA, report, or human annotation asserts that two artifacts belong together. Correlation must be reproducible from fields independently present in the source artifacts.

## 8. Claim boundary

This specification defines an experimental validation fixture only. It does not alter TRACE, AgenTrust, EABC, or any external system's normative semantics.

A passing IV-002 result means only that the released controlled artifacts satisfy the stated cross-source binding checks.
