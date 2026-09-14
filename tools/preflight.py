from __future__ import annotations

import shutil
import subprocess
import sys


def main() -> int:
    python_ok = sys.version_info >= (3, 11)
    git_path = shutil.which("git")
    print(f"[{'PASS' if python_ok else 'FAIL'}] Python 3.11+: {sys.version.split()[0]}")
    print(f"[{'PASS' if git_path else 'FAIL'}] Git on PATH: {git_path or 'not found'}")
    completed = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"], capture_output=True, text=True)
    combined = completed.stdout + completed.stderr
    baseline_ok = "Ran 7 tests" in combined and "failures=2, errors=1" in combined
    print(f"[{'PASS' if baseline_ok else 'FAIL'}] Starter baseline: 7 tests, 3 intentional failures")
    return 0 if python_ok and git_path and baseline_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
