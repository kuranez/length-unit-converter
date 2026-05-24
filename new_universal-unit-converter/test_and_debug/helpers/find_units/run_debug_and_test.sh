#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../../.."

python scripts/helpers/find_units/debug_find_units.py
python scripts/helpers/find_units/test_find_units.py

# run with
# bash universal-unit-converter/scripts/helpers/find_units/run_debug_and_test.sh