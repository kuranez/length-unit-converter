#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../../.."

python scripts/parse/convert/debug_convert.py
python scripts/parse/convert/test_convert.py

# run with
# bash universal-unit-converter/scripts/parse/convert/run_debug_and_test.sh