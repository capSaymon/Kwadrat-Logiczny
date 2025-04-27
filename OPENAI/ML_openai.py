import openai
import os

from prompt_sentence import prompt
from dotenv import load_dotenv

class run():
    def __init__(self, file_name):
        self.file_name = file_name

    def result(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Dokończ przykład"},
                {"role": "user", "content": prompt}
            ]
        )

        file_path = self.search_path()
        with open(file_path, 'r', encoding='utf-8') as file:
            task = file.read()

        return(response['choices'][0]['message']['content'])
    
    def save(self, answear):
        file_path = self.search_path()
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write('\nOPENAI \nAnswear:\n'+answear)

    def search_path(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        QUESTIONS_PATH = os.path.join(BASE_DIR, 'questions')
        file_path = os.path.join(QUESTIONS_PATH, f'{self.file_name}.txt')
        return file_path

