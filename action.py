from LLAMA.ML_llama import llama
from OPENAI.ML_openai import gpt
from HyDE.RAG import rag
from GEMINI.ML_gemini import gemini
from check_sentences import SentenceChecker

import os

class Run():
    def __init__(self, sentence: str = None, llm: int = 2, technique: int = 2):
        self.sentence = sentence
        self.llm = llm
        self.technique = technique
        self.folder_name = 'results'

    def result(self) -> str:
        index: int = 0
        end: int = 10

        while index < end:
            if self.llm == 1:
                outcome = self.run_GEMINI()
            elif self.llm == 2 and self.technique != 6:
                outcome = self.run_LLAMA()
            elif self.llm == 3:
                outcome = self.run_OPENAI()
            elif self.technique == 6:
                outcome = self.run_HyDE()
            else:
                print("Invalid combination of LLM and technique.")

            if outcome is None or len(outcome.splitlines()) > 5:
                continue

            index = index + 1
            if self.check_outcome(outcome):
                break

        return outcome
    
    def check_outcome(self, outcome) -> bool:
        check = SentenceChecker(self.sentence, outcome)
        try:
            check.test_response_format()
            if check.test_relation_between_sentences():
                return True
        except AssertionError:
            pass
        return False
    
    def save(self, answear):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(BASE_DIR, self.folder_name)
        os.makedirs(folder_path, exist_ok=True)

        existing_files = [f for f in os.listdir(folder_path) if f.startswith("sentences_") and f.endswith(".txt")]

        max_index = -1
        for fname in existing_files:
            try:
                num = int(fname[len("sentences_"):-len(".txt")])
                max_index = max(max_index, num)
            except ValueError:
                continue

        file_name = f"sentences_{max_index + 1}"

        addition = f'Answear:\n'
        file_path = self.search_path(file_name)
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(addition + answear)

    def search_path(self, file_name):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        QUESTIONS_PATH = os.path.join(BASE_DIR, self.folder_name)
        file_path = os.path.join(QUESTIONS_PATH, f'{file_name}.txt')
        return file_path

    def run_LLAMA(self) -> str:
        return llama(sentence=self.sentence, prompt_technique=self.technique).run()

    def run_OPENAI(self) -> str:
        return gpt(sentence=self.sentence, prompt_technique=self.technique).run()

    def run_HyDE(self) -> str:
        return rag(sentence=self.sentence).run()

    def run_GEMINI(self) -> str:
        return gemini(sentence=self.sentence, prompt_technique=self.technique).run()