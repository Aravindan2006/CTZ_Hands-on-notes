"""Task 44 - run Task_42 and Task_43, both should pass."""

import subprocess
import sys

if __name__ == "__main__":
    subprocess.run([sys.executable, "-m", "pytest", "-v", "Task_42.py", "Task_43.py"])
