from langchain.embeddings.base import Embeddings
from llama_cpp import Llama
from typing import List

class LlamaEmbeddings(Embeddings):
    def __init__(self, model_path: str):
        self.llm = Llama(model_path=model_path, embedding=True)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self.llm.embed(txt) for txt in texts]

    def embed_query(self, text: str) -> List[float]:
        return self.llm.embed(text)
