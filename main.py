from action import Run

def main():
    while True:         
        try:        
            sentence = input('Enter sentence A: ')

            print('\n\n 1 - gemini \n 2 - llama \n 3 - openai \n')
            choice_llm = int(input('Select options: '))

            if choice_llm not in [1, 2, 3]:
                raise IndexError

            else:
                print('\n\n 0: zero-shot\n 1: one-shot\n 2: few-shot\n 3: self-consistency\n 4: chain-of-thought\n 5: ReAct\n 6: HyDE\n')
                choice_technique = int(input('Select the prompt technique: '))

                if choice_technique not in [0, 1, 2, 3, 4, 5, 6]:
                    raise IndexError
    
            action = Run(sentence, choice_llm, choice_technique)
            print(action.result())

        except ValueError:
            print(f'\n Wrong value \n')

        except IndexError:
            print(f'\n It is not a number \n')

if __name__ == '__main__':
    main()