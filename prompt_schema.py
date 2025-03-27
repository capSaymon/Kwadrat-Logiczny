from ollama import chat
from ollama import ChatResponse

class Promptr_schema():
    def __init__(self, prompt, question):
        self.prompt = prompt
        self.question = question

    def run(self) -> str:
        response: ChatResponse = chat(model='KL_LLM', messages=[{
            'role': 'user',
            'content': self.prompt,
        }])
        return (response.message.content)