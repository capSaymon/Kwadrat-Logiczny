import os
import sys

from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from HyDE.llama_embeddings import LlamaEmbeddings
from HyDE.hyde_values import CHROMA_PATH, PROMPT_SENTENCE
from values import domain_prompt, domain_text

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LLAMA.send_prompt import Prompt
from schemat import LLM


class rag():
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

        domain = f'{domain_text}{self.create_domain(task)}\n---\n'

        llama_embeddings = LlamaEmbeddings(task)
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=llama_embeddings)

        results = db.similarity_search_with_relevance_scores(task, k=9)
        if len(results) == 0 or results[0][1] > 1:
            print(f"There is no matching sentences")
            return task, None


        context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
        prompt_template = ChatPromptTemplate.from_template(domain + PROMPT_SENTENCE)
        prompt = prompt_template.format(context=context_text, question=task)

        #LOOK FOR PROMPT
        #print(f'\n\n\n{prompt}\n\n\n\n')

        outcome = Prompt(domain + prompt).send()

        if self.file_name:
            return task, outcome
        else:
            return outcome
        
    def create_domain(self, task):
        return Prompt(f'{domain_prompt} \n\n {task}').send()
    
    def run(self):
        if self.file_name:
            question, outcome = self.result()
            if 'RAG' in question:
                print(f'File {self.file_name} allready have answear for RAG')
            else:
                return question, outcome
            
        else:
            outcome = self.result()
            return outcome
    
    def run_test(self):
        question, outcome = self.result()
        print(question,'\n\n',outcome,'\n\n', '-'*50, '\n\n')
        return question, outcome
    
    def search_path(self, folder_name='questions'):
        current_path = os.path.abspath(__file__)
        while True:
            if os.path.basename(current_path) == "Kwadrat-Logiczny":
                BASE_DIR = current_path
                break
            current_path = os.path.dirname(current_path)
            if current_path == os.path.dirname(current_path):
                raise FileNotFoundError("Not found 'Kwadrat-Logiczny'")
        
        QUESTIONS_PATH = os.path.join(BASE_DIR, folder_name)
        file_path = os.path.join(QUESTIONS_PATH, f'{self.file_name}.txt')

        return file_path
