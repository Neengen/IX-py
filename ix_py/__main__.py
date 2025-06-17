import argparse
import sys
from ix_py import core

def main():
    parser = argparse.ArgumentParser(
        description="IX-py: Zero-dependency Python environment manager"
    )
    subparsers = parser.add_subparsers(dest="command")

    # ix init
    subparsers.add_parser("init", help="Initialize a new IX environment")

    # ix install <package>
    install_parser = subparsers.add_parser("install", help="Install a package")
    install_parser.add_argument("package", help="Package name to install")

    # ix lock
    subparsers.add_parser("lock", help="Generate lockfile from installed packages")

    # ix run <command>
    run_parser = subparsers.add_parser("run", help="Run a command in the IX environment")
    run_parser.add_argument("args", nargs=argparse.REMAINDER)

    args = parser.parse_args()

    if args.command == "init":
        core.init_environment()
    elif args.command == "install":
        core.install_package(args.package)
    elif args.command == "lock":
        core.generate_lockfile()
    elif args.command == "run":
        if not args.args:
            print("No command provided to run.")
            sys.exit(1)
        core.run_command(args.args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
