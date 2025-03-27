from ollama import chat
from ollama import ChatResponse

sentence: str = 'Każdy samolot stoi na płycie lotniska'

"""prompt: str = f""
Dane wejściowe:  
Zdanie: "{sentence}"  
Zadanie: Podziel to zdanie na podmiot i predykt. 
Wymagania:
- Podaj podmiot w jednej linii i predykt w drugiej.
- Podmiot: to osoba, rzecz lub zjawisko, o którym mówimy.
- Predykat: to część zdania, która mówi coś o podmiocie.
- Nie zmieniaj żadnych słów w zdaniu.
""

response: ChatResponse = chat(model='llama3.2:3b', messages=[{
    'role': 'user',
    'content': prompt,
}])

x = response.message.content
print(x)"""


x = 'podmiot: Samolot predykt: stoi na płycie'



prompt: str = f"""
Dane wejściowe:  
Dane: "{x}"  
Zadanie: Otrzymane dane to podmiot i predykt skonstruj dla nich 4 zdania kategoryczne związane z kwadratem logicznym. 
Wymagania:
- Podaj zdanie w osobnych liniach, bez cyf czy pauz.
- Nie zmieniaj podmiotu i predyktu, chyba że zależy to od gramatyki.
- Nie dodawaj nie potrzebnych zdan poza tymi 4 zdaniami
"""

response: ChatResponse = chat(model='llama3.2:1b', messages=[{
    'role': 'user',
    'content': prompt,
}])

x = response.message.content
print(x)




"""subject = ''
prediction = ''

save: bool = False

for x in response.message.content.split():
    if x.lower() == 'podmiot:' and not subject:
        subject += ' '
        continue
    elif x.lower() == 'predykat:' or x.lower() == 'predykt:':
        prediction += ' '
        continue

    if subject and not prediction:
        subject += x + ' '
    elif prediction:
        prediction += x + ' '

subject = subject[1:]
prediction = prediction[1:]

print(subject)
print(prediction)

SaP: str = f'Każdy {subject} jest {prediction}'
SeP: str = f'Żadne {subject} nie jest {prediction}'
SiP: str = f'Niektóre {subject} są {prediction}'
SoP: str = f'Niektóre {subject} nie są {prediction}'

def check(opinion) -> str:
    prompt: str = f""
    Dane wejściowe:  
    Zdanie: "{opinion}"  
    Zadanie: Sprawdź poprawność gramatyczną zdania.
    Wymagania:
    - pisz w jednej linijce odpowiedź
    - popraw tylko słowa nie dodawaj nowych
    - nie dodawaj nic od siebie
    - ilość słów w odpowiedzi nie może być ani mniej ani więcej niż w pierwotnym zdaniu
    - podawaj pełne zdania
    - jeżeli gramatyka jest dobrze zrobiona nie zmieniaj nic
    - Skup się tylko na poprawności gramatycznej, nie dodawaj nowych słów ani nie zmieniaj struktury.
    - Jeśli jest błąd, popraw tylko słowo, które wymaga zmiany.
    - Odpowiedz w jednej linijce.
    - Odpowiedzi nie dawaj w cudzysłowach
    - Nie przekraczaj ilości słów zdania
    - Nie zmieniaj słów na całkiem inne
    ""

    response: ChatResponse = chat(model='llama3.2:1b', messages=[{
        'role': 'user',
        'content': prompt,
    }])
    return response.message.content

# Poprawiona część kodu
print(check(SaP))
print(check(SeP))
print(check(SiP))
print(check(SoP))

# Poprawienie formatu wejścia dla modelu
sentences = f"{SaP}, {SoP}, {SeP}, {SiP}"

prompt: str = f""
Dane wejściowe:  
Zdania: "{sentences}"  
Zadanie: Sprawdź poprawność według zasad zdań kategorycznych, zwróć "True" lub "False"
Warunki:
- określ czy jest poprawne czy nie
- odpowiedz to "True" lub "False"
- nie dodawaj nic więcej 
- zwraca wartosc bool
""

response: ChatResponse = chat(model='llama3.2:1b', messages=[{
    'role': 'user',
    'content': prompt,
}])

print(response.message.content)
"""