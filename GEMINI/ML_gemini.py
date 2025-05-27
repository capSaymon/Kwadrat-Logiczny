from collections import Counter
from GEMINI.send_prompt import Prompt
from values import prompt_zero_shots, prompt_few_shots,prompt_one_shots, prompt_chain_of_thought, prompt_ReAct, QUESTIONS_PATH

import os

class gemini():
    def __init__(self, *, file_name: str = None, sentence: str = None, prompt_technique: int = 2):
        self.file_name = file_name
        self.sentence = sentence
        self.prompt_technique = prompt_technique

    def result(self):
        if self.file_name:
            file_path = self.search_path()
            with open(file_path, 'r', encoding='utf-8') as file:
                task = file.read()
        else:
            task = self.sentence

        if self.prompt_technique == 0:
            outcome = Prompt(f'{prompt_zero_shots} \n\n {task}').send()
        elif self.prompt_technique == 1:
            outcome = Prompt(f'{prompt_one_shots} \n\n {task}').send()
        elif self.prompt_technique == 2:
            outcome = Prompt(f'{prompt_few_shots} \n\n {task}').send()
        elif self.prompt_technique == 3:
            outcome = self.self_consistency(task)
        elif self.prompt_technique == 4:
            outcome = Prompt(f'{prompt_chain_of_thought} \n\n {task}').send()
        elif self.prompt_technique == 5:
            outcome = Prompt(f'{prompt_ReAct} \n\n {task}').send()

        if self.file_name:
            return task, outcome
        else:
            return outcome
    
    def save(self, answear, addition = '\nGEMINI \nAnswear:\n', folder_name='questions'):
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
            if self.file_name:
                question, outcome = self.result()
                if 'GEMINI' in question:
                    print(f'File {self.file_name} allready have answear for gemini')
                    break
                print(question,'\n\n',outcome)

            else:
                outcome = self.result()
                print(outcome)

            while True:
                action = input('Reject or Accept (r/a): ')
                if action == 'a':
                    if self.file_name:
                        print('Accept and save answear \n')
                        self.save(outcome)
                    else:
                        print('Accept answear \n')
                    play = False
                    break
                elif action == 'r':
                    print('Reject and not save answear\n')
                    break
                else:
                    print('Error. Try again')
                
    def self_consistency(self, task):
        prompt_results = []
        for _ in range(3):
            result = Prompt(f'{prompt_few_shots} \n\n {task}').send()
            prompt_results.append(result.strip())
        
        counts = Counter(prompt_results)
        most_common_result, _ = counts.most_common(1)[0]
        return most_common_result
                    
    def run_test(self):
        question, outcome = self.result()
        print(question,'\n\n',outcome,'\n\n', '-'*50, '\n\n')
        return question, outcome