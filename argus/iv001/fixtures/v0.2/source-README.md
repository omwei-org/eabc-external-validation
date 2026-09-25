# PAMIR ARGUS × EABC — IV-001 Fixture Bundle v0.2

Concrete serialized fixtures for the EABC-side overlay.

Critical seam:
`Exact Governed Action → Authorization → Commit → Exact Effect Correlation → Observed Effect → Downstream Reconstruction`

The `effect_correlation` object is an EXPERIMENTAL IV-001 validation artifact matching the EABC overlay's proposed correlation requirement. It is not a new normative EABC field set and is not asserted to be a canonical ARGUS schema.

EABC should resolve `TO_BE_SUPPLIED_BY_EABC_OVERLAY` only with evidence actually supported by the implementation. If exact commit → observed-effect binding cannot be established, retain `GAP` / `INCONCLUSIVE`.

Cases: A Nominal; B Authorization failure; C Execution failure; D Evidence failure; E Correlation mismatch; F Temporal divergence.
