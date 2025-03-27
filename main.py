def main ():
    sentence: str = 'Każdy samolot stoi na płycie lotniska'

    prompt: str = f"""
    Dane wejściowe:  
    Zdanie: "{sentence}"  
    Zadanie: Podziel to zdanie na podmiot i predykt. 
    Wymagania:
    - Podaj podmiot w jednej linii i predykt w drugiej.
    - Podmiot: to osoba, rzecz lub zjawisko, o którym mówimy.
    - Predykat: to część zdania, która mówi coś o podmiocie.
    - Nie zmieniaj żadnych słów w zdaniu.
    """

if __name__ == '__main__':
    main()