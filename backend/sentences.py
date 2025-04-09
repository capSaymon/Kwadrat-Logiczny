from backend.send_prompt import Prompt

class SentencesPrompt():
    def __init__(self, file_name):
        self.file_name = file_name

    def send(self):
        #few-shot
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
        Teraz, rozwiąż ten kwadrat logiczny. Jest podane zdanie A podaj tylko reszte zdań i nic więcej. Bierz pod uwagę tylko te zasady:
        Przykład 3:
        
        """

        with open(f'G:\Kwadrat Logiczny\Kwadrat-Logiczny\questions\{self.file_name}.txt', 'r', encoding='utf-8') as file:
            task = file.read()

        result = Prompt(f'{prompt} \n\n {task}').send()
        return task, result
    
    def save(self, answear):
        with open(f'G:\Kwadrat Logiczny\Kwadrat-Logiczny\questions\{self.file_name}.txt', 'a', encoding='utf-8') as file:
            file.write('\nAnswear:\n'+answear)