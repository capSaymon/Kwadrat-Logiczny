from subject_prediction import SubjectPrediction
from categorical_sentences import CategoricalSentences

def main ():
    sentence: str = 'Każdy samolot stoi na płycie lotniska'

    result_subject_and_prediction = SubjectPrediction(sentence)
    find_sub_pre = result_subject_and_prediction.find()
    subject, prediction = find_sub_pre

    subject, prediction = ('samolot', 'stoi')

    find_categorical_sentences = CategoricalSentences(subject, prediction)
    print(find_categorical_sentences.create())
    

if __name__ == '__main__':
    main()