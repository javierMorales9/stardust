#!/bin/bash -e

ROOT_DIR="$(git rev-parse --show-toplevel)"

echo "Running Linters..."
"${ROOT_DIR}"/scripts/linters.sh
