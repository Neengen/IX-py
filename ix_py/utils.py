import os
import subprocess
import sys

def run_subprocess(command_list, env=None, capture=False):
    """
    Run a subprocess with optional environment and capture.

    Args:
        command_list (list of str): Command and arguments to execute.
        env (dict, optional): Custom environment variables.
        capture (bool): If True, capture output.

    Returns:
        subprocess.CompletedProcess or None
    """
    try:
        if capture:
            return subprocess.run(
                command_list,
                env=env,
                check=True,
                text=True,
                capture_output=True
            )
        else:
            return subprocess.run(
                command_list,
                env=env,
                check=True
            )
    except subprocess.CalledProcessError as e:
        print(f"[✗] Command failed: {' '.join(command_list)}")
        print(e)
        sys.exit(1)

def print_banner():
    print("="*36)
    print("     IX-py Environment Manager")
    print("="*36)

def path_exists(path):
    """Check if a given path exists."""
    return os.path.exists(path)

def is_env_initialized(env_dir=".ix_env"):
    """Returns True if environment directory exists."""
    return os.path.isdir(env_dir)
