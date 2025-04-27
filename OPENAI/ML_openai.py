from OPENAI.send_prompt import Prompt
from values import prompt, QUESTIONS_PATH

import os

class gpt():
    def __init__(self, file_name):
        self.file_name = file_name

    def result(self):
        file_path = self.search_path()
        with open(file_path, 'r', encoding='utf-8') as file:
            task = file.read()
            
        outcome = Prompt(f'{prompt} \n\n {task}').send()
        return task, outcome
    
    def save(self, answear):
        file_path = self.search_path()
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write('\nOPENAI \nAnswear:\n'+answear)

    def search_path(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        QUESTIONS_PATH = os.path.join(BASE_DIR, 'questions')
        file_path = os.path.join(QUESTIONS_PATH, f'{self.file_name}.txt')
        return file_path
    
    def run(self):
        play = True
        while play:
            question, outcome = self.result()
            if 'OPENAI' in question:
                print(f'File {self.file_name} allready have answear for openai')
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

def run_gpt(fun):
    def new():
        fun()
        for file_name in os.listdir(QUESTIONS_PATH):
            if not file_name.endswith('.txt'):
                continue
            base_name = os.path.splitext(file_name)[0]
            print(f'\nFile: {base_name}')

            openai_instance = gpt(base_name)
            openai_instance.run()
            print('\n','-'*50,'\n')
    return new