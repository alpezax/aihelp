import argparse
from pathlib import Path

from aihelp.services.file_service import render_files_context
from aihelp.services.tree_service import render_tree


def handle_context(args: argparse.Namespace) -> None:
    root = Path.cwd()

    if args.tree:
        print(render_tree(root))

    if args.files:
        if args.tree:
            print()
        print(render_files_context(root))

    if not args.tree and not args.files:
        print("Debes indicar una opción: --tree o --files")


def register_context_command(subparsers) -> None:
    parser = subparsers.add_parser(
        "context",
        help="Obtiene contexto del proyecto actual",
    )
    parser.add_argument("--tree", action="store_true", help="Muestra árbol del proyecto")
    parser.add_argument("--files", action="store_true", help="Muestra ficheros y contenido")
    parser.set_defaults(func=handle_context)