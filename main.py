from backend.information import InformationPrompt
from backend.sentences import SentencesPrompt

def main ():
    information_prompt = InformationPrompt()
    result = information_prompt.send()
    #print(result, '\n\n')

    sentence = SentencesPrompt('question_1')
    question, outcome = sentence.send()
    print(question, '\n\n', outcome)

if __name__ == '__main__':
    main()