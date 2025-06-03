from ollama import chat
from ollama import ChatResponse

class Prompt():
    def __init__(self, prompt):
        self.prompt = prompt

    def send(self) -> str:
        model: str = 'llama3.2:3b'
        response: ChatResponse = chat(model, messages=[{
            'role': 'user',
            'content': self.prompt,
        }])
        return (response.message.content)