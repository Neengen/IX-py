import os

# Root directory for environment
ENV_DIR_NAME = ".ix_env"
ENV_PATH = os.path.abspath(ENV_DIR_NAME)

# Lockfile name and path
LOCKFILE_NAME = "ix-lock.txt"
LOCKFILE_PATH = os.path.abspath(LOCKFILE_NAME)

# Metadata
TOOL_NAME = "IX-py"
TOOL_VERSION = "0.1.0"
PYTHON_MIN_VERSION = (3, 8)

# Messages
MSG_ENV_EXISTS = f"[!] Environment already exists at {ENV_DIR_NAME}"
MSG_ENV_CREATED = f"[✓] Initialized environment at {ENV_DIR_NAME}"
MSG_LOCK_CREATED = f"[✓] Lockfile written to {LOCKFILE_NAME}"
MSG_ENV_NOT_FOUND = f"[✗] IX environment not found. Run `ix init` first."
