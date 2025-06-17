# zeroenv/utils.py

import hashlib
import os
import time
from pathlib import Path
from functools import wraps

def sha256_file(path: Path) -> str:
    """Return SHA256 hash of a file"""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def timeit(label):
    """Decorator to time a function's execution"""
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"[⏱] {label} took {end - start:.2f}s")
            return result
        return wrapped
    return decorator

def format_title(text):
    print("\n" + "=" * len(text))
    print(text)
    print("=" * len(text) + "\n")

def ensure_dir(path: Path):
    """Create a directory if it doesn't exist"""
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
