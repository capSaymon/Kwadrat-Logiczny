import os
import sys

from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from HyDE.llama_embeddings import LlamaEmbeddings
from HyDE.hyde_values import CHROMA_PATH, PROMPT_SENTENCE
from HyDE.create_chroma import Run_chroma

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LLAMA.send_prompt import Prompt
from values import QUESTIONS_PATH


class rag():
    def __init__(self, file_name):
        self.file_name = file_name

    def result(self):
        file_path = self.search_path()
        with open(file_path, 'r', encoding='utf-8') as file:
            task = file.read()

        llama_embeddings = LlamaEmbeddings(task)
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=llama_embeddings)

        results = db.similarity_search_with_relevance_scores(task, k=9)
        if len(results) == 0 or results[0][1] > 1:
            print(f"There is no matching sentences")
            return

        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        prompt_template = ChatPromptTemplate.from_template(PROMPT_SENTENCE)
        prompt = prompt_template.format(context=context_text, question=task)
    #LOOK FOR PROMPT
        #print(f'\n\n\n{prompt}\n\n\n\n')
        outcome = Prompt(prompt).send()

        return task, outcome

    
    def save(self, answear):
        file_path = self.search_path()
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write('\nRAG \nAnswear:\n'+answear)

    def search_path(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        QUESTIONS_PATH = os.path.join(BASE_DIR, 'questions')
        file_path = os.path.join(QUESTIONS_PATH, f'{self.file_name}.txt')
        return file_path
    
    def run(self):
        play = True
        while play:
            question, outcome = self.result()
            if 'RAG' in question:
                print(f'File {self.file_name} allready have answear for llama')
                break
            print(question,'\n\n',outcome)

            while True:
                action = input('Reject or Accept (r/a): ')
                if action == 'a':
                    print('Accept and save answear \n')
                    self.save(outcome)
                    play = False
                    break
                elif action == 'r':
                    print('Reject and not save answear\n')
                    break
                else:
                    print('Error. Try again')
    
    def run_test(self):
        question, outcome = self.result()
        print(question,'\n\n',outcome,'\n\n', '-'*50, '\n\n')
        return question, outcome



def CHROMA(fun):
    def new():
        generate = Run_chroma()
    return new

def run_RAG(fun):
    def new():
        for file_name in os.listdir(QUESTIONS_PATH):
            if not file_name.endswith('.txt'):
                continue
            base_name = os.path.splitext(file_name)[0]
            print(f'\nFile: {base_name}')

            rag_instance = rag(base_name)
            rag_instance.run()
            print('\n','-'*50,'\n')
            
        fun()
    return new