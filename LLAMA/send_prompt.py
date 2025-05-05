from ollama import chat
from ollama import ChatResponse

class Prompt():
    model: str = 'llama3.2:1b'

    def __init__(self, prompt):
        self.prompt = prompt

    def send(self) -> str:
        response: ChatResponse = chat(self.model, messages=[{
            'role': 'user',
            'content': self.prompt,
        }])
        return (response.message.content)