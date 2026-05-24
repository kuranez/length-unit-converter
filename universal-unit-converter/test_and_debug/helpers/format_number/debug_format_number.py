"""Console debug helper for format_number()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from components.parser_core import format_number


def main() -> None:
	samples = [
		0,
		1,
		1.2345,
		1500,
		6.283185307179,
		0.0000001234,
		-42.5,
	]

	for sample in samples:
		print(f"input={sample!r} -> return={format_number(sample)!r}")


if __name__ == "__main__":
	main()

