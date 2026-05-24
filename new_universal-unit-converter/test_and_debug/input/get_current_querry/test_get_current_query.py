"""Smoke test for get_current_query()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

import app


def main() -> None:
    app.text_input.value_input = "1500 kcal in joules"
    assert app.get_current_query() == "1500 kcal in joules"

    app.text_input.value_input = ""
    app.text_input.value = "10 miles to km"
    assert app.get_current_query() == "10 miles to km"

    print("get_current_query smoke test passed")


if __name__ == "__main__":
    main()
