# IX-py

**IX-py** is a zero-dependency Python environment and dependency manager designed to completely eliminate dependency hell and environment isolation issues for developers of all levels.

---

## Features

- True environment isolation without virtualenv or conda
- Automatic lockfile generation and dependency resolution
- Single CLI tool for managing Python project environments
- No hidden dependencies, no conflicts, minimal setup
- Compatible with Python 3.8 and above

---

## Installation

You can install IX-py via pip:

```bash
pip install ix-py
```

---

## Usage

Initialize a new isolated environment:

```bash
ix init
```

Install packages in the isolated environment:

```bash
ix install <package-name>
```

Generate a lockfile:

```bash
ix lock
```

Run your Python scripts inside the environment:

```bash
ix run python script.py
```

---

## Contributing

Contributions are welcome! Please fork the repo, create a branch, and submit pull requests. Ensure tests pass before submitting.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or suggestions, please open an issue or reach out on GitHub.

---

_Enjoy hassle-free Python environments with IX-py!_
