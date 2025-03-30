from send_prompt import Prompt

def main ():
    sentence: str = 'Każdy samolot stoi na płycie lotniska'
    prompt: str = f"""
    Dane wejściowe:  
    Zdanie: "{sentence}"  
    Zadanie: Podziel to zdanie na podmiot i predykt
    Wymagania:
    - odpowiedzią nie jest {sentence}
    - wypisz tylko Podmiot oraz Predykt
    - Podmiot: to osoba, rzecz lub zjawisko, o którym mówimy
    - Predykt: to część zdania, która mówi coś o podmiocie o jego stanie
    - Podaj podmiot w jednej linii i predykt w drugiej
    - Nie zmieniaj żadnych słów w zdaniu
    """

    find_subject_and_prediction = Prompt(prompt, sentence)
    subject_and_prediction = find_subject_and_prediction.send()
    print(subject_and_prediction)

    


if __name__ == '__main__':
    main()