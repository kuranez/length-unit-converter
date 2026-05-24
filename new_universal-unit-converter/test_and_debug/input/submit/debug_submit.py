"""Console debug helper for submit()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

import app


def main() -> None:
    samples = ["1500 kcal in joules", "10 miles to km", "bad input"]

    for sample in samples:
        app.text_input.value_input = sample
        app.text_input.value = sample
        app.pending_query_signature = None
        app.submit()
        print(f"input={sample!r}")
        print(f"output={app.output_area.object!r}")
        print("---")


if __name__ == "__main__":
    main()
