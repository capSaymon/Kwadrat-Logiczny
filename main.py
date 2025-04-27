from LLAMA.ML_llama import llama
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_PATH = os.path.join(BASE_DIR, 'questions')

def main ():
    if not os.path.isdir(QUESTIONS_PATH):
        print(f'Folder "questions" nie istnieje w: {QUESTIONS_PATH}')
        return
    
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