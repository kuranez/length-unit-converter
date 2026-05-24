"""Parser helper utilities: normalization, unit matcher building, and low-level finders.

This module builds `UNIT_MATCHERS` from the `UNIT_TABLE` in config.py and
exposes `normalize_text`, `find_number`, and `find_units` helpers used by the
parser core.
"""

from __future__ import annotations

from typing import Any, Dict, List
import re

from config import UNIT_TABLE as CONFIG_UNIT_TABLE


def normalize_text(text: str) -> str:
    cleaned = text.lower().replace("μ", "u").replace("µ", "u")
    cleaned = cleaned.replace("→", " to ").replace("=", " to ")
    cleaned = re.sub(r"[^a-z0-9\s\.,\-\+]", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


UNIT_MATCHERS: List[Dict[str, Any]] = []
for category, units in CONFIG_UNIT_TABLE.items():
    for canonical_name, factor, aliases in units:
        for alias in aliases:
            normalized_alias = normalize_text(alias)
            UNIT_MATCHERS.append(
                {
                    "category": category,
                    "canonical": canonical_name,
                    "factor": factor,
                    "alias": normalized_alias,
                    "pattern": re.compile(rf"(?<!\w){re.escape(normalized_alias)}(?!\w)"),
                }
            )

UNIT_MATCHERS.sort(key=lambda item: len(str(item["alias"])), reverse=True)

NUMBER_PATTERN = re.compile(
    r"(?<!\w)[+-]?(?:\d[\d,]*\.?\d*|\.\d+)(?:e[+-]?\d+)?(?!\w)", re.IGNORECASE
)
CONNECTOR_PATTERN = re.compile(r"\b(?:in|to|into)\b", re.IGNORECASE)


def find_number(text: str) -> tuple[float, str] | None:
    match = NUMBER_PATTERN.search(text)
    if not match:
        return None

    amount_text = match.group(0).replace(",", "")
    try:
        return float(amount_text), amount_text
    except ValueError:
        return None


def find_units(text: str) -> List[Dict[str, Any]]:
    matches: List[Dict[str, Any]] = []
    for unit_matcher in UNIT_MATCHERS:
        pattern = unit_matcher["pattern"]
        if not isinstance(pattern, re.Pattern):
            continue
        for match in pattern.finditer(text):
            matches.append(
                {
                    "start": match.start(),
                    "end": match.end(),
                    "text": match.group(0),
                    "category": unit_matcher["category"],
                    "canonical": unit_matcher["canonical"],
                    "factor": unit_matcher["factor"],
                    "alias": unit_matcher["alias"],
                }
            )

    matches.sort(key=lambda item: (item["start"], -(item["end"] - item["start"])))
    resolved_matches: List[Dict[str, Any]] = []
    last_end = -1
    for match in matches:
        if match["start"] >= last_end:
            resolved_matches.append(match)
            last_end = match["end"]
    return resolved_matches
