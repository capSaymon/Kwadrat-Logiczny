import sys
import os

from langchain.embeddings.base import Embeddings
from llama_cpp import Llama
from typing import List
from HyDE.hyde_values import MODEL_PATH, PROMPT_EMBED

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LLAMA.send_prompt import Prompt

class LlamaEmbeddings(Embeddings):
    def __init__(self, task: str ="", model_path: str = MODEL_PATH):
        self.llm = Llama(model_path=MODEL_PATH, embedding=True)
        self.task = task

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self.llm.embed(txt) for txt in texts]

    def embed_query(self, text: str) -> List[float]:
        if self.task:
            prompt_sentence: str = PROMPT_EMBED + self.task
            text = Prompt(prompt_sentence).send()
            print(f'\n\n\n\n {text} \n\n\n\n')
        return self.llm.embed(text)