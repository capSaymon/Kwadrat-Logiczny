import os
import sys

from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from HyDE.llama_embeddings import LlamaEmbeddings
from HyDE.hyde_values import CHROMA_PATH, PROMPT_SENTENCE

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LLAMA.send_prompt import Prompt
from schemat import LLM


class rag(LLM):
    def __init__(self, *, file_name: str = None, sentence: str = None):
        self.file_name = file_name
        self.sentence = sentence

    def result(self):
        if self.file_name:
            file_path = self.search_path()
            with open(file_path, 'r', encoding='utf-8') as file:
                task = file.read()
        else:
            task = self.sentence

        llama_embeddings = LlamaEmbeddings(task)
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=llama_embeddings)

        results = db.similarity_search_with_relevance_scores(task, k=9)
        if len(results) == 0 or results[0][1] > 1:
            print(f"There is no matching sentences")
            return

        context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
        prompt_template = ChatPromptTemplate.from_template(PROMPT_SENTENCE)
        prompt = prompt_template.format(context=context_text, question=task)

        #LOOK FOR PROMPT
        #print(f'\n\n\n{prompt}\n\n\n\n')

        outcome = Prompt(prompt).send()

        if self.file_name:
            return task, outcome
        else:
            return outcome