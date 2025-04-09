# Kwadrat-Logiczny

Program wspomaga analizę logiczną poprzez generowanie zdań dla brakujących wierzchołków kwadratu logicznego. Wykorzystuje w tym celu technikę few-shot prompting z użyciem dużych modeli językowych (LLM), uruchamianych lokalnie za pomocą Ollama.

Opis działania
---
Użytkownik wprowadza jedno zdanie, które stanowi punkt wyjściowy (lewy górny wierzchołek kwadratu). Na tej podstawie program formułuje prompt zawierający:

- schemat budowy wierzchołków kwadratu

- opis relacji logicznych między wierzchołkami kwadratu

- dwa przykłady zdań

Model językowy generuje brakujące wierzchołki kwadratu.


Technologia
---
***Język:*** Python

***Środowisko LLM:*** Ollama

***Modele LLM:***

- llama3:1b

- lama3:3b
