"""Smoke test for format_confirmation()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from components.parser_core import format_confirmation


def main() -> None:
    result = format_confirmation({
        "amount": 1500.0,
        "source": {"category": "energy", "text": "kcal"},
        "target": {"text": "joules"},
    })
    assert "Understood" in result
    assert "1,500" in result
    assert "kcal" in result
    assert "joules" in result

    print("format_confirmation smoke test passed")


if __name__ == "__main__":
    main()
