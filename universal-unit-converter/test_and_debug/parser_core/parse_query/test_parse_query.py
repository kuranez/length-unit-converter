"""Smoke test for parse_query()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from components.parser_core import parse_query


def main() -> None:
    parsed = parse_query("1500 kcal in joules")
    assert parsed is not None
    assert parsed["amount"] == 1500.0
    assert parsed["source"]["text"] == "kcal"
    assert parsed["target"]["text"] == "joules"

    assert parse_query("bad input") is None

    print("parse_query smoke test passed")


if __name__ == "__main__":
    main()
