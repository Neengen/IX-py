import os
import subprocess
import sys

ENV_DIR = ".ix_env"
LOCKFILE = "ix-lock.txt"

def init_environment():
    """Create an isolated environment directory."""
    if not os.path.exists(ENV_DIR):
        os.makedirs(ENV_DIR)
        print(f"[✓] Initialized IX environment at ./{ENV_DIR}")
    else:
        print(f"[!] Environment already exists at ./{ENV_DIR}")

def install_package(package_name):
    """Install a package into the isolated IX environment."""
    pip_args = [sys.executable, "-m", "pip", "install", package_name, "--target", ENV_DIR]
    subprocess.run(pip_args, check=True)
    print(f"[✓] Installed '{package_name}' into ./{ENV_DIR}")

def generate_lockfile():
    """Generate a basic lockfile by listing installed packages in IX env."""
    pip_args = [sys.executable, "-m", "pip", "freeze", "--path", ENV_DIR]
    result = subprocess.run(pip_args, capture_output=True, text=True, check=True)
    
    with open(LOCKFILE, "w") as f:
        f.write(result.stdout)
    print(f"[✓] Lockfile created at ./{LOCKFILE}")

def run_command(args):
    """Run a command with the IX environment in sys.path."""
    full_env_path = os.path.abspath(ENV_DIR)
    if not os.path.exists(full_env_path):
        print(f"[✗] Environment not initialized. Run `ix init` first.")
        sys.exit(1)

    env = os.environ.copy()
    pythonpath = full_env_path + os.pathsep + env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = pythonpath

    subprocess.run(args, env=env)
