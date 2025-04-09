# Kwadrat-Logiczny

Program wspomaga analizę logiczną poprzez generowanie zdań dla brakujących wierzchołków [kwadratu logicznego](https://pl.wikipedia.org/wiki/Kwadrat_logiczny). Wykorzystuje w tym celu technikę [few-shot prompting](https://www.promptingguide.ai/techniques/fewshot) z użyciem dużych modeli językowych (LLM), uruchamianych lokalnie za pomocą Ollama.

Opis działania
---
Użytkownik wprowadza jedno zdanie, które stanowi punkt wyjściowy (lewy górny wierzchołek kwadratu). Na tej podstawie program formułuje prompt zawierający:

- schemat budowy wierzchołków kwadratu

- opis relacji logicznych między wierzchołkami kwadratu

- dwa przykłady zdań

Model językowy generuje brakujące wierzchołki kwadratu.


Technologia
---
***Język:*** [Python](https://www.python.org/)

***Środowisko LLM:*** [Ollama](https://ollama.com/)

***Modele LLM:***

- [llama3:1b](https://www.llama.com/llama-downloads/)

- [lama3:3b](https://www.llama.com/llama-downloads/)
