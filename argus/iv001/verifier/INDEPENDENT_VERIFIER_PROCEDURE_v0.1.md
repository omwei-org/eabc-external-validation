# IV-001 Independent Verifier Procedure v0.1

## Purpose

Determine the strongest conclusion that can be established from the released IV-001 evidence corpus without relying on undocumented trust assumptions.

## Inputs

The verifier operates only on:

1. the released transaction fixtures;
2. the EABC authority/commit evidence overlay;
3. the released evidence manifest;
4. the stated integrity references;
5. the downstream reconstruction inputs.

The verifier must not use unpublished implementation state to upgrade a result.

## Verification sequence

### 1. Identify the governed action

Confirm that the transaction has an unambiguous lifecycle identifier and that the exact governed action/payload can be identified.

### 2. Verify authorization

Confirm:

- authorization decision;
- applicable authority state / epoch;
- authorization reason;
- correlation to the governed action.

### 3. Verify commit

Confirm:

- final authority check;
- commit decision;
- commit reason;
- correlation to the same governed action;
- execution epoch / authority epoch as applicable.

### 4. Verify execution

Determine whether an execution outcome is actually recorded.

Do not infer execution merely from an ALLOW decision.

### 5. Verify evidence integrity

Verify the released evidence sequence and its declared integrity references.

For hash-chained records, verify each record against its predecessor and the declared genesis condition.

### 6. Verify observed effect

Determine whether an independently identifiable downstream effect was observed.

The verifier should establish the effect source and observation time where supplied.

### 7. Verify exact effect correlation

Test whether the evidence establishes:

```
Exact Governed Action
→ Authorization
→ Commit
→ Observed Effect
```

A matching lifecycle identifier alone is not sufficient if the actual effect identity remains ambiguous.

### 8. Verify temporal consistency

Check that the relevant events occur in an order compatible with the claimed transaction:

```
Authorization
→ Commit
→ Effect Observation
```

Temporal divergence must be reported rather than repaired by interpretation.

## Decision vocabulary

Use the narrowest supported result:

- **VALIDATED FOR TESTED TRANSACTION** — the released corpus establishes the requested relationship for the tested case.
- **PARTIAL / CONSTRAINED** — some links are established, but one or more required relationships remain bounded or experimentally supported.
- **UNRESOLVED SEMANTIC GAP** — the corpus cannot establish the requested relationship without an additional assumption or artifact.
- **INCONCLUSIVE** — evidence is insufficient to distinguish the relevant alternatives.

## Mandatory distinctions

```
ALLOW ≠ EXECUTION
EXECUTION ≠ EVIDENCE
EVIDENCE INTEGRITY ≠ EFFECT INTEGRITY
EFFECT OBSERVATION ≠ EXACT EFFECT CORRELATION
MISSING EVIDENCE ≠ EXECUTION FAILURE
```

## Reproducibility

A second verifier must be able to repeat the decision from the same released corpus and obtain the same conclusion.

If the second verifier reaches a different conclusion, the discrepancy itself becomes a validation finding and must identify the differing evidence interpretation or missing binding.

## Non-claims

This procedure does not establish:

- production interoperability;
- general EABC conformance;
- security certification;
- regulatory approval;
- physical-world safety;
- resistance to compromise outside the tested execution path.
