#!/bin/bash
# run_tests.sh

echo "--- Initializing SGIN Test Suite ---"

# 1. Run Unit Tests (Fast, no dependencies)
python -m pytest tests/
if [ $? -ne 0 ]; then
    echo "Unit Tests Failed. Aborting."
    exit 1
fi

# 2. Run Integration Tests (Requires IPC/Hardware mocks)
pytest tests/integration/
if [ $? -ne 0 ]; then
    echo "Integration Tests Failed."
    exit 1
fi

echo "--- All Tests Passed: System Ready for Hardening ---"
