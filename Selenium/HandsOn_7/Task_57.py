"""Task 57 - test_input_form_submit using the new InputFormPage."""

import subprocess
import sys

if __name__ == "__main__":
    subprocess.run([sys.executable, "-m", "pytest", "tests/test_input_form.py", "-v"])
