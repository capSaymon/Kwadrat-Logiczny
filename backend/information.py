from backend.send_prompt import Prompt

class InformationPrompt():
    def __init__(self):
        pass

    def send(self):
        prompt: str = f"""
        Kwadrat logiczny ma cztery wierzchołki oznaczone A, E, I oraz O.

        - Wierzchołek A to zdanie ogólno-twierdzące (np. „Wszystkie X są Y”).
        - Wierzchołek E to zdanie ogólno-przeczące (np. „Żadne X nie jest Y”).
        - Wierzchołek I to zdanie szczegółowo-twierdzące (np. „Niektóre X są Y”).
        - Wierzchołek O to zdanie szczegółowo-przeczące (np. „Niektóre X nie są Y”).

        Między tymi wierzchołkami zachodzą relacje logiczne:
        
        - Implikacja:  
        - A implikuje I  
        - E implikuje O  

        - Przeciwieństwo:
        - A i E nie mogą być jednocześnie prawdziwe, ale mogą być jednocześnie fałszywe

        - Sprzeczność: 
        - A i O nie mogą być jednocześnie prawdziwe ani jednocześnie fałszywe  
        - E i I - analogicznie

        - Podprzeciwieństwo: 
        - I i O nie mogą być jednocześnie fałszywe, ale mogą być jednocześnie prawdziwe
        """

        result = Prompt(prompt).send()
        return result
