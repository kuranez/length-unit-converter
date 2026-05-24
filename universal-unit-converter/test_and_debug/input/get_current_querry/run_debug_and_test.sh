#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../../.."

python scripts/functions/get_current_querry/debug_get_current_query.py
python scripts/functions/get_current_querry/test_get_current_query.py

# run with
# bash universal-unit-converter/scripts/functions/get_current_querry/run_debug_and_test.sh