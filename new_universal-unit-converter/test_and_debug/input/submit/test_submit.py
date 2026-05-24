"""Smoke test for submit()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

import app


def main() -> None:
    app.pending_query_signature = None
    app.text_input.value_input = "1500 kcal in joules"
    app.text_input.value = "1500 kcal in joules"
    app.submit()
    assert "Understood" in str(app.output_area.object)

    app.submit()
    assert "Result" in str(app.output_area.object)

    app.pending_query_signature = None
    app.text_input.value_input = "bad input"
    app.text_input.value = "bad input"
    app.submit()
    assert str(app.output_area.object) == "Please rephrase inquiry"

    print("submit smoke test passed")


if __name__ == "__main__":
    main()
