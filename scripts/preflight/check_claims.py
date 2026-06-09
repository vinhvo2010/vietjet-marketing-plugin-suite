#!/usr/bin/env python3
"""Detect unsupported campaign claims using Python standard library only."""

from __future__ import annotations

import re
import sys
from pathlib import Path


TEXT_SUFFIXES = {".md", ".html", ".js"}
SKIP_PARTS = {"audit", ".git"}
SKIP_FILES = {"CAMPAIGN_AUDIT_AND_SYSTEM_UPGRADE.md"}

ASSUMPTION_CONTEXT = re.compile(
    r"assumption|assumptions|assumption_only|calculation_from_assumptions|"
    r"giả định|gia dinh|placeholder|data_unavailable|data unavailable|"
    r"not forecast|không phải dự báo|not approved|chưa duyệt",
    re.IGNORECASE,
)
WARNING_CONTEXT = re.compile(
    r"\bno\b|do not|must not|không|cấm|avoid|prohibit|warning|risk|flag|"
    r"review|required|không được|không dùng|không claim",
    re.IGNORECASE,
)
EVIDENCE_CONTEXT = re.compile(
    r"evidence|register|logged|log entry|source|bằng chứng|audit/|"
    r"not approved|not verified|not completed|chưa duyệt|không được duyệt",
    re.IGNORECASE,
)
NUMBER = r"(?:\d[\d,.]*\s*(?:B|M|K)?\s*(?:VND|USD|Đ|đ)?|\d+(?:\.\d+)?%)"


def issue(severity: str, code: str, path: Path, line: int, message: str) -> dict:
    return {
        "severity": severity,
        "code": code,
        "path": str(path),
        "line": line,
        "message": message,
    }


def iter_source_files(campaign: Path):
    for path in campaign.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if path.name in SKIP_FILES or any(part in SKIP_PARTS for part in path.parts):
            continue
        yield path


def check_claims(campaign: Path) -> list[dict]:
    findings: list[dict] = []
    claim_patterns = {
        "UNLABELED_BUDGET": re.compile(rf"\bbudget\b.*{NUMBER}|{NUMBER}.*\bbudget\b", re.I),
        "UNLABELED_BOOKINGS": re.compile(rf"\bbookings?\b.*{NUMBER}|{NUMBER}.*\bbookings?\b", re.I),
        "UNLABELED_REVENUE": re.compile(
            rf"\b(?:gross\s+revenue|revenue|doanh thu)\b.*{NUMBER}|"
            rf"{NUMBER}.*\b(?:gross\s+revenue|revenue|doanh thu)\b",
            re.I,
        ),
        "UNLABELED_ABV": re.compile(rf"\bABV\b.*{NUMBER}|{NUMBER}.*\bABV\b", re.I),
    }
    status_pattern = re.compile(r"\b(PASS|VERIFIED|APPROVED|COMPLETED)\b", re.I)
    official_pattern = re.compile(r"\bofficial\s+(?:sponsor|partner|airline|travel partner)\b", re.I)
    ticket_pattern = re.compile(r"\b(?:match|game|event)\s+tickets?\b|vé\s+xem\s+trận", re.I)
    fare_pattern = re.compile(r"\b(?:fare|inventory|scarcity)\b|0\s*[Đđ]|vé\s+0", re.I)
    roi_pattern = re.compile(r"\bROI\b", re.I)
    incremental_pattern = re.compile(r"\bincremental\s+revenue\b|doanh thu gia tăng", re.I)

    for path in iter_source_files(campaign):
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for line_no, line in enumerate(lines, 1):
            compact = line.strip()
            if not compact:
                continue
            for code, pattern in claim_patterns.items():
                if pattern.search(compact) and not ASSUMPTION_CONTEXT.search(compact):
                    findings.append(
                        issue("P0", code, path, line_no, "Numeric claim lacks an assumption/evidence label.")
                    )
            if roi_pattern.search(compact) and not WARNING_CONTEXT.search(compact):
                findings.append(issue("P0", "ROI_WITHOUT_VERIFIED_INPUTS", path, line_no, "ROI claim requires verified cost and revenue evidence."))
            if incremental_pattern.search(compact):
                window = " ".join(lines[max(0, line_no - 3): min(len(lines), line_no + 2)])
                if not re.search(r"holdout|control|counterfactual|đối chứng", window, re.I) and not WARNING_CONTEXT.search(compact):
                    findings.append(issue("P0", "INCREMENTAL_WITHOUT_CONTROL", path, line_no, "Incremental revenue claim lacks holdout/control evidence."))
            if status_pattern.search(compact) and not EVIDENCE_CONTEXT.search(compact) and not WARNING_CONTEXT.search(compact):
                findings.append(issue("P0", "UNSUPPORTED_STATUS_LABEL", path, line_no, "PASS/VERIFIED/APPROVED/COMPLETED label lacks evidence context."))
            if official_pattern.search(compact) and not WARNING_CONTEXT.search(compact):
                findings.append(issue("P0", "UNVERIFIED_OFFICIAL_RELATIONSHIP", path, line_no, "Official relationship wording lacks prohibition/review context."))
            if ticket_pattern.search(compact) and not WARNING_CONTEXT.search(compact):
                findings.append(issue("P0", "TICKET_ACCESS_CLAIM", path, line_no, "Ticket-access claim lacks evidence or prohibition context."))
            if fare_pattern.search(compact) and not WARNING_CONTEXT.search(compact) and not ASSUMPTION_CONTEXT.search(compact):
                findings.append(issue("P0", "UNVERIFIED_COMMERCIAL_CLAIM", path, line_no, "Fare/inventory/scarcity claim lacks source or assumption context."))
    return findings


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/preflight/check_claims.py <campaign-folder>")
        return 2
    campaign = Path(sys.argv[1]).resolve()
    findings = check_claims(campaign)
    for finding in findings:
        print(f"{finding['severity']} {finding['code']} {finding['path']}:{finding['line']} - {finding['message']}")
    print(f"Claim issues: {len(findings)}")
    return 1 if any(item["severity"] == "P0" for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
