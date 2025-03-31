from backend.subject_prediction import SubjectPrediction
from backend.categorical_sentences import CategoricalSentences

def main ():
    #sentence = input('Write sentence: ')
    sentence: str = 'Samolot stoi na płycie lotniska'
    print(f'{sentence} \n\n')

    result_subject_and_prediction = SubjectPrediction(sentence)
    while True:
        find_sub_pre = result_subject_and_prediction.find()
        subject, prediction = find_sub_pre
        subject = subject.lower()
        prediction = prediction.lower()
        if prediction in sentence.lower() and subject in sentence.lower():
            break

    prediction_index = sentence.find(prediction) + len(prediction) + 1
    rest: str = sentence[prediction_index:]

    find_categorical_sentences = CategoricalSentences(subject, prediction, rest)
    SaP, SeP, SiP, SoP = find_categorical_sentences.create()
    print(f'\n{SaP} \n{SeP} \n{SiP} \n{SoP} \n')

if __name__ == '__main__':
    main()