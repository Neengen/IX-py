# tests/test_doctor.py

import pytest
from zeroenv import doctor, manager

@pytest.fixture(autouse=True)
def ensure_env():
    """Make sure the environment is ready before diagnostic tests"""
    if not manager.environment_exists():
        manager.initialize_environment()
    yield

def test_python_version_check():
    # Should pass on Python 3.8+
    doctor.check_python_version()

def test_env_existence_check():
    assert manager.environment_exists()
    doctor.check_env_existence()

def test_pip_check_passes():
    doctor.check_pip_installed()

def test_permissions_check():
    doctor.check_path_permissions()

def test_run_diagnostics_output(capsys):
    doctor.run_diagnostics()
    captured = capsys.readouterr()
    assert "[*] Running diagnostics..." in captured.out
    assert "[✓]" in captured.out
