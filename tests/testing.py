import os
import re
import sys
import csv
import time
import statistics

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LLAMA.ML_llama import llama


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


def normalize(text: str) -> str:
    return text.strip().lower().rstrip(".").replace("ów", "").replace("y", "").replace("i", "").replace("a", "")


def contradicts_a_o(sentence_a: str, sentence_o: str) -> bool:
    pattern_a = r"Wszystkie (.+?)(?:\.|$)"
    pattern_o = r"Niektóre (.+?) nie (.+?)(?:\.|$)"

    match_a = re.match(pattern_a, sentence_a.strip())
    match_o = re.match(pattern_o, sentence_o.strip())

    if match_a and match_o:
        a_full = normalize(match_a.group(1))
        subject_o = normalize(match_o.group(1))
        predicate_o = normalize(match_o.group(2))

        return a_full == f"{subject_o} {predicate_o}"
    
    return False


def contradicts_i_e(sentence_i: str, sentence_e: str) -> bool:
    pattern_i = r"Niektóre (.+?)(?:\.|$)"
    pattern_e = r"Żadne (.+?) nie (.+?)(?:\.|$)"

    match_i = re.match(pattern_i, sentence_i.strip())
    match_e = re.match(pattern_e, sentence_e.strip())

    if match_i and match_e:
        i_full = normalize(match_i.group(1))
        subject_e = normalize(match_e.group(1))
        predicate_e = normalize(match_e.group(2))

        return  i_full == f"{subject_e} {predicate_e}"

    return False


def save(file_name: str, data: str, index: str):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    QUESTIONS_PATH = os.path.join(BASE_DIR, 'result_test')
    
    if not os.path.exists(QUESTIONS_PATH):
        os.makedirs(QUESTIONS_PATH)

    file_path = os.path.join(QUESTIONS_PATH, f'{file_name}.txt')
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f'Approach {index}\n{data}\n\n')


def save_data_to_csv(report_file_name, question, number_of_attempts, format_success, relation_success, first_aproach_successful, average_time, min_time, max_time):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    QUESTIONS_PATH = os.path.join(BASE_DIR, 'tests')
    os.makedirs(QUESTIONS_PATH, exist_ok=True)
    file_path = os.path.join(QUESTIONS_PATH, f'{report_file_name}.csv')
    file_exists = os.path.isfile(file_path)

    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['Question', 'Attempts', 'Format Success', 'Relation Success', 'First Aproach Successful', 'Average Time', 'Min Time', 'Max Time'])

        writer.writerow([ question, number_of_attempts, format_success, relation_success, first_aproach_successful, f"{average_time:.3f}", f"{min_time:.3f}", f"{max_time:.3f}" ])



def main():
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
        n: int = 30
        times = []
        report_file_name="report_LLAMA"
        for i in range(n):
            llama_instance = llama(base_name)
            start_time = time.time()
            question, outcome = llama_instance.run_test()
            end_time = time.time()
            result_time = end_time - start_time
            times.append(result_time)

            try:
                test_response_format(outcome)
                format_success += 1
                if test_raltion_between_sentences(question, outcome):
                    relation_success += 1
                
                    if not first_aproach_successful:
                        first_aproach_successful += i+1
                    save(f'result_{base_name}', outcome, i+1)
            except AssertionError:
                pass
        
        average_time = statistics.mean(times)
        min_time = min(times)
        max_time = max(times)

        data: str = f"\n\nAttempts: {n} \nFormat success: {format_success} \nRelation success: {relation_success} \nFirst aproach successful: {first_aproach_successful}\n\n"
        line: str ='='*50
        print(line,data,line)
        save_data_to_csv(report_file_name, file_name[:-4], n, format_success, relation_success, first_aproach_successful, average_time, min_time, max_time)

if __name__ == '__main__':
    main()