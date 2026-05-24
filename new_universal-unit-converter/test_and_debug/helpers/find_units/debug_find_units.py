"""Console debug helper for find_units()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from components.parser_helpers import find_units


def main() -> None:
    samples = [
        "1500 kcal in joules",
        "10 miles to km",
        "1 cup to ml",
        "bad input",
    ]

    for sample in samples:
        matches = find_units(sample)
        print(f"input={sample!r}")
        print(f"matches={[match['text'] for match in matches]!r}")
        print("---")


if __name__ == "__main__":
    main()
