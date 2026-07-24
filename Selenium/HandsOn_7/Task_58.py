"""Task 58 - run the whole suite with an HTML report."""

import subprocess
import sys

if __name__ == "__main__":
    subprocess.run([
        sys.executable, "-m", "pytest", "tests/", "-v",
        "--html=report.html", "--self-contained-html",
    ])
