from backend.sentences import SentencesPrompt

def main ():
    task = SentencesPrompt('question_1')
    question, outcome = task.send()
    print(question, '\n-----------------------------------------------------------\n', outcome)    

if __name__ == '__main__':
    main()