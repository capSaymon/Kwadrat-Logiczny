# Kwadrat-Logiczny

Program wspomaga analizę logiczną poprzez generowanie zdań dla brakujących wierzchołków [kwadratu logicznego](https://pl.wikipedia.org/wiki/Kwadrat_logiczny). Stosowane są rózne techniki promptowania do pracy z dużymi modelami językowymi (LLM).

Opis działania
---
Użytkownik wprowadza jedno zdanie (ręcznie lub poprzez plik .txt), które stanowi punkt wyjściowy – lewy górny wierzchołek kwadratu logicznego (zdanie typu A). Następnie wybierana jest technika promptowania..

Na podstawie tego zdania program generuje odpowiedni prompt zawierający:

- Dziedzinę, z której pochodzi zdanie

- Schemat konstrukcyjny czterech wierzchołków kwadratu

- Opis relacji logicznych między wierzchołkami (np. sprzeczność, przeciwieństwo, kontrarność, kontradyktoryczność)

Wybrany model językowy generuje brakujące wierzchołki (E, I, O). W zależności od zastosowanej techniki promptowania, struktura promptu może się różnić, ale powyższe elementy są wspólne dla wszystkich wariantów.

Techniki promptingu
---
Wykorzystuje nowoczesne techniki promptowania, takie jak:

- [zero-shot](https://www.promptingguide.ai/techniques/zeroshot)
  
- [one-shot](https://www.ibm.com/think/topics/one-shot-prompting)
  
- [few-shot](https://www.promptingguide.ai/techniques/fewshot)
  
- [chain-of-thought](https://www.promptingguide.ai/techniques/cot)
  
- [ReAct](https://www.promptingguide.ai/techniques/react)
  
- [HyDE](https://medium.com/data-science/how-to-use-hyde-for-better-llm-rag-retrieval-a0aa5d0e23e8) + [RAG](https://www.promptingguide.ai/techniques/rag) 

Technologia
---
***Język:*** [Python](https://www.python.org/)


***Środowisko LLM:***
- [Ollama](https://ollama.com/)

- [Gemini](https://gemini.google.com/?hl=pl)

- [OpenAI](https://openai.com/)


***Modele LLM:***

- [llama3:3b](https://www.llama.com/llama-downloads/)

- [gemini-1.5-flash](https://ai.google.dev/competition/projects/multimodal-gemini-15-flash-api?hl=pl)

- [gpt-3.5-turbo](https://platform.openai.com/docs/models)


Konfiguracja i pliki
---
- Klucze API dla OpenAI i Gemini należy dodać do pliku .env.

- Zdania wejściowe (A) zapisuje się w plikach tekstowych w folderze questions/.

- Wyniki działania modeli można zapisać w folderze results/.

Instalacja zależności
---
Instalacja bibliotek z LLM:
```bash
pip install ollama llama-cpp-python google-genai openai
```
Reszta:
```bash
pip install python-dotenv langchain langchain-community chromadb pandas matplotlib numpy fpdf spacy
```
Model językowy dla języka polskiego:
```bash
python -m spacy download pl_core_news_sm
```

Należy jeszcze pobrać model osadzeń tekstowych [nomic-embed-text-v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF) w formacie GGUF. Następnie trzeba podać ścieżkę do tego pliku w module **hyde_values.py**.