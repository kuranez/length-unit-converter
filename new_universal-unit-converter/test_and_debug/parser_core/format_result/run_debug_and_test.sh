#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../../.."

python scripts/parse/format_result/debug_format_result.py
python scripts/parse/format_result/test_format_result.py

# run with
# bash universal-unit-converter/scripts/parse/format_result/run_debug_and_test.sh