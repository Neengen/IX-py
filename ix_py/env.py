import os

ENV_DIR_NAME = ".ix_env"

def get_env_path():
    """Returns the absolute path to the IX environment directory."""
    return os.path.abspath(ENV_DIR_NAME)

def ensure_env_exists():
    """Checks if IX environment is initialized, otherwise raises an error."""
    env_path = get_env_path()
    if not os.path.isdir(env_path):
        raise FileNotFoundError(f"IX environment not found at {env_path}. Run `ix init` first.")
    return env_path

def get_site_packages_path():
    """Returns the path to where packages are installed inside IX environment."""
    return get_env_path()

def create_env():
    """Creates the environment directory if it doesn't exist."""
    env_path = get_env_path()
    if not os.path.exists(env_path):
        os.makedirs(env_path)
        return True
    return False
