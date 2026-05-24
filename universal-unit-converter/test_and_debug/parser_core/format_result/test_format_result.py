"""Smoke test for format_result()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from components.parser_core import format_result


def main() -> None:
    result = format_result(
        {
            "amount": 1500.0,
            "source": {"text": "kcal"},
            "target": {"text": "joules"},
        },
        6276000.0,
    )
    assert "Result" in result
    assert "1,500 kcal" in result
    assert "6,276,000 joules" in result

    print("format_result smoke test passed")


if __name__ == "__main__":
    main()
