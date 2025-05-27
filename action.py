from LLAMA.ML_llama import llama
from OPENAI.ML_openai import gpt
from HyDE.RAG import rag
from GEMINI.ML_gemini import gemini
from check_sentences import SentenceChecker

class Run():
    def __init__(self, sentence: str = None, llm: int = 2, technique: int = 2):
        self.sentence = sentence
        self.llm = llm
        self.technique = technique

    def result(self) -> str:
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

    def run_LLAMA(self) -> str:
        return llama(sentence=self.sentence, prompt_technique=self.technique).run()

    def run_OPENAI(self) -> str:
        return gpt(sentence=self.sentence, prompt_technique=self.technique).run()

    def run_HyDE(self) -> str:
        return rag(sentence=self.sentence).run()

    def run_GEMINI(self) -> str:
        return gemini(sentence=self.sentence, prompt_technique=self.technique).run()