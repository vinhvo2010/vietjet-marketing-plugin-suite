#!/usr/bin/env python3
"""Validate/sync this suite and optionally copy it to an explicit target."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def sync_source() -> None:
    subprocess.run([sys.executable, str(ROOT / 'scripts' / 'sync_specialists.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'scripts' / 'validate_suite.py')], check=True)


def inventory(root: Path) -> dict[str, object]:
    version = json.loads((root / '.codex-plugin' / 'plugin.json').read_text(encoding='utf-8'))['version']
    return {
        'installed': True,
        'version': version,
        'agents': len(list((root / 'agents').glob('*.md'))),
        'skills': len(list((root / 'skills').glob('*/SKILL.md'))),
        'rules': len(list((root / 'rules').glob('*.md'))),
        'connectors': len(list((root / 'plugins').glob('*.json'))),
        'project_root': str(root),
    }


def write_state(root: Path) -> dict[str, object]:
    state = inventory(root)
    state_dir = root / '.vietjet'
    state_dir.mkdir(exist_ok=True)
    (state_dir / 'install-state.json').write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
    )
    return state


def install(target: Path, force: bool) -> Path:
    source = ROOT.resolve()
    destination = target.expanduser().resolve()
    if destination == source:
        return source
    if is_within(destination, source):
        raise ValueError('target cannot be inside the source suite')
    if destination.exists():
        if not force:
            raise FileExistsError('target exists; pass --force to replace this exact target')
        if destination.is_symlink():
            raise ValueError('refusing to replace a symlink target')
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        source,
        destination,
        ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'),
    )
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description='Install Vietjet AI Marketing Suite v5')
    parser.add_argument('--target', type=Path, help='Explicit destination directory; omit to sync in place')
    parser.add_argument('--force', action='store_true', help='Replace the exact target when it already exists')
    args = parser.parse_args()

    sync_source()
    installed_root = install(args.target, args.force) if args.target else ROOT
    state = write_state(installed_root)
    print(json.dumps(state, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, FileExistsError, subprocess.CalledProcessError) as exc:
        print(f'INSTALL: FAIL — {exc}', file=sys.stderr)
        raise SystemExit(1)

