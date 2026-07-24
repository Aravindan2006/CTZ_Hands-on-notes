"""Task 47 - generate the pytest-html report."""

import subprocess
import sys

if __name__ == "__main__":
    subprocess.run([
        sys.executable, "-m", "pytest", "-v",
        "Task_42.py", "Task_43.py", "Task_45.py", "Task_49.py",
        "--html=report.html", "--self-contained-html",
    ])
