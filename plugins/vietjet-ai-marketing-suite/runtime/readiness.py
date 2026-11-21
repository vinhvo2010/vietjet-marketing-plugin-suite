#!/usr/bin/env python3
"""Offline, fail-closed readiness checks for Vietjet AI Marketing Suite.

This module never contacts a provider, validates an approval identity or
authorizes publication, spending, pricing, customer-data processing or flight
operations. It inspects local declarations and evidence only.
"""
from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LABELS = {"VERIFIED", "ILLUSTRATIVE", "NEEDS_VERIFICATION"}
CLAIM_TYPES = {"OBSERVED", "INFERENCE", "PROPOSAL"}
EMPTY_REFERENCES = {"", "tbd", "todo", "none", "unknown", "n/a", "placeholder"}
NO_AUTHORITY = "NONE_NO_AUTOMATIC_EXTERNAL_ACTIONS"


def _stamp(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed.astimezone(timezone.utc) if parsed.tzinfo else None


def audit_evidence(ledger: Any, now: datetime | None = None) -> dict[str, Any]:
    """Check traceability and freshness; never certify a source as truthful."""
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        raise ValueError("now must have timezone information")
    issues: list[str] = []
    verified: list[str] = []
    seen: set[str] = set()
    entries = ledger.get("entries") if isinstance(ledger, dict) else None
    mission = ledger.get("mission_id") if isinstance(ledger, dict) else None
    if not isinstance(mission, str) or len(mission.strip()) < 3:
        issues.append("mission_id: missing or invalid")
    if not isinstance(entries, list):
        entries = []
        issues.append("entries: expected an array")
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            issues.append(f"entry[{index}]: expected an object")
            continue
        ident = entry.get("claim_id")
        if not isinstance(ident, str) or not ident.strip():
            issues.append(f"entry[{index}]: claim_id is missing")
            continue
        if ident in seen:
            issues.append(f"{ident}: duplicate claim_id")
            continue
        seen.add(ident)
        label, kind = entry.get("data_label"), entry.get("claim_type")
        if label not in LABELS or kind not in CLAIM_TYPES:
            issues.append(f"{ident}: invalid data_label or claim_type")
            continue
        if not isinstance(entry.get("claim"), str) or not entry["claim"].strip():
            issues.append(f"{ident}: missing claim")
        if label != "VERIFIED":
            continue
        if not isinstance(entry.get("owner"), str) or not entry["owner"].strip():
            issues.append(f"{ident}: verified claim has no accountable source owner")
            continue
        source = entry.get("source_ref")
        if not isinstance(source, str) or source.strip().lower() in EMPTY_REFERENCES:
            issues.append(f"{ident}: verified claim has no specific source reference")
            continue
        checked = _stamp(entry.get("checked_at"))
        expires = _stamp(entry.get("expires_at"))
        if checked is None or expires is None:
            issues.append(f"{ident}: verified claim requires timezone-aware checked_at and expires_at")
        elif checked > now + timedelta(minutes=5):
            issues.append(f"{ident}: checked_at is in the future")
        elif expires <= now or expires <= checked:
            issues.append(f"{ident}: source expired or invalid expiry window")
        else:
            verified.append(ident)
    return {
        "status": "BLOCKED_INPUT" if issues else "EVIDENCE_REVIEWABLE",
        "mission_id": mission if isinstance(mission, str) else None,
        "total_claims": len(entries),
        "fresh_verified_ids": sorted(verified),
        "nonverified_ids": sorted(seen - set(verified)),
        "issues": issues,
        "truth_verified_by_runtime": False,
        "execution_authority": NO_AUTHORITY,
    }


def audit_connectors(root: Path = ROOT, environ: dict[str, str] | None = None) -> dict[str, Any]:
    """Check declared environment variables, never inspect or print their values."""
    environ = os.environ if environ is None else environ
    items = []
    for path in sorted((root / "plugins").glob("*.json")):
        try:
            blueprint = json.loads(path.read_text(encoding="utf-8"))
            name, kind = blueprint["name"], blueprint["type"]
            required = blueprint.get("env", [])
            if not isinstance(required, list) or any(not isinstance(x, str) for x in required):
                raise ValueError("invalid env declaration")
            missing = [key for key in required if not environ.get(key)]
            if kind == "connector":
                status = "MISSING_CONFIGURATION" if missing else "CONFIGURED_UNVERIFIED"
            elif kind == "capability":
                status = "HOST_BINDING_UNVERIFIED"
            else:
                status = "INVALID_BLUEPRINT"
            items.append({"name": name, "type": kind, "status": status, "missing_env_names": missing})
        except (ValueError, KeyError, json.JSONDecodeError) as exc:
            items.append({"name": path.stem, "type": "unknown", "status": "INVALID_BLUEPRINT",
                          "issues": [type(exc).__name__]})
    return {
        "status": "OFFLINE_DECLARATION_AUDIT",
        "connectors": items,
        "live_access_verified": False,
        "secrets_exposed": False,
        "execution_authority": NO_AUTHORITY,
    }


def audit_release(packet: Any, ledger: Any, artifact: bytes | None,
                  now: datetime | None = None) -> dict[str, Any]:
    """Compare immutable artifact digest and cited evidence; human approval remains external."""
    issues: list[str] = []
    evidence = audit_evidence(ledger, now=now)
    if not isinstance(packet, dict):
        packet = {}
        issues.append("release packet must be an object")
    if packet.get("mission_id") != evidence["mission_id"]:
        issues.append("release mission_id does not match evidence ledger")
    for field in ("artifact_id", "target", "release_owner", "rollback_plan"):
        if not isinstance(packet.get(field), str) or not packet[field].strip():
            issues.append(f"{field}: missing")
    claims = packet.get("claims")
    if not isinstance(claims, list):
        claims = []
        issues.append("claims must be an array")
    verified = set(evidence["fresh_verified_ids"])
    for i, item in enumerate(claims):
        if not isinstance(item, dict) or not isinstance(item.get("evidence_id"), str):
            issues.append(f"claim[{i}]: missing evidence_id")
        elif item["evidence_id"] not in verified:
            issues.append(f"claim[{i}]: evidence missing, unverified or stale")
    digest = packet.get("artifact_hash")
    if artifact is None:
        issues.append("artifact bytes not supplied: immutable digest cannot be checked")
    elif not isinstance(digest, str) or not hmac.compare_digest(
        digest.lower(), hashlib.sha256(artifact).hexdigest()
    ):
        issues.append("artifact SHA-256 mismatch")
    if evidence["issues"]:
        issues.append("evidence ledger has validation issues")
    approvals = packet.get("approval_evidence")
    if not isinstance(approvals, list) or not approvals or not all(
        isinstance(x, str) and x.strip() for x in approvals
    ):
        approval_gap = True
    else:
        approval_gap = False
    status = ("BLOCKED_INPUT" if issues else
              "BLOCKED_APPROVAL" if approval_gap else
              "READY_FOR_HUMAN_REVIEW")
    return {
        "status": status,
        "mission_id": evidence["mission_id"],
        "issues": issues,
        "approval_note": (
            "Approval references are self-declared; identity, scope, target, "
            "signature and revocation MUST be checked by an external human-owned system."
        ),
        "claimed_packet_status": packet.get("status"),
        "release_authorized": False,
        "execution_authority": NO_AUTHORITY,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Offline, read-only marketing readiness gates")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("connectors")
    ep = sub.add_parser("evidence")
    ep.add_argument("ledger_json")
    rp = sub.add_parser("release")
    rp.add_argument("release_json")
    rp.add_argument("ledger_json")
    rp.add_argument("--artifact", required=True, help="Exact local artifact to hash; never uploaded")
    args = parser.parse_args(argv)
    try:
        if args.command == "connectors":
            result = audit_connectors()
        elif args.command == "evidence":
            result = audit_evidence(json.loads(Path(args.ledger_json).read_text(encoding="utf-8")))
        else:
            packet = json.loads(Path(args.release_json).read_text(encoding="utf-8"))
            ledger = json.loads(Path(args.ledger_json).read_text(encoding="utf-8"))
            result = audit_release(packet, ledger, Path(args.artifact).read_bytes())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        result = {"status": "BLOCKED_INPUT", "issues": [type(exc).__name__],
                  "execution_authority": NO_AUTHORITY}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if result["status"].startswith("BLOCKED") else 0


if __name__ == "__main__":
    raise SystemExit(main())
