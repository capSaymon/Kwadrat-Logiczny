from send_prompt import Prompt

class CategoricalSentences():
    def __init__(self, subject, prediction):
        self.subject = subject
        self.prediction = prediction

    def create(self) -> str:
        SaP: str = f'Każdy {self.subject} jest {self.prediction}'
        SeP: str = f'Żaden {self.subject} nie jest {self.prediction}'
        SiP: str = f'Niektóre {self.subject} są {self.prediction}'
        SoP: str = f'Niektóre {self.subject} nie są {self.prediction}'
        sentences_list: list[str] = [SaP, SeP, SiP, SoP]
        result: str = ''

        for sentence in sentences_list:
            prompt: str = f"""
            Dane wejściowe:  
            Zdanie: "{sentence}"  
            Zadanie: Popraw gramatykę podanego zdania.  
            Wymagania:
            - Jeśli zdanie jest poprawne, zwróć je bez zmian
            - Popraw błędy gramatyczne i składniowe, jeśli występują
            - Zachowaj znaczenie i styl oryginalnego zdania
            - Nie zmieniaj słów na niepowiązane synonimy ani nie dodawaj nowych treści
            """
            grammar = Prompt(prompt, sentence)
            corrected_grammar = grammar.send()
            result += corrected_grammar + ', '

        return result