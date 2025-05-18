import os

from LLAMA.ML_llama import llama
from OPENAI.ML_openai import run_gpt
from values import QUESTIONS_PATH
from HyDE.RAG import CHROMA, run_RAG
from GEMINI.ML_gemini import run_gemini


#@CHROMA
#@run_RAG
#@run_gemini
#@run_gpt
def main ():
    if not os.path.isdir(QUESTIONS_PATH):
        print(f'Folder "questions" does not exist: {QUESTIONS_PATH}')
        return None
    
    for file_name in os.listdir(QUESTIONS_PATH):
        if not file_name.endswith('.txt'):
            continue
        base_name = os.path.splitext(file_name)[0]
        print(f'\nFile: {base_name}')

        llama_instance = llama(base_name)
        llama_instance.run()
        print('\n','-'*50,'\n')

if __name__ == '__main__':
    main()