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
Odpowiedz na pytanie bazując na tych kontekstach:

{context}

Odpoweidz bazując na podanych kontekstach tego jedngo zdania: {question} Znajdź reszte zdań.
"""

#embed prompt
PROMPT_EMBED: str = f"""
        #Zadanie
        Teraz, rozwiąż ten kwadrat logiczny. Jest podane zdanie A podaj tylko reszte zdań i nic więcej.
        Nie opisuj. Utwórz kolejne zdania typu E, I oraz O. Bierz pod uwagę tylko te zasady:

        #wzór odpowiedzi:
        Zdanie A: treść...
        Zdanie E: treść...
        Zdanie I: treść...
        Zdanie O: treść...

        """

#SL description
SQUEARE_LOGIC: str = f"""
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

        """