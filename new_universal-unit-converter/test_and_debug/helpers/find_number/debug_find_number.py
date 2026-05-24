"""Console debug helper for find_number()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from components.parser_helpers import find_number


def main() -> None:
    samples = [
        "1500 kcal in joules",
        "1,250.5 km to miles",
        "2.5e3 g to kg",
        "no number here",
    ]

    for sample in samples:
        print(f"input={sample!r} -> return={find_number(sample)!r}")


if __name__ == "__main__":
    main()
