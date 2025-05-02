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