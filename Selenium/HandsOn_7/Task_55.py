"""Task 55 - test_simple_form_submission refactored to use SimpleFormPage (tests/test_simple_form.py)."""

import subprocess
import sys

if __name__ == "__main__":
    subprocess.run([sys.executable, "-m", "pytest", "tests/test_simple_form.py", "-v"])
