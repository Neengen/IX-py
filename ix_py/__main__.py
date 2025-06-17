import argparse
import sys

from ix_py import core, env, lockfile, utils, constants

def main():
    utils.print_banner()

    parser = argparse.ArgumentParser(
        prog="ix",
        description="IX-py: Zero-dependency Python environment and dependency manager",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # init command
    init_parser = subparsers.add_parser("init", help="Initialize isolated environment")

    # install command
    install_parser = subparsers.add_parser("install", help="Install package into environment")
    install_parser.add_argument("package", help="Package name to install")

    # lock command
    lock_parser = subparsers.add_parser("lock", help="Generate lockfile from environment")

    # run command
    run_parser = subparsers.add_parser("run", help="Run a command inside the environment")
    run_parser.add_argument("cmd", nargs=argparse.REMAINDER, help="Command and args to run")

    args = parser.parse_args()

    if args.command == "init":
        if env.create_env():
            print(constants.MSG_ENV_CREATED)
        else:
            print(constants.MSG_ENV_EXISTS)

    elif args.command == "install":
        try:
            env.ensure_env_exists()
        except FileNotFoundError as e:
            print(constants.MSG_ENV_NOT_FOUND)
            sys.exit(1)
        core.install_package(args.package)

    elif args.command == "lock":
        try:
            env.ensure_env_exists()
        except FileNotFoundError as e:
            print(constants.MSG_ENV_NOT_FOUND)
            sys.exit(1)
        # Run pip freeze and write to lockfile
        from ix_py.utils import run_subprocess
        result = run_subprocess(
            [sys.executable, "-m", "pip", "freeze", "--path", env.get_env_path()],
            capture=True
        )
        lockfile.write_lockfile(result.stdout.splitlines())

    elif args.command == "run":
        try:
            env.ensure_env_exists()
        except FileNotFoundError as e:
            print(constants.MSG_ENV_NOT_FOUND)
            sys.exit(1)
        if not args.cmd:
            print("[!] No command provided to run")
            sys.exit(1)
        core.run_command(args.cmd)

if __name__ == "__main__":
    main()
