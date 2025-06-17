# zeroenv/manager.py

import os
import sys
import subprocess
import shutil
from pathlib import Path

VENV_DIR = Path(".ixenv")

def _venv_python_path():
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    else:
        return VENV_DIR / "bin" / "python"

def environment_exists():
    """Check if a virtual environment already exists"""
    return _venv_python_path().exists()

def initialize_environment():
    """Create a new virtual environment if it doesn't already exist"""
    if environment_exists():
        print(f"[✓] Environment already exists at {VENV_DIR}")
        return

    print(f"[+] Creating virtual environment at {VENV_DIR}")
    try:
        subprocess.check_call([sys.executable, "-m", "virtualenv", str(VENV_DIR)])
        print(f"[✓] Virtual environment created at {VENV_DIR}")
    except subprocess.CalledProcessError as e:
        print(f"[✗] Failed to create environment: {e}")
        sys.exit(1)

def get_environment_python():
    """Return the path to the venv Python binary"""
    if not environment_exists():
        raise RuntimeError("No environment found. Run `ix init` first.")
    return str(_venv_python_path())

def remove_environment():
    """Optional: Remove the virtual environment completely"""
    if VENV_DIR.exists():
        shutil.rmtree(VENV_DIR)
        print(f"[−] Removed environment at {VENV_DIR}")
