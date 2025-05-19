from LLAMA.send_prompt import Prompt
from values import prompt_few_shots, prompt_zero_shots, prompt_one_shots

import os

class llama():
    def __init__(self, file_name, prompt_technique=2):
        self.file_name = file_name
        self.prompt_technique=prompt_technique

    def result(self):
        file_path = self.search_path()
        with open(file_path, 'r', encoding='utf-8') as file:
            task = file.read()

        if self.prompt_technique == 0:
            outcome = Prompt(f'{prompt_zero_shots} \n\n {task}').send()
        elif self.prompt_technique == 1:
            outcome = Prompt(f'{prompt_one_shots} \n\n {task}').send()
        elif self.prompt_technique == 2:
            outcome = Prompt(f'{prompt_few_shots} \n\n {task}').send()
        else:
            return None, None
        return task, outcome
    
    def save(self, answear, addition = '\nLLAMA \nAnswear:\n', folder_name='questions'):
        file_path = self.search_path(folder_name)
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(addition + answear)

    def search_path(self, folder_name='questions'):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        QUESTIONS_PATH = os.path.join(BASE_DIR, folder_name)
        file_path = os.path.join(QUESTIONS_PATH, f'{self.file_name}.txt')
        return file_path
    
    def run(self):
        play = True
        while play:
            question, outcome = self.result()
            if 'LLAMA' in question:
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