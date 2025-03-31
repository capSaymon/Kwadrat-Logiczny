from backend.send_prompt import Prompt

class SubjectPrediction():
    def __init__(self, sentence):
        self.sentence = sentence
    
    def extract(self, mind):
        subject, prediction = '', ''

        for word in mind.split():
            if word == 'Podmiot:' or word == 'Predykt:':
                continue
            if not subject:
                subject += word
            else:
                prediction += word

        return subject, prediction

    def find(self):
        prompt: str = f"""
        Dane wejściowe:  
        Zdanie: "{self.sentence}"  
        Zadanie: Podziel to zdanie na podmiot i predykt
        Wymagania:
        - odpowiedzią nie jest {self.sentence}
        - wypisz tylko Podmiot oraz Predykt
        - Podmiot: to osoba, rzecz lub zjawisko, o którym mówimy
        - Predykt: to część zdania, która mówi coś o podmiocie o jego stanie
        - Podaj podmiot w jednej linii i predykt w drugiej
        - Nie zmieniaj żadnych słów w zdaniu
        """

        find_subject_and_prediction = Prompt(prompt, self.sentence)
        result_subject_and_prediction = find_subject_and_prediction.send()

        #return result_subject_and_prediction
        return self.extract(result_subject_and_prediction)