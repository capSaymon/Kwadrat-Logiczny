from action import Run

def main():      
    try:        
        sentence = input('Enter sentence A: ')
        sentence = 'A: '+sentence

        print('\n\n 1 - gemini \n 2 - llama \n 3 - openai \n')
        choice_llm = int(input('Select options: '))

        if choice_llm not in [1, 2, 3]:
            raise IndexError

        else:
            text: str = '\n\n 0: zero-shot\n 1: one-shot\n 2: few-shot\n 3: self-consistency\n 4: chain-of-thought\n 5: ReAct\n'
            if choice_llm == 2:
                print(text+' 6: HyDE\n')
            else:
                print(text)
            choice_technique = int(input('Select the prompt technique: '))

            valid_techniques = [0, 1, 2, 3, 4, 5]
            if choice_llm == 2:
                valid_techniques.append(6)

            if choice_technique not in valid_techniques:
                raise ValueError("Invalid prompt technique selected for the chosen LLM.")

        while True:
            action = Run(sentence, choice_llm, choice_technique)
            outcome = action.result()

            print()
            print('-'*50,'\n')
            print(f'{outcome}\n')
            print('-'*50,'\n')

            choice = input('Reject or Accept (r/a): ')
            if choice == 'a':
                print('Accept answear and save\n')
                action.save(outcome)
                break
            elif choice == 'r':
                print('Reject answear\n')
            else:
                print('Error. Try again\n')

    except ValueError as e:
        print(f'\n[Error] {e}\n')

    except IndexError:
        print(f'\n[Error] Input must be a valid number.\n')


if __name__ == '__main__':
    main()