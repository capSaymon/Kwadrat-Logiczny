from backend.information import InformationPrompt

def main ():
    information_prompt = InformationPrompt()
    result = information_prompt.send()
    print(result)

if __name__ == '__main__':
    main()