# EABC External Validation

External validation artifacts for the Equinibrium Execution Authority Boundary Contract (EABC).

This repository is a **validation and audit layer**, not the normative EABC specification and not an implementation of EABC itself.

## Purpose

The repository provides a common place for independently scoped validation work that tests whether EABC execution-authority evidence can be correlated with downstream execution, observed effects, and reconstruction.

The validation chain is:

```
Exact Governed Action
        ↓
Authorization
        ↓
Commit
        ↓
Effect
        ↓
Observed State
        ↓
Evidence
        ↓
Independent Reconstruction
```

The central question is:

> Can an independent verifier establish, from released evidence alone, that a specific downstream effect corresponds to a specific action that was validly authorized and committed at the EABC execution-authority boundary?

## Repository boundary

### This repository contains

- external validation fixtures;
- validation mappings and overlays;
- evidence-correlation records;
- independent-verifier procedures;
- experimental validation results;
- references to external implementations and test runs.

### This repository does not contain

- the normative EABC specification;
- EABC core implementation code;
- private or proprietary implementations;
- a replacement for an external system being validated.

The normative EABC definition remains in the EABC repository.

## Validation status vocabulary

Validation artifacts use explicit classifications:

- **NORMATIVE** — defined by the applicable specification.
- **IMPLEMENTED** — implemented and directly evidenced by the referenced system.
- **EXPERIMENTAL** — exercised in a validation experiment but not yet established as a normative requirement.
- **GAP** — required for the validation claim but not currently established by the available evidence.

An independent verifier should report the narrowest conclusion supported by the released evidence.

In particular:

- **ALLOW ≠ EXECUTION**
- **EXECUTION ≠ EVIDENCE**
- **MISSING EVIDENCE ≠ EXECUTION FAILURE**
- **UNKNOWN / INCONCLUSIVE** is a valid verification result.

## Current validation lanes

### PAMIR ARGUS × EABC — IV-001

Bilateral validation with PAMILANGA Labs / ARGUS.

The initial lane tests whether EABC authority/commit evidence can be joined to downstream ARGUS reconstruction without introducing an unverified trust assumption at the boundary.

The IV-001 corpus is experimental. It is not a new normative EABC schema and does not modify the ARGUS baseline.

The current validation question includes:

```
Exact Governed Action
→ Authorization
→ Commit
→ Observed Effect
→ Reconstruction
```

### ComOS / HALOS — Run002

External execution-boundary validation using Ron Reynolds' ComOS federation work and the HALOS execution-boundary analysis.

The source implementation and original evidence remain in:

```
omwei-org/halos-1.3-atl-analysis
```

This repository should reference that material rather than duplicate or fork the underlying ComOS/HALOS tests.

## Relationship to other EABC repositories

| Repository | Role |
|---|---|
| `omwei-eabc` | Normative EABC specification, profiles, documentation and reference material |
| `halos-1.3-atl-analysis` | HALOS execution-boundary analysis and ComOS validation implementation |
| `eabc-execution-guard` | EABC execution guard for autonomous / Physical AI execution paths |
| `eabc-agentrust-interoperability` | AgenTrust / cMCP interoperability validation |
| `eabc-external-validation` | External validation, evidence correlation and independent-verifier artifacts |

## Evidence principle

A validation result should preserve the distinction between:

1. what was authorized;
2. what was committed;
3. what was actually executed;
4. what effect was observed;
5. what evidence proves the relationship between those events.

The repository therefore treats **commit-to-effect correlation** as an explicit validation boundary rather than assuming that an execution outcome automatically proves the observed effect.

## Scope and non-claims

Artifacts in this repository are scoped to their stated validation experiment.

Unless an artifact explicitly establishes otherwise, publication here does **not** claim:

- production interoperability;
- general EABC conformance;
- security certification;
- regulatory approval;
- formal verification of an implementation;
- resistance to all classes of execution-path compromise.

Each validation lane must state its own evidence basis, limitations, and unresolved gaps.

## License

Unless a subdirectory states otherwise, repository code and validation tooling are licensed under Apache License 2.0.

Specification text or externally originated material may retain its own stated license.

