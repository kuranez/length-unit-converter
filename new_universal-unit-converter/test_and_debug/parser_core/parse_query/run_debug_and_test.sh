#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../../.."

python scripts/parse/parse_query/debug_parse_query.py
python scripts/parse/parse_query/test_parse_query.py

# run with
# bash universal-unit-converter/scripts/parse/parse_query/run_debug_and_test.sh