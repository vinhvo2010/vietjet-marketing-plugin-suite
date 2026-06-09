#!/usr/bin/env python3
"""Inspect campaign media assets without third-party dependencies."""

from __future__ import annotations

import re
import struct
import sys
from pathlib import Path


MEDIA_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".mp4", ".mov", ".webm", ".m4v"}
VIDEO_SUFFIXES = {".mp4", ".mov", ".webm", ".m4v"}
MIME_EXTENSIONS = {
    "image/png": {".png"},
    "image/jpeg": {".jpg", ".jpeg"},
    "image/gif": {".gif"},
    "image/webp": {".webp"},
}


def detect_mime(data: bytes) -> str:
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "image/png"
    if data.startswith(b"\xff\xd8\xff"):
        return "image/jpeg"
    if data.startswith((b"GIF87a", b"GIF89a")):
        return "image/gif"
    if data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        return "image/webp"
    if len(data) > 12 and data[4:8] == b"ftyp":
        return "video/mp4"
    return "application/octet-stream"


def png_dimensions(data: bytes):
    return struct.unpack(">II", data[16:24]) if len(data) >= 24 else (None, None)


def gif_dimensions(data: bytes):
    return struct.unpack("<HH", data[6:10]) if len(data) >= 10 else (None, None)


def jpeg_dimensions(data: bytes):
    index = 2
    while index + 9 < len(data):
        if data[index] != 0xFF:
            index += 1
            continue
        marker = data[index + 1]
        index += 2
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            continue
        if index + 2 > len(data):
            break
        length = struct.unpack(">H", data[index:index + 2])[0]
        if marker in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
            height, width = struct.unpack(">HH", data[index + 3:index + 7])
            return width, height
        index += length
    return None, None


def dimensions(mime: str, data: bytes):
    if mime == "image/png":
        return png_dimensions(data)
    if mime == "image/jpeg":
        return jpeg_dimensions(data)
    if mime == "image/gif":
        return gif_dimensions(data)
    return None, None


def expected_ratios(name: str):
    patterns = [
        ("video-8s", [9 / 16], "9:16"),
        ("app-banner", [3 / 1, 16 / 5], "3:1 or 16:5"),
        ("airport-screen", [16 / 9], "16:9"),
        ("story-9x16", [9 / 16], "9:16"),
        ("kv-4x5", [4 / 5], "4:5"),
        ("carousel-", [4 / 5], "4:5"),
        ("dashboard", [16 / 9], "16:9"),
        ("hero", [16 / 9], "16:9"),
    ]
    for token, ratios, label in patterns:
        if token in name.lower():
            return ratios, label
    return [], "DATA_UNAVAILABLE"


def intended_use(name: str) -> str:
    stem = name.lower()
    if "hero" in stem:
        return "Microsite hero"
    if "kv-4x5" in stem:
        return "4:5 key visual"
    if "story-9x16" in stem:
        return "9:16 story/video reference"
    if "carousel-" in stem:
        return "4:5 carousel slide"
    if "app-banner" in stem:
        return "App banner"
    if "airport-screen" in stem:
        return "Airport screen"
    if "dashboard" in stem:
        return "Planning dashboard visual"
    return "Unclassified campaign asset"


def inspect_assets(campaign: Path) -> tuple[list[dict], list[dict]]:
    asset_root = campaign / "html-preview" / "assets"
    manifest_path = campaign / "audit" / "ASSET_MANIFEST.md"
    manifest_text = manifest_path.read_text(encoding="utf-8", errors="replace") if manifest_path.exists() else ""
    findings: list[dict] = []
    inventory: list[dict] = []

    media_files = [p for p in asset_root.rglob("*") if p.is_file() and p.suffix.lower() in MEDIA_SUFFIXES]
    html_path = campaign / "html-preview" / "index.html"
    html_text = html_path.read_text(encoding="utf-8", errors="replace") if html_path.exists() else ""
    for path in sorted(media_files):
        relative_to_assets = path.relative_to(asset_root)
        controlled = relative_to_assets.parts[0] in {"draft", "approved", "release"}
        referenced = str(relative_to_assets) in html_text
        active = controlled or referenced
        data = path.read_bytes()
        mime = detect_mime(data)
        width, height = dimensions(mime, data)
        ratio = width / height if width and height else None
        expected, expected_label = expected_ratios(path.name)
        reasons = []
        statuses = []

        if active and mime in MIME_EXTENSIONS and path.suffix.lower() not in MIME_EXTENSIONS[mime]:
            findings.append({"severity": "P0", "code": "MIME_EXTENSION_MISMATCH", "path": str(path), "message": f"{mime} content uses {path.suffix} extension."})
            reasons.append("MIME/extension mismatch")
            statuses.append("PREFLIGHT_FAILED")
        if active and (width is None or height is None):
            findings.append({"severity": "P1", "code": "UNKNOWN_DIMENSIONS", "path": str(path), "message": "Dimensions could not be determined with the standard-library parser."})
            reasons.append("Unknown dimensions")
        elif active and expected and not any(abs(ratio - target) <= 0.035 for target in expected):
            findings.append({"severity": "P0", "code": "ASPECT_RATIO_MISMATCH", "path": str(path), "message": f"Actual {width}:{height} ({ratio:.4f}) does not match required {expected_label}."})
            reasons.append(f"Aspect ratio mismatch; required {expected_label}")
            statuses.append("PREFLIGHT_FAILED")
        if active and path.name not in manifest_text and "PENDING_SCAN" not in manifest_text:
            findings.append({"severity": "P1", "code": "ASSET_NOT_IN_MANIFEST", "path": str(path), "message": "Asset is not listed in the current asset manifest."})
            reasons.append("Asset not in manifest")
        if active and "approved" not in path.parts and "release" not in path.parts:
            findings.append({
                "severity": "P1",
                "code": "HUMAN_VISUAL_QA_REQUIRED",
                "path": str(path),
                "message": "Asset lacks human QA evidence for generated text/logo, fake UI/signage, and prohibited/off-policy objects.",
            })
            reasons.append("Human visual QA evidence missing")
        if path.suffix.lower() in VIDEO_SUFFIXES:
            findings.append({
                "severity": "P0",
                "code": "VIDEO_DURATION_NOT_VALIDATED",
                "path": str(path),
                "message": "Video duration requires deterministic validation before release.",
            })
            reasons.append("Video duration not validated")
            statuses.append("PREFLIGHT_FAILED")

        inventory.append({
            "filename": str(path.relative_to(campaign)),
            "intended_use": intended_use(path.name),
            "required_format": expected_label,
            "mime": mime,
            "extension": path.suffix.lower(),
            "width": width,
            "height": height,
            "ratio": f"{ratio:.4f}" if ratio else "UNKNOWN",
            "duration": "N/A" if path.suffix.lower() not in VIDEO_SUFFIXES else "NOT_VALIDATED",
            "exists": "YES",
            "source_prompt": "`html-preview/assets/GEMINI_IMAGE_PROMPTS_V2_ASSET_SAFE.md`" if "draft" in path.parts else "`html-preview/assets/GEMINI_IMAGE_PROMPTS.md`",
            "generator": "Built-in image generation plus local JPEG normalization" if "draft" in path.parts else "Reported legacy AI generator; evidence pending",
            "generated_date": "2026-06-09" if "draft" in path.parts else "DATA_UNAVAILABLE",
            "preflight": "LEGACY_DO_NOT_RELEASE" if not active else ("PREFLIGHT_FAILED" if statuses else "PREFLIGHT_PASSED"),
            "reason": "; ".join(reasons) if reasons else ("Legacy root asset retained for audit history; not referenced" if not active else "Deterministic MIME/dimension/ratio checks passed; human QA required"),
        })

    promised_video = False
    video_pattern = re.compile(r"8[- ]second|8s\b|8\s*giây|8\s*seconds", re.I)
    for path in campaign.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".html", ".js"} and "audit" not in path.parts:
            if video_pattern.search(path.read_text(encoding="utf-8", errors="replace")):
                promised_video = True
                break
    videos = [p for p in media_files if p.suffix.lower() in VIDEO_SUFFIXES]
    if promised_video and not videos:
        findings.append({"severity": "P0", "code": "MISSING_PROMISED_VIDEO", "path": str(asset_root), "message": "An eight-second video is promised but no video file exists."})
        inventory.append({
            "filename": "MISSING: promised 8-second video",
            "intended_use": "9:16 short-form video",
            "required_format": "9:16 video, 8 seconds",
            "mime": "MISSING",
            "extension": "MISSING",
            "width": None,
            "height": None,
            "ratio": "MISSING",
            "duration": "MISSING",
            "exists": "NO",
            "source_prompt": "`html-preview/assets/VIDEO_8S_GENERATION_PROMPT.md`",
            "generator": "DATA_UNAVAILABLE",
            "generated_date": "DATA_UNAVAILABLE",
            "preflight": "PREFLIGHT_FAILED",
            "reason": "Missing promised video deliverable",
        })
    return findings, inventory


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/preflight/check_assets.py <campaign-folder>")
        return 2
    findings, _ = inspect_assets(Path(sys.argv[1]).resolve())
    for finding in findings:
        print(f"{finding['severity']} {finding['code']} {finding['path']} - {finding['message']}")
    print(f"Asset issues: {len(findings)}")
    return 1 if any(item["severity"] == "P0" for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
