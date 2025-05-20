#path to questions file
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_PATH = os.path.join(BASE_DIR, 'questions')

#few-shots prompt
prompt_few_shots: str = f"""
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

Przykład 1:
A: Wszystkie ptaki mają skrzydła.  
E: Żadne ptaki nie mają skrzydeł.  
I: Niektóre ptaki mają skrzydła.  
O: Niektóre ptaki nie mają skrzydeł.

Przykład 2:
A: Wszystkie komputery są podłączone do Internetu.  
E: Żaden komputer nie jest podłączony do Internetu.  
I: Niektóre komputery są podłączone do Internetu.  
O: Niektóre komputery nie są podłączone do Internetu.

Przykład 3:
A: Wszystkie samochody są elektryczne.  
E: Żadne samochody nie są elektryczne.  
I: Niektóre samochody są elektryczne.  
O: Niektóre samochody nie są elektryczne.

Przykład 4:
A: Wszystkie książki w bibliotece są nowe.  
E: Żadne książki w bibliotece nie są nowe.  
I: Niektóre książki w bibliotece są nowe.  
O: Niektóre książki w bibliotece nie są nowe.

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

#zero-shots prompt
prompt_zero_shots: str = f"""
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

### Wzór zdań

- A: Wszystkie X są Y
- E: Żadne X nie jest Y
- I: Niektóre X są Y
- O: Niektóre X nie są Y


### Zadanie

Na podstawie podanego zdania A wygeneruj pozostałe trzy zdania (E, I, O), stosując się do podanych zasad logiki kwadratu.  
Twoja odpowiedź **musi zawierać dokładnie cztery linijki**, w formacie:

A: [podane zdanie]  
E: ... 
I: ...  
O: ...

Nie dodawaj żadnych wyjaśnień, opisów ani komentarzy.
"""



#one-shots prompt
prompt_one_shots: str = f"""
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

Przykład 1:
A: Wszystkie ptaki mają skrzydła.  
E: Żadne ptaki nie mają skrzydeł.  
I: Niektóre ptaki mają skrzydła.  
O: Niektóre ptaki nie mają skrzydeł.

### Zadanie

Na podstawie podanego zdania A wygeneruj pozostałe trzy zdania (E, I, O), stosując się do podanych zasad logiki kwadratu.  
Twoja odpowiedź **musi zawierać dokładnie cztery linijki**, w formacie:

A: [podane zdanie]  
E: ... 
I: ...  
O: ...

Nie dodawaj żadnych wyjaśnień, opisów ani komentarzy.
"""






#chain-of-thought prompt
prompt_chain_of_thought = f"""
Zadanie: Na podstawie zdania A wygeneruj trzy inne zdania: E, I i O, zgodnie z logiką kwadratu.

Typy zdań:
- A: Wszystkie X są Y
- E: Żadne X nie jest Y
- I: Niektóre X są Y
- O: Niektóre X nie są Y

Zależności:
- A → I (implikacja)
- E → O (implikacja)
- A i E: przeciwieństwo
- A i O: sprzeczność
- E i I: sprzeczność
- I i O: podprzeciwieństwo

---

Zdanie A: "Wszystkie komputery są podłączone do internetu."

Pomyśl krok po kroku:

1. Jakie jest znaczenie zdania A?
- To zdanie mówi, że dla każdego obiektu, jeśli jest komputerem, to jest podłączony do internetu.

2. Jaka jest logiczna sprzeczność? (zdanie E)
- Zdanie E powinno zaprzeczać A. Czyli: istnieje przynajmniej jeden komputer, który nie jest podłączony do internetu.

3. Jakie jest zdanie szczegółowe zgodne? (zdanie I)
- Powinno stwierdzać istnienie przynajmniej jednego komputera, który jest podłączony do internetu.

4. Jakie jest zdanie szczegółowe sprzeczne? (zdanie O)
- Powinno stwierdzać istnienie przynajmniej jednego komputera, który nie jest podłączony do internetu.

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





#ReAct prompt
prompt_ReAct = f"""
#### Zadanie: Na podstawie zdania A wygeneruj trzy inne zdania: E, I i O, zgodnie z logiką kwadratu.

### Typy zdań:
- A: Wszystkie X są Y
- E: Żadne X nie jest Y
- I: Niektóre X są Y
- O: Niektóre X nie są Y


### Zależności:
- A → I (implikacja)
- E → O (implikacja)
- A i E: przeciwieństwo
- A i O: sprzeczność
- E i I: sprzeczność
- I i O: podprzeciwieństwo


### Proces:
Myślenie: Analizuję zależności między typami zdań.  
Działanie: Generuję zdania E, I, O zgodnie z zasadami logiki kwadratu.  
Obserwacja: Zdania zostały poprawnie utworzone.  
Odpowiedź: ...  

### Przykład:
A: Wszystkie ptaki mają skrzydła.  
E: Żadne ptaki nie mają skrzydeł.  
I: Niektóre ptaki mają skrzydła.  
O: Niektóre ptaki nie mają skrzydeł.  

### Zadanie

Na podstawie podanego zdania A wygeneruj pozostałe trzy zdania (E, I, O), stosując się do podanych zasad logiki kwadratu.  
Twoja odpowiedź **musi zawierać dokładnie cztery linijki**, w formacie:

A: [podane zdanie]  
E: ... 
I: ...  
O: ...

Nie dodawaj żadnych wyjaśnień, opisów ani komentarzy.
"""