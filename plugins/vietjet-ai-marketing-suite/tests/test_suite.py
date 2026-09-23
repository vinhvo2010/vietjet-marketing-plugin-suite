import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_output import check_text


def main():
    plugin = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    assert plugin["name"] == "vietjet-ai-marketing-suite"
    assert plugin["version"].split("+", 1)[0] == "5.0.4"
    assert len(plugin["interface"]["defaultPrompt"]) <= 3
    assert len(list((ROOT / "agents").glob("*.md"))) == 18
    assert len(list((ROOT / "skills").glob("*/SKILL.md"))) == 24
    assert all("PLUGIN_ROOT" in path.read_text(encoding="utf-8") for path in (ROOT / "skills").glob("*/SKILL.md"))
    assert (ROOT / "rules" / "vietjet-delivery-standard.md").exists()
    assert (ROOT / "rules" / "vietjet-group-marketing-operating-model.md").exists()
    assert (ROOT / "rules" / "vietjet-agent-collaboration.md").exists()
    assert (ROOT / "schemas" / "mission-brief.schema.json").exists()
    assert (ROOT / "research" / "claim-source-ledger.md").exists()
    assert check_text('---\ndescription: "Load factor 30%"\n---\n# Safe document') == []
    print("SUITE TEST: OK")


if __name__ == "__main__":
    main()
