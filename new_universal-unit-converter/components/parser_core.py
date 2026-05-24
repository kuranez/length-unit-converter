"""Parser core: high-level parse/convert/format functions.

This module depends on the lower-level helpers in `parser_helpers` and
exposes `parse_query`, `convert`, and formatting helpers used by the UI.
"""

from __future__ import annotations

from typing import Any, Dict

from .parser_helpers import normalize_text, find_number, find_units, CONNECTOR_PATTERN


def format_number(value: float) -> str:
    formatted = f"{value:,.12f}".rstrip("0").rstrip(".")
    return formatted or "0"


def parse_query(query: str) -> Dict[str, Any] | None:
    normalized_query = normalize_text(query)
    if not normalized_query:
        return None

    amount_info = find_number(normalized_query)
    if amount_info is None:
        return None

    amount_value, amount_text = amount_info
    unit_matches = find_units(normalized_query)
    if len(unit_matches) < 2:
        return None

    connector_match = CONNECTOR_PATTERN.search(normalized_query)
    if connector_match:
        source_candidates = [match for match in unit_matches if match["end"] <= connector_match.start()]
        target_candidates = [match for match in unit_matches if match["start"] >= connector_match.end()]
        if source_candidates and target_candidates:
            source_unit = source_candidates[-1]
            target_unit = target_candidates[0]
        else:
            source_unit, target_unit = unit_matches[0], unit_matches[1]
    else:
        source_unit, target_unit = unit_matches[0], unit_matches[1]

    if source_unit["category"] != target_unit["category"]:
        return None

    if amount_text not in normalized_query:
        return None

    amount_position = normalized_query.find(amount_text)
    if amount_position == -1 or amount_position > source_unit["start"]:
        return None

    if source_unit["start"] > target_unit["start"]:
        return None

    return {
        "amount": amount_value,
        "source": source_unit,
        "target": target_unit,
    }


def convert(parsed_query: Dict[str, Any]) -> float:
    amount = float(parsed_query["amount"])
    source_unit = parsed_query["source"]
    target_unit = parsed_query["target"]
    return amount * float(source_unit["factor"]) / float(target_unit["factor"])


def format_confirmation(parsed_query: Dict[str, Any]) -> str:
    amount_text = format_number(float(parsed_query["amount"]))
    source_unit = parsed_query["source"]
    target_unit = parsed_query["target"]
    category = str(source_unit["category"]).title()
    return (
        f"Understood inquiry **:** `{amount_text} {source_unit['text']} in {target_unit['text']}`  \n"
        f"Detected category **:** `{category}`  \n\n"
        "Submit again or press `Enter` to calculate."
    )


def format_result(parsed_query: Dict[str, Any], result: float) -> str:
    amount_text = format_number(float(parsed_query["amount"]))
    source_unit = parsed_query["source"]
    target_unit = parsed_query["target"]
    return f"Result **:** `{amount_text} {source_unit['text']}` = `{format_number(result)} {target_unit['text']}`"
