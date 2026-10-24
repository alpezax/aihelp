import argparse
from pathlib import Path

DEFAULT_IGNORE_CONTENT = """# Directorios
.venv/
venv/
env/
node_modules/
dist/
build/
.git/

# Python
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/

# IDEs
.vscode/
.idea/

# Sistema
.DS_Store
Thumbs.db

# Entorno
.env
.env.*

# Logs/temp
*.log
*.tmp
*.swp
"""


def handle_ignore(args: argparse.Namespace) -> None:
    ignore_path = Path.cwd() / ".aihelpignore"

    if ignore_path.exists() and not args.force:
        print("Ya existe .aihelpignore. Usa --force para sobrescribirlo.")
        return

    ignore_path.write_text(DEFAULT_IGNORE_CONTENT, encoding="utf-8")
    print(f"Creado: {ignore_path}")


def register_ignore_command(subparsers) -> None:
    parser = subparsers.add_parser(
        "ignore",
        help="Crea un fichero .aihelpignore en el directorio actual",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Sobrescribe .aihelpignore si ya existe",
    )
    parser.set_defaults(func=handle_ignore)