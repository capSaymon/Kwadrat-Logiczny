from backend.send_prompt import Prompt

class SentencesPrompt():
    def __init__(self, file_name):
        self.file_name = file_name

    def send(self):
        with open(f'G:\Kwadrat Logiczny\Kwadrat-Logiczny\prompts\{self.file_name}.txt', 'r', encoding='utf-8') as file:
            prompt = file.read()

        result = Prompt(prompt).send()

        with open(f'G:\Kwadrat Logiczny\Kwadrat-Logiczny\prompts\{self.file_name}.txt', 'a', encoding='utf-8') as file:
            file.write('\n\n\nAnswear: \n' + result + '\n')

        return prompt, result
        