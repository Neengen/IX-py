# tests/test_manager.py

import shutil
import pytest
from pathlib import Path
from zeroenv import manager

@pytest.fixture(autouse=True)
def clean_env():
    """Ensure a clean test environment before and after each test"""
    env_path = Path(".ixenv")
    if env_path.exists():
        shutil.rmtree(env_path)
    yield
    if env_path.exists():
        shutil.rmtree(env_path)

def test_environment_is_created():
    assert not manager.environment_exists()
    manager.initialize_environment()
    assert manager.environment_exists()

def test_environment_is_idempotent():
    manager.initialize_environment()
    first_state = manager.environment_exists()
    manager.initialize_environment()
    second_state = manager.environment_exists()
    assert first_state and second_state

def test_remove_environment():
    manager.initialize_environment()
    assert manager.environment_exists()
    manager.remove_environment()
    assert not manager.environment_exists()
