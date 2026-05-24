"""Console debug helper for format_result()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from components.parser_core import format_result


def main() -> None:
    samples = [
        (
            {
                "amount": 1500.0,
                "source": {"text": "kcal"},
                "target": {"text": "joules"},
            },
            6276000.0,
        ),
        (
            {
                "amount": 10.0,
                "source": {"text": "miles"},
                "target": {"text": "km"},
            },
            16.09344,
        ),
    ]

    for parsed_query, result in samples:
        print(f"input={parsed_query!r}, result={result!r}")
        print(format_result(parsed_query, result))
        print("---")


if __name__ == "__main__":
    main()
