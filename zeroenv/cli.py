# zeroenv/cli.py

import click
from zeroenv import manager, doctor, lock

@click.group()
def main():
    """IX-py: Zero-Compromise Environment Manager CLI"""
    pass

@main.command()
def init():
    """Initialize a virtual environment in the current directory"""
    manager.initialize_environment()

@main.command()
def doctor():
    """Diagnose and repair the current Python environment"""
    doctor.run_diagnostics()

@main.command()
def lock():
    """Generate a lockfile to ensure reproducible installs"""
    lock.generate_lockfile()

if __name__ == "__main__":
    main()
