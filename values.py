#path to questions file
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_PATH = os.path.join(BASE_DIR, 'questions')

#few-shots prompt
prompt: str = f"""
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
