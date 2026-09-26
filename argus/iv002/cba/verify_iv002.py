#!/usr/bin/env python3
"""Minimal CBA verifier for ARGUS IV-002."""

import argparse
import hashlib
import json
from pathlib import Path


SHARED_EVENT_ID = "iv002-shared-001"


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def sha256_file(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--trace", required=True)
    p.add_argument("--eabc", required=True)
    p.add_argument("--trace-hash", required=True)
    p.add_argument("--eabc-hash", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()

    trace = load_json(args.trace)
    eabc = load_json(args.eabc)

    trace_hash = sha256_file(args.trace)
    eabc_hash = sha256_file(args.eabc)

    trace_integrity = trace_hash == args.trace_hash
    eabc_integrity = eabc_hash == args.eabc_hash

    call_id = trace["context"]["call_id"]
    command_id = eabc["command_id"]

    binding_match = (
        call_id == command_id
        and call_id == SHARED_EVENT_ID
        and command_id == SHARED_EVENT_ID
    )

    result = {
        "schema": "eabc-external-validation/iv002-cba-result/v0.1",
        "validation_id": "ARGUS-EABC-IV-002",
        "case_id": "E1",
        "shared_event_id": SHARED_EVENT_ID,
        "trace_artifact_hash": "sha256:" + trace_hash,
        "eabc_artifact_hash": "sha256:" + eabc_hash,
        "declared_trace_artifact_hash": "sha256:" + args.trace_hash,
        "declared_eabc_artifact_hash": "sha256:" + args.eabc_hash,
        "binding_rule": "call_id==command_id",
        "trace_integrity": "MATCH" if trace_integrity else "MISMATCH",
        "eabc_integrity": "MATCH" if eabc_integrity else "MISMATCH",
        "event_binding": "MATCH" if binding_match else "MISMATCH",
        "verification_result": (
            "PASS"
            if trace_integrity and eabc_integrity and binding_match
            else "FAIL"
        ),
    }

    Path(args.output).write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["verification_result"] == "PASS" else 1)


if __name__ == "__main__":
    main()
