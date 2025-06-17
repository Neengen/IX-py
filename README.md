# IX-py

IX-py is a zero-dependency Python environment and dependency manager designed to completely eliminate dependency hell and environment isolation issues for developers of all levels.

## Features

- True environment isolation without virtualenv or conda
- Automatic lockfile generation and dependency resolution
- Single CLI tool for managing Python project environments
- No hidden dependencies, no conflicts, minimal setup
- Compatible with Python 3.8 and above

## Installation

You can install IX-py via pip:

```bash
pip install ix-py

Usage:::
Initialize a new isolated environment in the current directory: ix init
Install packages into the isolated environment: ix install <package-name>
Generate a lockfile of your environment’s packages: ix lock
Run commands or scripts inside the isolated environment: ix run python script.py

Why IX-py?
If you've struggled with dependency conflicts, virtual environment complexities, or conda headaches, IX-py offers a straightforward, zero-dependency alternative. It isolates environments in a single directory, automates package management, and removes the typical friction developers face.

Contributing
Contributions are welcome! Please fork the repo, create a feature branch, and submit a pull request. Ensure tests pass before submitting.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For questions or suggestions, please open an issue or reach out on GitHub.

Enjoy hassle-free Python environments with IX-py!
