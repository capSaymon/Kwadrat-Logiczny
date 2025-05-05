#path to questions file
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_PATH = os.path.join(BASE_DIR, 'questions')

#few-shots prompt
prompt: str = f"""
        Kwadrat logiczny ma cztery wierzchołki oznaczone A, E, I oraz O

        - Wierzchołek A to zdanie ogólno-twierdzące (np. „Wszystkie X są Y”)
        - Wierzchołek E to zdanie ogólno-przeczące (np. „Żadne X nie jest Y”)
        - Wierzchołek I to zdanie szczegółowo-twierdzące (np. „Niektóre X są Y”)
        - Wierzchołek O to zdanie szczegółowo-przeczące (np. „Niektóre X nie są Y”)

        Między tymi wierzchołkami zachodzą relacje logiczne:
        
        Implikacja:  
        - A implikuje I jeśli A jest prawdziwe, to I jest prawdziwe
        - E implikuje O jeśli E jest prawdziwe, to O jest prawdziwe

        Przeciwieństwo:
        - A i E nie mogą być jednocześnie prawdziwe, ale mogą być jednocześnie fałszywe

        Sprzeczność: 
        - A i O nie mogą być jednocześnie prawdziwe ani jednocześnie fałszywe  
        - E i I nie mogą być jednocześnie prawdziwe ani jednocześnie fałszywe

        Podprzeciwieństwo: 
        - I i O nie mogą być jednocześnie fałszywe, ale mogą być jednocześnie prawdziwe
        
        
        #Przykłady

        Przykład 1:
        Zdanie A: Wszystkie ptaki mają skrzydła.
        Zdanie E: Żadne ptaki nie mają skrzydeł.
        Zdanie I: Niektóre ptaki mają skrzydła.
        Zdanie O: Niektóre ptaki nie mają skrzydeł.

        Przykład 2:
        Zdanie A: Wszystkie komputery są podłączone do Internetu.
        Zdanie E: Żaden komputer nie jest podłączony do Internetu.
        Zdanie I: Niektóre komputery są podłączone do Internetu.
        Zdanie O: Niektóre komputery nie są podłączone do Internetu.

        #Zadanie
        Teraz, rozwiąż ten kwadrat logiczny. Jest podane zdanie A podaj tylko reszte zdań i nic więcej. Nie opisuj. Bierz pod uwagę tylko te zasady:
        Przykład 3:
        
        """