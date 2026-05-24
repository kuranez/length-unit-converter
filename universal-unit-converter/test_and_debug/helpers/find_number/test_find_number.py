"""Smoke test for find_number()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from components.parser_helpers import find_number


def main() -> None:
    assert find_number("1500 kcal in joules") == (1500.0, "1500")
    assert find_number("1,250.5 km to miles") == (1250.5, "1250.5")
    assert find_number("2.5e3 g to kg") == (2500.0, "2.5e3")
    assert find_number("no number here") is None

    print("find_number smoke test passed")


if __name__ == "__main__":
    main()
