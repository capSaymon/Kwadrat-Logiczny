import openai
import os

from dotenv import load_dotenv

class Prompt():
    def __init__(self, prompt):
        self.prompt = prompt

    def send(self) -> str:
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Dokończ przykład"},
                {"role": "user", "content": self.prompt}
            ]
        )
        return response['choices'][0]['message']['content']