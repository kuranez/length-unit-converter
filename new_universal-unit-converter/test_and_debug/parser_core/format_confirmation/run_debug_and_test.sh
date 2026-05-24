#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../../.."

python scripts/parse/format_confirmation/debug_format_confirmation.py
python scripts/parse/format_confirmation/test_format_confirmation.py

# run with
# bash universal-unit-converter/scripts/parse/format_confirmation/run_debug_and_test.sh