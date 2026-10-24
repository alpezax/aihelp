import argparse

from aihelp.commands.context import register_context_command
from aihelp.commands.ask import register_ask_command
from aihelp.commands.ignore import register_ignore_command


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="aihelp",
        description="CLI para extraer contexto y enviarlo a IA.",
    )

    subparsers = parser.add_subparsers(dest="command")

    register_context_command(subparsers)
    register_ask_command(subparsers)
    register_ignore_command(subparsers)

    return parser


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()