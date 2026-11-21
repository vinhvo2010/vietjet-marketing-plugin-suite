"""Regression tests: no provider call, no automatic authority, no secret disclosure."""
import hashlib
import json
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))
from readiness import audit_connectors, audit_evidence, audit_release, main

NOW = datetime(2026, 11, 21, 0, 0, tzinfo=timezone.utc)


def evidence(label="VERIFIED", expires=None):
    return {
        "mission_id": "mission-123",
        "entries": [{
            "claim_id": "claim-1", "claim_type": "OBSERVED",
            "claim": "Synthetic aggregate result", "data_label": label,
            "source_ref": "approved-mock-source", "owner": "Test Owner",
            "checked_at": (NOW - timedelta(days=1)).isoformat(),
            "expires_at": (expires or NOW + timedelta(days=1)).isoformat(),
        }],
    }


def packet(data: bytes):
    return {
        "mission_id": "mission-123", "artifact_id": "draft-1",
        "artifact_hash": hashlib.sha256(data).hexdigest(),
        "target": "Internal review only", "release_owner": "Human Owner",
        "rollback_plan": "Withdraw the draft", "approval_evidence": ["approval-ref-to-verify"],
        "claims": [{"claim": "Synthetic aggregate result", "evidence_id": "claim-1"}],
        "status": "APPROVED_FOR_NAMED_TARGET",
    }


class ReadinessTests(unittest.TestCase):
    def test_fresh_verified_evidence_reviewable_not_truth_certified(self):
        result = audit_evidence(evidence(), NOW)
        self.assertEqual(result["status"], "EVIDENCE_REVIEWABLE")
        self.assertEqual(result["fresh_verified_ids"], ["claim-1"])
        self.assertFalse(result["truth_verified_by_runtime"])

    def test_unverified_claim_never_passes_verified_reference(self):
        result = audit_evidence(evidence("ILLUSTRATIVE"), NOW)
        self.assertEqual(result["fresh_verified_ids"], [])
        self.assertIn("claim-1", result["nonverified_ids"])

    def test_stale_evidence_blocks(self):
        result = audit_evidence(evidence(expires=NOW - timedelta(hours=1)), NOW)
        self.assertEqual(result["status"], "BLOCKED_INPUT")
        self.assertTrue(any("expired" in s for s in result["issues"]))

    def test_missing_expiry_blocks_verified_claim(self):
        x = evidence()
        del x["entries"][0]["expires_at"]
        self.assertEqual(audit_evidence(x, NOW)["status"], "BLOCKED_INPUT")

    def test_future_checked_at_blocks(self):
        x = evidence()
        x["entries"][0]["checked_at"] = (NOW + timedelta(days=1)).isoformat()
        self.assertEqual(audit_evidence(x, NOW)["status"], "BLOCKED_INPUT")

    def test_naive_timestamp_blocks(self):
        x = evidence()
        x["entries"][0]["checked_at"] = "2026-11-20T00:00:00"
        self.assertEqual(audit_evidence(x, NOW)["status"], "BLOCKED_INPUT")

    def test_duplicate_claim_ids_block(self):
        x = evidence()
        x["entries"].append(dict(x["entries"][0]))
        self.assertEqual(audit_evidence(x, NOW)["status"], "BLOCKED_INPUT")

    def test_release_matching_artifact_is_still_human_only(self):
        data = b"synthetic local artifact"
        result = audit_release(packet(data), evidence(), data, NOW)
        self.assertEqual(result["status"], "READY_FOR_HUMAN_REVIEW")
        self.assertFalse(result["release_authorized"])
        self.assertEqual(result["execution_authority"], "NONE_NO_AUTOMATIC_EXTERNAL_ACTIONS")

    def test_release_modified_artifact_blocks(self):
        data = b"original"
        result = audit_release(packet(data), evidence(), data + b" tampered", NOW)
        self.assertEqual(result["status"], "BLOCKED_INPUT")

    def test_release_unverified_reference_blocks(self):
        data = b"original"
        result = audit_release(packet(data), evidence("NEEDS_VERIFICATION"), data, NOW)
        self.assertEqual(result["status"], "BLOCKED_INPUT")

    def test_release_wrong_mission_blocks(self):
        data = b"original"
        x = packet(data)
        x["mission_id"] = "wrong"
        self.assertEqual(audit_release(x, evidence(), data, NOW)["status"], "BLOCKED_INPUT")

    def test_release_missing_approval_blocks(self):
        data = b"original"
        x = packet(data)
        x["approval_evidence"] = []
        self.assertEqual(audit_release(x, evidence(), data, NOW)["status"], "BLOCKED_APPROVAL")

    def test_connector_status_hides_secret_values(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "plugins"
            folder.mkdir()
            (folder / "test.json").write_text(json.dumps({
                "name": "commerce", "type": "connector",
                "env": ["VJAI_COMMERCE_ENDPOINT", "VJAI_COMMERCE_READ_TOKEN"],
            }))
            result = audit_connectors(Path(tmp), {
                "VJAI_COMMERCE_ENDPOINT": "https://example.invalid",
                "VJAI_COMMERCE_READ_TOKEN": "TOP-SECRET-MOCK",
            })
            self.assertEqual(result["connectors"][0]["status"], "CONFIGURED_UNVERIFIED")
            self.assertNotIn("TOP-SECRET-MOCK", json.dumps(result))
            self.assertFalse(result["live_access_verified"])

    def test_missing_connector_env_is_not_connected(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "plugins"
            folder.mkdir()
            (folder / "x.json").write_text(json.dumps({
                "name": "test", "type": "connector", "env": ["MISSING_TOKEN"]
            }))
            result = audit_connectors(Path(tmp), {})
            self.assertEqual(result["connectors"][0]["status"], "MISSING_CONFIGURATION")
            self.assertEqual(result["connectors"][0]["missing_env_names"], ["MISSING_TOKEN"])

    def test_cli_fails_closed_on_missing_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(main(["evidence", str(Path(tmp) / "absent.json")]), 2)


if __name__ == "__main__":
    unittest.main()
