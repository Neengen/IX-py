import subprocess
import sys
import os
import pytest

IX_CMD = [sys.executable, "-m", "ix_py"]

def test_init_environment(tmp_path):
    os.chdir(tmp_path)
    result = subprocess.run(IX_CMD + ["init"], capture_output=True, text=True)
    assert result.returncode == 0
    assert ".ix_env" in os.listdir(tmp_path)

def test_install_invalid_package(tmp_path):
    os.chdir(tmp_path)
    subprocess.run(IX_CMD + ["init"], check=True)
    result = subprocess.run(IX_CMD + ["install", "nonexistent-package-xyz123"], capture_output=True, text=True)
    assert result.returncode != 0

def test_lockfile_creation(tmp_path):
    os.chdir(tmp_path)
    subprocess.run(IX_CMD + ["init"], check=True)
    subprocess.run(IX_CMD + ["install", "requests"], check=True)
    result = subprocess.run(IX_CMD + ["lock"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "ix-lock.txt" in os.listdir(tmp_path)

def test_run_script(tmp_path):
    os.chdir(tmp_path)
    subprocess.run(IX_CMD + ["init"], check=True)
    script = tmp_path / "hello.py"
    script.write_text("print('Hello from IX-py')")
    result = subprocess.run(IX_CMD + ["run", "python", "hello.py"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Hello from IX-py" in result.stdout
