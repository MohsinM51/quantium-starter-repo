#!/bin/bash

# Activate the virtual environment
source /Users/mohsin/Desktop/Computers/pythonProject/quantium-starter-repo/venv

# Execute the test suite
python3 /Users/mohsin/Desktop/Computers/pythonProject/quantium-starter-repo/dash-app-for-analysis/testing.py

# Capture the exit code
test_exit_code=$?

# Deactivate the virtual environment
deactivate

# Return the exit code
if [ $test_exit_code -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
