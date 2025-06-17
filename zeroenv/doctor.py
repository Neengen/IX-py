# zeroenv/doctor.py

import os
import sys
import subprocess
from zeroenv import manager

def run_diagnostics():
    """Run a series of health checks on the Python environment"""
    print("[*] Running diagnostics...")

    checks = [
        check_python_version,
        check_env_existence,
        check_pip_installed,
        check_path_permissions
    ]

    issues = 0
    for check in checks:
        try:
            check()
        except Exception as e:
            print(f"[!] {check.__name__} failed: {e}")
            issues += 1

    if issues == 0:
        print("[✓] Environment is healthy.")
    else:
        print(f"[!] {issues} issues found. Run `ix init` to recreate env.")

def check_python_version():
    required = (3, 8)
    current = sys.version_info[:2]
    if current < required:
        raise RuntimeError(f"Python {required[0]}.{required[1]}+ required, found {current[0]}.{current[1]}")
    print(f"[✓] Python version OK ({current[0]}.{current[1]})")

def check_env_existence():
    if not manager.environment_exists():
        raise RuntimeError("Environment not initialized. Run `ix init`.")
    print("[✓] Virtual environment exists")

def check_pip_installed():
    try:
        subprocess.check_output([manager.get_environment_python(), "-m", "pip", "--version"])
    except Exception:
        raise RuntimeError("pip is not installed or not working inside the environment")
    print("[✓] pip is working")

def check_path_permissions():
    test_path = os.path.join(os.getcwd(), ".ixenv", "perm_test.tmp")
    try:
        with open(test_path, "w") as f:
            f.write("test")
        os.remove(test_path)
    except Exception:
        raise RuntimeError("Permission issue writing inside virtual environment directory")
    print("[✓] Directory permissions OK")
