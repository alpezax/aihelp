from openai import OpenAI

from aihelp.core.config import get_chatgpt_token, get_default_model


class OpenAIService:
    def __init__(self) -> None:
        self.client = OpenAI(api_key=get_chatgpt_token())
        self.model = get_default_model()

    def ask(self, prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text