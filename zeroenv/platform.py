# zeroenv/platform.py

import os
import platform
import sys

def get_os():
    """Return simplified name of the operating system"""
    name = platform.system().lower()
    if "windows" in name:
        return "windows"
    elif "darwin" in name:
        return "macos"
    elif "linux" in name:
        return "linux"
    else:
        return "unknown"

def is_windows():
    return get_os() == "windows"

def is_macos():
    return get_os() == "macos"

def is_linux():
    return get_os() == "linux"

def get_python_bin_path(venv_root):
    """Return full path to Python binary inside a venv on any OS"""
    if is_windows():
        return venv_root / "Scripts" / "python.exe"
    else:
        return venv_root / "bin" / "python"

def print_platform_summary():
    print(f"[•] OS: {get_os()}")
    print(f"[•] Python Version: {sys.version.split()[0]}")
    print(f"[•] Platform: {platform.platform()}")
