import os

LOCKFILE_NAME = "ix-lock.txt"

def get_lockfile_path():
    """Returns the absolute path to the IX lockfile."""
    return os.path.abspath(LOCKFILE_NAME)

def write_lockfile(package_list):
    """
    Writes a list of frozen packages to the lockfile.
    Args:
        package_list (list of str): List of pip freeze output lines
    """
    lockfile_path = get_lockfile_path()
    with open(lockfile_path, "w") as f:
        for line in package_list:
            f.write(f"{line.strip()}\n")
    print(f"[✓] Lockfile saved to {LOCKFILE_NAME}")

def read_lockfile():
    """
    Reads the lockfile and returns the package list.
    Returns:
        list of str: Lines representing packages and their versions
    """
    lockfile_path = get_lockfile_path()
    if not os.path.exists(lockfile_path):
        print(f"[!] Lockfile not found: {LOCKFILE_NAME}")
        return []
    with open(lockfile_path, "r") as f:
        return [line.strip() for line in f.readlines()]
