import argparse

from aihelp.services.openai_service import OpenAIService


def handle_ask(args: argparse.Namespace) -> None:
    service = OpenAIService()
    result = service.ask(args.prompt)
    print(result)


def register_ask_command(subparsers) -> None:
    parser = subparsers.add_parser(
        "ask",
        help="Envía un prompt a ChatGPT",
        description="Envía un prompt a OpenAI usando el token de CHATGPT_TOKEN.",
    )
    parser.add_argument(
        "prompt",
        help='Prompt a enviar, por ejemplo: aihelp ask "explica este proyecto"',
    )
    parser.set_defaults(func=handle_ask)