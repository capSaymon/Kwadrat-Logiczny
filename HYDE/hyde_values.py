import os


#path to chroma file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_PATH = os.path.join(BASE_DIR, 'chroma')

#path to data file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'DATA')

#model path (download model)
MODEL_PATH: str = r"G:\Kwadrat Logiczny\nomic-embed-text-v1.5.Q5_K_M.gguf"

#prompt
PROMPT_SENTENCE: str = """
Kwadrat logiczny składa się z czterech zdań oznaczonych jako A, E, I, O:

- A: zdanie ogólno-twierdzące (np. „Wszystkie X są Y”)
- E: zdanie ogólno-przeczące (np. „Żadne X nie jest Y”)
- I: zdanie szczegółowo-twierdzące (np. „Niektóre X są Y”)
- O: zdanie szczegółowo-przeczące (np. „Niektóre X nie są Y”)

Relacje logiczne między zdaniami:

**Implikacja**:
- A → I (jeśli A jest prawdziwe, to I też)
- E → O (jeśli E jest prawdziwe, to O też)

**Przeciwieństwo**:
- A i E nie mogą być jednocześnie prawdziwe, ale mogą być fałszywe

**Sprzeczność**:
- A i O nie mogą być jednocześnie prawdziwe ani jednocześnie fałszywe
- E i I nie mogą być jednocześnie prawdziwe ani jednocześnie fałszywe

**Podprzeciwieństwo**:
- I i O nie mogą być jednocześnie fałszywe, ale mogą być prawdziwe

### Przykłady

{context}

### Zadanie

Na podstawie podanego zdania A wygeneruj pozostałe trzy zdania (E, I, O), stosując się do podanych zasad logiki kwadratu.  
Twoja odpowiedź **musi zawierać dokładnie cztery linijki**, w formacie:

A: [podane zdanie]  
E: ... 
I: ...  
O: ...

Nie dodawaj żadnych wyjaśnień, opisów ani komentarzy.

{question}
"""



#embed prompt
PROMPT_EMBED: str = f"""
Kwadrat logiczny składa się z czterech zdań oznaczonych jako A, E, I, O:

- A: zdanie ogólno-twierdzące (np. „Wszystkie X są Y”)
- E: zdanie ogólno-przeczące (np. „Żadne X nie jest Y”)
- I: zdanie szczegółowo-twierdzące (np. „Niektóre X są Y”)
- O: zdanie szczegółowo-przeczące (np. „Niektóre X nie są Y”)

Relacje logiczne między zdaniami:

**Implikacja**:
- A → I (jeśli A jest prawdziwe, to I też)
- E → O (jeśli E jest prawdziwe, to O też)

**Przeciwieństwo**:
- A i E nie mogą być jednocześnie prawdziwe, ale mogą być fałszywe

**Sprzeczność**:
- A i O nie mogą być jednocześnie prawdziwe ani jednocześnie fałszywe
- E i I nie mogą być jednocześnie prawdziwe ani jednocześnie fałszywe

**Podprzeciwieństwo**:
- I i O nie mogą być jednocześnie fałszywe, ale mogą być prawdziwe

---

### Zadanie

Na podstawie podanego zdania A wygeneruj pozostałe trzy zdania (E, I, O), stosując się do podanych zasad logiki kwadratu.  
Twoja odpowiedź **musi zawierać dokładnie cztery linijki**, w formacie:

A: [podane zdanie]  
E: ... 
I: ...  
O: ...

Nie dodawaj żadnych wyjaśnień, opisów ani komentarzy.
"""
