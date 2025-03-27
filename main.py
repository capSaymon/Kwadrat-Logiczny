from ollama import chat
from ollama import ChatResponse

sentence: str = 'Samolot stoi na płycie lotniska'

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