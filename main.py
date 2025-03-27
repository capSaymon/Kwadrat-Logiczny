from send_prompt import Prompt

def main ():
    sentence: str = 'Każdy samolot stoi na płycie lotniska'
    prompt: str = f"""
    Dane wejściowe:  
    Zdanie: "{sentence}"  
    Zadanie: Podziel to zdanie na podmiot i predykt. 
    Wymagania:
    - Podaj podmiot w jednej linii i predykt w drugiej.
    - Podmiot: to osoba, rzecz lub zjawisko, o którym mówimy.
    - Predykt: to część zdania, która mówi coś o podmiocie o jego stanie.
    - Nie zmieniaj żadnych słów w zdaniu.
    """

    subject_and_prediction = Prompt(prompt, sentence)
    print(subject_and_prediction.send())

if __name__ == '__main__':
    main()