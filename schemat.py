import os

class LLM:
    def __init__(self, *, file_name: str = None, sentence: str = None, prompt_technique: int = 2, name = None):
        self.file_name = file_name
        self.sentence = sentence
        self.prompt_technique = prompt_technique
        self.name = name
    
    def save(self, answear, folder_name='questions'):
        addition = f'\n{self.name} \nAnswear:\n'
        file_path = self.search_path(folder_name)
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(addition + answear)

    def search_path(self, folder_name='questions'):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        QUESTIONS_PATH = os.path.join(BASE_DIR, folder_name)
        file_path = os.path.join(QUESTIONS_PATH, f'{self.file_name}.txt')
        return file_path
    
    def result(self):
        pass
    
    def run(self):
        if self.file_name:
            question, outcome = self.result()
            if self.name in question:
                print(f'File {self.file_name} allready have answear for {self.name}')
            else:
                return question, outcome
            
        else:
            outcome = self.result()
            return outcome
    
    def run_test(self):
        question, outcome = self.result()
        print(question,'\n\n',outcome,'\n\n', '-'*50, '\n\n')
        return question, outcome