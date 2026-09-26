#!/usr/bin/env python3
"""Deterministically generate the IV-002 controlled EABC artifact."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "argus" / "iv002" / "eabc" / "iv002_eabc_artifact.json"

SHARED_EVENT_ID = "iv002-shared-001"
ACTION = {
    "agent_id": "did:web:agent.example:cell-a:planner-1",
    "action_type": "material.move",
    "action_scope": "cell-a.material.move",
    "action_timestamp": "2026-09-26T06:00:00Z",
}
PAYLOAD = {
    "action": "material.move",
    "material": "MAT-001",
    "from": "buffer-a",
    "to": "station-1",
    "target": "did:web:factory.example:cell-a:material-station-1",
}

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha256(value):
    return "sha256:" + hashlib.sha256(canonical(value).encode()).hexdigest()

def build():
    action_ref = sha256(ACTION)
    payload_digest = sha256(PAYLOAD)
    return {
        "schema": "eabc-external-validation/iv002-eabc-artifact/v0.1",
        "validation_id": "ARGUS-EABC-IV-002",
        "case_id": "E1",
        "claim_status": "EXPERIMENTAL",
        "shared_event_id": SHARED_EVENT_ID,
        "command_id": SHARED_EVENT_ID,
        "action": {**ACTION, "action_ref": action_ref},
        "governed_action": {"payload": PAYLOAD, "payload_digest": payload_digest},
        "authorization": {"decision": "ALLOW", "policy": "iv002-controlled-policy-v0.1"},
        "execution_authority": {"authority_state": "VALID", "epoch": 1, "scope": "cell-a.material.move"},
        "commit": {
            "commit_id": "commit-iv002-shared-001",
            "status": "COMMITTED",
            "command_id": SHARED_EVENT_ID,
            "governed_action_digest": payload_digest,
        },
        "effect": {
            "effect_correlation": SHARED_EVENT_ID,
            "status": "APPLIED",
            "observed_at": "2026-09-26T06:00:02Z",
        },
        "evidence": {"commit_observed": True, "effect_observed": True},
        "method_note": "Controlled validation fixture; not a production EABC runtime trace and not a cryptographically signed TRACE Trust Record.",
    }

if __name__ == "__main__":
    artifact = build()
    OUT.write_text(json.dumps(artifact, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(OUT)
    print("canonical_sha256:", hashlib.sha256(canonical(artifact).encode()).hexdigest())
