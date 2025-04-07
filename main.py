from backend.sentences import SentencesPrompt
import os

QUESTIONS_PATH = r'G:\Kwadrat Logiczny\Kwadrat-Logiczny\questions'

def main ():
    for file_name in os.listdir(QUESTIONS_PATH):
        if not file_name.endswith('.txt'):
            continue
        base_name = os.path.splitext(file_name)[0]
        print(f'\nFile: {base_name}')

        run = True
        while run:
            task = SentencesPrompt(base_name)
            question, outcome = task.send()
            if 'Answear:' in question:
                print(f'File {base_name} allready have answear')
                break
            print(question,'\n\n', outcome)

            while True:
                action = input('Reject or Accept (r/a): ')
                if action == 'a':
                    print('Accept and save answear \n')
                    task.save(outcome)
                    run = False
                    break
                elif action == 'r':
                    print('Reject and not save answear\n')
                    break
                else:
                    print('Error. Try again')
        print('\n','-'*50,'\n')


if __name__ == '__main__':
    main()