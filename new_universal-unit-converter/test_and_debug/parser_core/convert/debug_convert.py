"""Console debug helper for convert()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from components.parser_core import convert


def main() -> None:
    samples = [
        {
            "amount": 1500.0,
            "source": {"factor": 4184.0, "text": "kcal"},
            "target": {"factor": 1.0, "text": "joules"},
        },
        {
            "amount": 10.0,
            "source": {"factor": 1609.344, "text": "miles"},
            "target": {"factor": 1000.0, "text": "km"},
        },
    ]

    for sample in samples:
        print(f"input={sample!r} -> return={convert(sample)!r}")


if __name__ == "__main__":
    main()
