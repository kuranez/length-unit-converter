#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../../.."

python scripts/math/format_number/debug_format_number.py
python scripts/math/format_number/test_format_number.py

# run with
# bash universal-unit-converter/scripts/math/format_number/run_debug_and_test.sh