#!/usr/bin/env python3
"""Check microsite release-safety controls."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def finding(severity: str, code: str, path: Path, message: str) -> dict:
    return {"severity": severity, "code": code, "path": str(path), "message": message}


def check_html_release_safety(campaign: Path) -> list[dict]:
    preview = campaign / "html-preview"
    index = preview / "index.html"
    script = preview / "script.js"
    html = index.read_text(encoding="utf-8", errors="replace") if index.exists() else ""
    js = script.read_text(encoding="utf-8", errors="replace") if script.exists() else ""
    combined = html + "\n" + js
    findings: list[dict] = []

    if "CONCEPT PREVIEW — NOT PRODUCTION READY" not in html:
        findings.append(finding("P0", "MISSING_CONCEPT_BANNER", index, "Concept-only production warning is missing."))
    if "Planning Scenario — Assumptions Only" not in html:
        findings.append(finding("P0", "UNSAFE_BUSINESS_CASE_LABEL", index, "Planning scenario is not explicitly labeled assumptions-only."))
    if "ASSUMPTION ONLY — NOT FORECAST" not in html:
        findings.append(finding("P0", "MISSING_SCENARIO_WARNING", index, "Scenario cards lack assumption-only warning."))
    if "DRAFT AI-GENERATED ASSET — HUMAN QA REQUIRED" not in combined:
        findings.append(finding("P0", "MISSING_DRAFT_ASSET_LABEL", preview, "Draft generated assets lack visible human-QA-required label."))
    if "Current release status: NOT RELEASE READY" not in html:
        findings.append(finding("P0", "MISSING_RELEASE_BLOCKER_PANEL", index, "Release blocker panel is missing."))
    if re.search(r"\bAPPROVED_FOR_RELEASE\b", combined):
        findings.append(finding("P0", "UNSUPPORTED_RELEASE_STATE", preview, "HTML/JS assigns an approval-only release state."))
    if re.search(r"Board of Directors|Ban Giám đốc", combined, re.I):
        findings.append(finding("P0", "HARDCODED_FINAL_APPROVER", preview, "A prohibited final approver label is hardcoded."))
    if re.search(r"<img[^>]+src=[\"']https?://", html, re.I):
        findings.append(finding("P0", "REMOTE_IMAGE", index, "Remote image detected."))
    if re.search(r"<(?:script|link)[^>]+(?:src|href)=[\"']https?://", html, re.I):
        findings.append(finding("P0", "EXTERNAL_CDN", index, "External CDN dependency detected."))
    if "navigator.clipboard" in js:
        copy_window = js[js.find("navigator.clipboard") - 2500: js.find("navigator.clipboard") + 1000]
        commercial_number = re.compile(
            r"(?:booking|revenue|doanh thu|ABV|ROI|ngân sách|budget).{0,80}\d|"
            r"\d.{0,80}(?:booking|revenue|doanh thu|ABV|ROI|ngân sách|budget)",
            re.I | re.S,
        )
        if commercial_number.search(copy_window):
            findings.append(finding("P0", "CLIPBOARD_UNVERIFIED_NUMBERS", script, "Clipboard summary includes unverified commercial/performance fields."))
        if "All numbers are assumptions only and not approved targets or forecasts." not in copy_window:
            findings.append(finding("P0", "CLIPBOARD_MISSING_WARNING", script, "Clipboard summary lacks the required assumption warning."))
    if re.search(r"\bBusiness Case\b", html, re.I):
        findings.append(finding("P1", "LEGACY_BUSINESS_CASE_WORDING", index, "Legacy Business Case wording remains in concept preview."))
    if 'data-release-mode="release"' in html and "assets/release/" not in combined:
        findings.append(finding("P0", "RELEASE_MODE_ASSET_PATH", preview, "Release mode does not enforce assets/release paths."))
    return findings


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/preflight/check_html_release_safety.py <campaign-folder>")
        return 2
    findings = check_html_release_safety(Path(sys.argv[1]).resolve())
    for item in findings:
        print(f"{item['severity']} {item['code']} {item['path']} - {item['message']}")
    print(f"HTML safety issues: {len(findings)}")
    return 1 if any(item["severity"] == "P0" for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
