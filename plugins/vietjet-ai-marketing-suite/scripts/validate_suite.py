#!/usr/bin/env python3
"""Dependency-free structural and safety validation for the suite."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONT = re.compile(r"^---\n(.*?)\n---\n", re.S)
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")


def fail(message: str) -> None:
    raise AssertionError(message)


def meta(path: Path) -> dict[str, str]:
    match = FRONT.match(path.read_text(encoding="utf-8"))
    if not match:
        fail(f"missing YAML frontmatter: {path.relative_to(ROOT)}")
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"')
    return result


def main() -> int:
    plugin = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    if plugin["name"] != ROOT.name:
        fail("plugin name must match its directory")
    if not SEMVER.fullmatch(plugin["version"]):
        fail("plugin version must be strict semver")

    agents = sorted((ROOT / "agents").glob("*.md"))
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    rules = sorted((ROOT / "rules").glob("*.md"))
    if len(agents) != 18:
        fail(f"expected 18 canonical agents, found {len(agents)}")
    if len(skills) != 24:
        fail(f"expected 24 discoverable skills, found {len(skills)}")
    if len(rules) < 8:
        fail(f"expected at least 8 rules, found {len(rules)}")

    for path in skills:
        front = meta(path)
        if front.get("name") != path.parent.name:
            fail(f"skill name/folder mismatch: {path.relative_to(ROOT)}")
        if not front.get("description"):
            fail(f"missing skill description: {path.relative_to(ROOT)}")
        ui = path.parent / "agents" / "openai.yaml"
        if not ui.exists():
            fail(f"missing UI metadata: {ui.relative_to(ROOT)}")
        ui_text = ui.read_text(encoding="utf-8")
        if f"${path.parent.name}" not in ui_text:
            fail(f"default_prompt must mention skill: {ui.relative_to(ROOT)}")

    inventory = json.loads((ROOT / ".vietjet" / "manifest.json").read_text(encoding="utf-8"))
    if inventory["version"] != plugin["version"] or len(inventory["skills"]) != 24:
        fail("generated inventory is stale")

    for required in (
        ROOT / "schemas" / "mission-brief.schema.json",
        ROOT / "schemas" / "handoff.schema.json",
        ROOT / "schemas" / "experiment-card.schema.json",
        ROOT / "schemas" / "evidence-ledger.schema.json",
        ROOT / "schemas" / "decision-record.schema.json",
        ROOT / "schemas" / "release-packet.schema.json",
        ROOT / "schemas" / "learning-record.schema.json",
    ):
        json.loads(required.read_text(encoding="utf-8"))
    if not (ROOT / "research" / "claim-source-ledger.md").exists():
        fail("missing claim-source ledger")
    if not (ROOT / "docs" / "vietjet-group-marketing-operating-model.md").exists():
        fail("missing operating-model report")

    subprocess.run([sys.executable, str(ROOT / "scripts" / "sync_specialists.py"), "--check"], check=True)
    subprocess.run([sys.executable, str(ROOT / "tests" / "test_runtime.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "tests" / "test_suite.py")], check=True)
    print("VALIDATE SUITE: OK — 18 agents, 24 skills, team router, schemas and research ledger")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
        print(f"VALIDATE SUITE: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
