import os


def get_chatgpt_token() -> str:
    token = os.getenv("CHATGPT_TOKEN")
    if not token:
        raise ValueError(
            "Falta la variable de entorno CHATGPT_TOKEN. "
            "Ejemplo: export CHATGPT_TOKEN='tu_token'"
        )
    return token


def get_default_model() -> str:
    return "gpt-5.4"