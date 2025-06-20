import os

class LLM:
    def __init__(self, *, file_name: str = None, sentence: str = None, prompt_technique: int = 2, name = None):
        self.file_name = file_name
        self.sentence = sentence
        self.prompt_technique = prompt_technique
        self.name = name
    
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
