#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../../.."

python scripts/helpers/find_number/debug_find_number.py
python scripts/helpers/find_number/test_find_number.py

# run with
# bash universal-unit-converter/scripts/helpers/find_number/run_debug_and_test.sh