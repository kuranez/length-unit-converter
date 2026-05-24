"""Smoke test for normalize_text()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from components.parser_helpers import normalize_text


def main() -> None:
    assert normalize_text(" 1500 KCal in Joules ") == "1500 kcal in joules"
    assert normalize_text("10 Miles → km") == "10 miles to km"
    assert normalize_text("CAPS and µ units") == "caps and u units"

    print("normalize_text smoke test passed")


if __name__ == "__main__":
    main()
