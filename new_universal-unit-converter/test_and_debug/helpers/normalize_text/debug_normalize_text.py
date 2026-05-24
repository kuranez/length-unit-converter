"""Console debug helper for normalize_text()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from components.parser_helpers import normalize_text


def main() -> None:
    samples = [
        " 1500 KCal in Joules ",
        "10 Miles → km",
        "CAPS and µ units",
    ]

    for sample in samples:
        print(f"input={sample!r} -> return={normalize_text(sample)!r}")


if __name__ == "__main__":
    main()
