# Campaign Production Preflight

These scripts use the Python standard library only.

Run the complete gate:

```bash
python3 scripts/preflight/run_preflight.py campaigns/football-summer-2026
```

Individual checks:

```bash
python3 scripts/preflight/check_claims.py campaigns/football-summer-2026
python3 scripts/preflight/check_assets.py campaigns/football-summer-2026
python3 scripts/preflight/check_html_release_safety.py campaigns/football-summer-2026
```

The runner refreshes:

- `audit/ASSET_MANIFEST.md`
- `audit/PREFLIGHT_REPORT.md`
- `audit/RELEASE_READINESS_REPORT.md`

A deterministic preflight result never grants `HUMAN_QA_PASSED` or `APPROVED_FOR_RELEASE`. Any P0 issue keeps the campaign `NOT RELEASE READY`.
