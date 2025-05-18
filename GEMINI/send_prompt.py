import os

from google import genai
from google.genai import types
from dotenv import load_dotenv

class Prompt():
    def __init__(self, prompt):
        self.prompt = prompt

    def send(self) -> str:
        load_dotenv()
        client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
        model = "gemini-1.5-flash"
        
        contents = [types.Content(parts=[types.Part.from_text(text=self.prompt)])]
        generate_content_config = types.GenerateContentConfig(response_mime_type="text/plain", )

        output = ""
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            output += chunk.text

        return output