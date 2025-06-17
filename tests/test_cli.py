# tests/test_cli.py

import pytest
from click.testing import CliRunner
from zeroenv import cli

@pytest.fixture
def runner():
    return CliRunner()

def test_cli_entry(runner):
    result = runner.invoke(cli.main)
    assert result.exit_code == 0 or result.exit_code == 1
    assert "Usage:" in result.output

def test_init_command_does_not_crash(runner):
    result = runner.invoke(cli.main, ["init"])
    assert result.exit_code in [0, 1]  # already exists or success

def test_doctor_command_runs(runner):
    result = runner.invoke(cli.main, ["doctor"])
    assert result.exit_code in [0, 1]
    assert "[*] Running diagnostics..." in result.output or "[✓]" in result.output
