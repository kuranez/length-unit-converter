"""Smoke test for find_units()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from components.parser_helpers import find_units


def main() -> None:
    matches = find_units("1500 kcal in joules")
    assert [match["text"] for match in matches] == ["kcal", "joules"]

    matches = find_units("10 miles to km")
    assert [match["text"] for match in matches] == ["miles", "km"]

    assert find_units("bad input") == []

    print("find_units smoke test passed")


if __name__ == "__main__":
    main()
