from subject_prediction import SubjectPrediction
from categorical_sentences import CategoricalSentences

def main ():
    sentence: str = 'Każdy samolot stoi na płycie lotniska'
    #sentence: str = 'Każdy telefon leży na stole'

    result_subject_and_prediction = SubjectPrediction(sentence)
    while True:
        find_sub_pre = result_subject_and_prediction.find()
        subject, prediction = find_sub_pre
        if prediction in sentence and subject in sentence:
            break

    prediction_index = sentence.find(prediction) + len(prediction) + 1
    rest: str = sentence[prediction_index:]

    find_categorical_sentences = CategoricalSentences(subject, prediction, rest)
    result = find_categorical_sentences.create()
    SaP, SeP, SiP, SoP = result
    print(SaP)
    print(SeP)
    print(SiP)
    print(SoP)
    print()

if __name__ == '__main__':
    main()