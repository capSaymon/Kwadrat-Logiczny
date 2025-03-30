from subject_prediction import SubjectPrediction
from categorical_sentences import CategoricalSentences

def main ():
    sentence: str = 'Każdy samolot stoi na płycie lotniska'

    result_subject_and_prediction = SubjectPrediction(sentence)
    print(result_subject_and_prediction.find())

    find_categorical_sentences = CategoricalSentences(result_subject_and_prediction)
    print(find_categorical_sentences.create())
    

if __name__ == '__main__':
    main()