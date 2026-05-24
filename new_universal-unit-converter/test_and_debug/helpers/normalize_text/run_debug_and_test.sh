#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../../.."

python scripts/helpers/normalize_text/debug_normalize_text.py
python scripts/helpers/normalize_text/test_normalize_text.py

# run with
# bash universal-unit-converter/scripts/helpers/normalize_text/run_debug_and_test.sh