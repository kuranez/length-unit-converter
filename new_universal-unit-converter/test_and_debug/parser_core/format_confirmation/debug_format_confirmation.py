"""Console debug helper for format_confirmation()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from components.parser_core import format_confirmation


def main() -> None:
    samples = [
        {
            "amount": 1500.0,
            "source": {"category": "energy", "text": "kcal"},
            "target": {"text": "joules"},
        },
        {
            "amount": 10.0,
            "source": {"category": "length", "text": "miles"},
            "target": {"text": "km"},
        },
    ]

    for sample in samples:
        print("input=", sample)
        print(format_confirmation(sample))
        print("---")


if __name__ == "__main__":
    main()
