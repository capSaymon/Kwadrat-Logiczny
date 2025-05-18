import os
import re
import sys
import csv
import time
import spacy
import statistics

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LLAMA.ML_llama import llama
from OPENAI.ML_openai import gpt
from HyDE.RAG import rag
from GEMINI.ML_gemini import gemini


def test_response_format(response: str):    
    assert "E:" in response
    assert "I:" in response
    assert "O:" in response

    linie = response.splitlines()
    assert len(linie) == 4


def extract_sentence(response: str, apex: str) -> str:
    for line in response.splitlines():
        if f"{apex}:" in line:
            parts = line.split(":", 1)
            if len(parts) == 2:
                return parts[1].strip()
    raise ValueError(f"No sentence type found: {apex}")


def test_raltion_between_sentences(question: str, response: str) -> bool:
    apex_a = extract_sentence(question, "A")
    apex_o = extract_sentence(response, "O")
    apex_i = extract_sentence(response, "I")
    apex_e = extract_sentence(response, "E")

    return (contradicts_a_o(apex_a, apex_o) and contradicts_i_e(apex_i, apex_e))

nlp = spacy.load("pl_core_news_sm")

def lemmatize(text: str) -> str:
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc])

def normalize(text: str) -> str:
    return lemmatize(text.strip().lower().rstrip("."))


def contradicts_a_o(sentence_a: str, sentence_o: str) -> bool:
    pattern_a = r"Wszystkie (.+?)(?:\.|$)"
    pattern_o = r"Niektóre (.+?) nie (.+?)(?:\.|$)"

    match_a = re.match(pattern_a, sentence_a.strip())
    match_o = re.match(pattern_o, sentence_o.strip())

    if match_a and match_o:
        a_full = normalize(match_a.group(1))
        subject_o = normalize(match_o.group(1))
        predicate_o = normalize(match_o.group(2))

        return f"{subject_o} {predicate_o}" in a_full or a_full in f"{subject_o} {predicate_o}"

    return False


def contradicts_i_e(sentence_i: str, sentence_e: str) -> bool:
    pattern_i = r"Niektóre (.+?)(?:\.|$)"
    pattern_e = r"Żaden (.+?) nie (.+?)(?:\.|$)"

    match_i = re.match(pattern_i, sentence_i.strip())
    match_e = re.match(pattern_e, sentence_e.strip())

    if match_e is None:
        pattern_e = r"Żadne (.+?) nie (.+?)(?:\.|$)"
        match_e = re.match(pattern_e, sentence_e.strip())

    if match_i and match_e:
        i_full = normalize(match_i.group(1))
        subject_e = normalize(match_e.group(1))
        predicate_e = normalize(match_e.group(2))

        return f"{subject_e} {predicate_e}" in i_full or i_full in f"{subject_e} {predicate_e}"

    return False


def save(file_name: str, data: str, index: str, LLM: str =''):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    QUESTIONS_PATH = os.path.join(BASE_DIR, 'result_test')
    
    if not os.path.exists(QUESTIONS_PATH):
        os.makedirs(QUESTIONS_PATH)

    file_path = os.path.join(QUESTIONS_PATH, f'{file_name}.txt')
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f'{LLM}\nApproach {index}\n{data}\n\n')


def save_data_to_csv(report_file_name, question, number_of_attempts, format_success, relation_success, first_aproach_successful, average_time, min_time, max_time):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    QUESTIONS_PATH = os.path.join(BASE_DIR, 'reports')

    os.makedirs(QUESTIONS_PATH, exist_ok=True)
    file_path = os.path.join(QUESTIONS_PATH, f'{report_file_name}.csv')
    file_exists = os.path.isfile(file_path)

    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['Question', 'Attempts', 'Format Success', 'Relation Success', 'First Aproach Successful', 'Average Time', 'Min Time', 'Max Time'])

        writer.writerow([ question, number_of_attempts, format_success, relation_success, first_aproach_successful, f"{average_time:.3f}", f"{min_time:.3f}", f"{max_time:.3f}" ])



def run_LLAMA(base_name: str):
    llama_instance = llama(base_name)
    start_time = time.time()
    question, outcome = llama_instance.run_test()
    end_time = time.time()
    return question, outcome, end_time, start_time


def run_OPENAI(base_name: str):
    openai_instance = gpt(base_name)
    start_time = time.time()
    question, outcome = openai_instance.run_test()
    end_time = time.time()
    return question, outcome, end_time, start_time


def run_HyDE(base_name: str):
    rag_instance = rag(base_name)
    start_time = time.time()
    question, outcome = rag_instance.run_test()
    end_time = time.time()
    return question, outcome, end_time, start_time


def run_GEMINI(base_name: str):
    gemini_instance = gemini(base_name)
    start_time = time.time()
    question, outcome = gemini_instance.run_test()
    end_time = time.time()
    return question, outcome, end_time, start_time



def create_report(report_file_name: str):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    QUESTIONS_PATH = os.path.join(BASE_DIR, 'questions')

    if not os.path.isdir(QUESTIONS_PATH):
        print(f'Folder "questions" does not exist: {QUESTIONS_PATH}')
        return None

    
    for file_name in os.listdir(QUESTIONS_PATH):
        if not file_name.endswith('.txt'):
            continue
        base_name = os.path.splitext(file_name)[0]
        print(f'\nFile: {base_name}')

        format_success: int = 0
        relation_success: int = 0
        first_aproach_successful: int = 0
        n: int = 1
        times = []
        
        for i in range(n):
            if report_file_name == 'report_LLAMA':
                question, outcome, end_time, start_time = run_LLAMA(base_name)
            elif report_file_name == 'report_OPENAI':
                question, outcome, end_time, start_time = run_OPENAI(base_name)
            elif report_file_name == 'report_HyDE':
                question, outcome, end_time, start_time = run_HyDE(base_name)
            elif report_file_name == 'report_GEMINI':
                question, outcome, end_time, start_time = run_GEMINI(base_name)
            else:
                print('there is no such llm report name')

            result_time = end_time - start_time
            times.append(result_time)

            try:
                test_response_format(outcome)
                format_success += 1
                if test_raltion_between_sentences(question, outcome):
                    relation_success += 1
                
                    if not first_aproach_successful:
                        first_aproach_successful += i+1
                    save(f'result_{base_name}', outcome, i+1, report_file_name[7:])
            except AssertionError:
                pass
        
        average_time = statistics.mean(times)
        min_time = min(times)
        max_time = max(times)

        data: str = f"\n\nAttempts: {n} \nFormat success: {format_success} \nRelation success: {relation_success} \nFirst aproach successful: {first_aproach_successful}\n\n"
        line: str ='='*50
        print(line,data,line)
        save_data_to_csv(report_file_name, file_name[:-4], n, format_success, relation_success, first_aproach_successful, average_time, min_time, max_time)
