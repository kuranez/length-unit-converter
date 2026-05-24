"""Console debug helper for parse_query()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from components.parser_core import parse_query


def main() -> None:
    samples = [
        "1500 kcal in joules",
        "10 miles to km",
        "1 cup to ml",
        "bad input",
    ]

    for sample in samples:
        print(f"input={sample!r} -> return={parse_query(sample)!r}")


if __name__ == "__main__":
    main()
