"""Smoke test for format_number()."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from components.parser_core import format_number


def main() -> None:
	assert format_number(0) == "0"
	assert format_number(1) == "1"
	assert format_number(1.2345) == "1.2345"
	assert format_number(1500) == "1,500"
	assert format_number(6.283185307179) == "6.283185307179"
	assert format_number(0.0000001234) == "0.0000001234"
	assert format_number(-42.5) == "-42.5"

	print("format_number smoke test passed")


if __name__ == "__main__":
	main()

