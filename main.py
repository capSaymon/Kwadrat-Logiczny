from ollama import chat
from ollama import ChatResponse

sentence: str = 'Każdy samolot stoi na płycie lotniska'

prompt: str = f"""
Dane wejściowe:  
Zdanie: "{sentence}"  
Zadanie: Podziel zdanie na podmiot i predykt. 
Wymagania:
- zawsze w 2 linijkach rozpisz odpowiedź
- napisz w odpowiedzi podmiot: oraz predykt: 
- nic nie zmieniaj
- odpowiedzi to słowa nie zmienione z podanego zdania
"""

response: ChatResponse = chat(model='llama3.2:1b', messages=[
  {
    'role': 'user',
    'content': prompt,
  },
])

subject = ''
prediction = ''

save: bool = False

for x in response.message.content.split():
    if x.lower() == 'podmiot:' and not subject:
        subject += ' '
        continue
    elif x.lower() == 'predykt:' or x.lower() == 'predyk:':
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

    prompt: str = f"""
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
    - Nie zmieniaj słów na całkiem inne słowa
    """

    response: ChatResponse = chat(model='llama3.2:1b', messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])
    return response.message.content

print()
print(check(SaP))
print(check(SeP))
print(check(SiP))
print(check(SoP))