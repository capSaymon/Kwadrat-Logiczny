from send_prompt import Prompt

class CategoricalSentences():
    def __init__(self, subject, prediction, rest):
        self.subject = subject
        self.prediction = prediction
        self.rest = rest

    def create(self) -> list[str]:
        SaP: str = f'Każdy {self.subject} jest {self.prediction} {self.rest}'
        SeP: str = f'Żaden {self.subject} nie jest {self.prediction} {self.rest}'
        SiP: str = f'Niektóre {self.subject} {self.prediction} {self.rest}'
        SoP: str = f'Niektóre {self.subject} nie {self.prediction} {self.rest}'
        sentences_list: list[str] = [SaP, SeP, SiP, SoP]
        result: str = ''

        for sentence in sentences_list:
            prompt: str = f"""
            Dane wejściowe:  
            Zdanie: "{sentence}"  
            Zadanie: Popraw gramatykę podanego zdania.  

            Wymagania:
            - Zdanie musi zawierać wyraźny predykat (orzeczenie): {self.prediction}
            - Jeśli zdanie jest poprawne, zwróć je bez zmian
            - Popraw błędy gramatyczne i składniowe, jeśli występują
            - Zachowaj znaczenie i styl oryginalnego zdania
            - Nie zmieniaj słów na niepowiązane synonimy ani nie dodawaj nowych treści
            - Możesz pominąć słowa: "jest", "nie jest" tylko wtedy, gdy ich usunięcie nie zmienia poprawności i jasności zdania
            - Możesz dodać słowo "są" jeżeli jest to konieczne 

            Oczekiwany format odpowiedzi:
            - Poprawione zdanie w tej samej strukturze, ale poprawne i naturalnie brzmiące
            """

            grammar = Prompt(prompt, sentence)
            corrected_grammar = grammar.send()
            result += corrected_grammar
            
        result_list: list[str] = result.split('.')
        result_list.pop(-1)
        return result_list