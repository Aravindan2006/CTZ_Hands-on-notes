"""Task 56 - test_checkbox_demo and test_dropdown_selection refactored to use their page objects."""

import subprocess
import sys

if __name__ == "__main__":
    subprocess.run([sys.executable, "-m", "pytest", "tests/test_checkbox.py", "tests/test_dropdown.py", "-v"])
