"""Console debug helper for get_current_query()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

import app


def main() -> None:
    samples = ["1500 kcal in joules", " 10 miles to km ", ""]
    for sample in samples:
        app.text_input.value_input = sample
        print(f"input={sample!r} -> return={app.get_current_query()!r}")


if __name__ == "__main__":
    main()
