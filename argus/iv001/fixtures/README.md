# IV-001 Fixtures

This directory is reserved for the concrete validation fixtures supplied by the PAMIR ARGUS side.

The fixtures must be preserved **as received** for the validation run. Do not normalize, rewrite, or silently repair them.

Expected source package:

- `iv001_evidence_corpus.json`
- `iv001_manifest.csv`
- any accompanying fixture files required by the independent-verifier procedure

The validation corpus is experimental and must not be treated as a normative EABC schema.

## Case set

The IV-001 package is expected to exercise:

- nominal transaction;
- authorization failure;
- execution failure;
- evidence failure;
- exact-effect correlation mismatch;
- temporal divergence.

Once the source package is available, record its release identifier and hashes in the validation manifest.
