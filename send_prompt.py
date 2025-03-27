from ollama import chat
from ollama import ChatResponse

class Prompt():
    model: str = 'KL_LLM'
    
    def __init__(self, prompt, question):
        self.prompt = prompt
        self.question = question

    def send(self) -> str:
        response: ChatResponse = chat(self.model, messages=[{
            'role': 'user',
            'content': self.prompt,
        }])
        return (response.message.content)