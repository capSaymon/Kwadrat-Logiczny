# Kwadrat-Logiczny

Program wspomaga analizę logiczną poprzez generowanie zdań dla brakujących wierzchołków [kwadratu logicznego](https://pl.wikipedia.org/wiki/Kwadrat_logiczny). Wykorzystuje w tym celu technikę [few-shot prompting](https://www.promptingguide.ai/techniques/fewshot) z użyciem dużych modeli językowych (LLM).

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


***Środowisko LLM:***
- [Ollama](https://ollama.com/)

- [OpenAI](https://openai.com/)


***Modele LLM:***

- [llama3:1b](https://www.llama.com/llama-downloads/)

- [lama3:3b](https://www.llama.com/llama-downloads/)

- [gpt-3.5-turbo](https://platform.openai.com/docs/models)

***RAG***: Program może korzystać z techniki retrieval-augmented generation (RAG), która polega na wyszukiwaniu odpowiednich informacji w zbiorze danych przed generowaniem odpowiedzi. Wykorzystuje to w kontekście generowania brakujących wierzchołków kwadratu logicznego.

***Hyde***: Używana jest również technika Hyde, pozwalająca na ukrywanie złożonych detali implementacyjnych w celu uproszczenia interfejsu użytkownika i umożliwienia bardziej intuicyjnej interakcji z systemem.


LLM
---
W projekcie wykorzystywane są środowiska Ollama oraz OpenAI. Z OpenAI można korzystać, dodając swój klucz API w pliku **.env**, oraz odkomentowując dekorator, który umożliwia integrację z OpenAI. Domyślnie ustawione jest środowisko Llama. W plikach question przechowywane jest zdanie A, a wyniki promptu z danego modelu LLM można zapisać w plikach wynikowych.

