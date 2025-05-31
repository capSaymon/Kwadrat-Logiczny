from schemat import LLM
from collections import Counter
from LLAMA.send_prompt import Prompt
from values import prompt_zero_shots, prompt_one_shots, prompt_few_shots, prompt_chain_of_thought, prompt_ReAct, domain_prompt, domain_text

class llama(LLM):
    def __init__(self, *, file_name: str = None, sentence: str = None, prompt_technique: int = 2, name = 'LLAMA'):
        super().__init__(file_name=file_name, sentence=sentence, prompt_technique=prompt_technique, name=name)

    def result(self):
        if self.file_name:
            file_path = self.search_path()
            with open(file_path, 'r', encoding='utf-8') as file:
                task = file.read()
        else:
            task = self.sentence

        domain = f'{domain_text}{self.create_domain(task)}\n---\n'

        if self.prompt_technique == 0:
            outcome = Prompt(f'{domain + prompt_zero_shots} \n\n {task}').send()
        elif self.prompt_technique == 1:
            outcome = Prompt(f'{domain + prompt_one_shots} \n\n {task}').send()
        elif self.prompt_technique == 2:
            outcome = Prompt(f'{domain + prompt_few_shots} \n\n {task}').send()
        elif self.prompt_technique == 3:
            outcome = self.self_consistency(task, domain)
        elif self.prompt_technique == 4:
            outcome = Prompt(f'{domain + prompt_chain_of_thought} \n\n {task}').send()
        elif self.prompt_technique == 5:
            outcome = Prompt(f'{domain + prompt_ReAct} \n\n {task}').send()
        
        if self.file_name:
            return task, outcome
        else:
            return outcome
        
    def create_domain(self, task):
        return Prompt(f'{domain_prompt} \n\n {task}').send()
        
    def self_consistency(self, task, domain):
        prompt_results = []
        for _ in range(5):
            result = Prompt(f'{domain + prompt_few_shots} \n\n {task}').send()
            prompt_results.append(result.strip())
        
        counts = Counter(prompt_results)
        most_common_result, _ = counts.most_common(1)[0]
        return most_common_result