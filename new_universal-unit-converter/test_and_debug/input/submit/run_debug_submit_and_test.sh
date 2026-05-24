#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../../.."

python scripts/functions/submit/debug_submit.py
python scripts/functions/submit/test_submit.py

# run with
# bash universal-unit-converter/scripts/functions/submit/run_debug_submit_and_test.sh