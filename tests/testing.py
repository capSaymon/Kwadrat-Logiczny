import os
import sys
import csv
import time
import statistics

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LLAMA.ML_llama import llama


def test_response_format(response):    
    assert "E:" in response
    assert "I:" in response
    assert "O:" in response


def save(file_name, data, index):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    QUESTIONS_PATH = os.path.join(BASE_DIR, 'result_test')
    
    if not os.path.exists(QUESTIONS_PATH):
        os.makedirs(QUESTIONS_PATH)

    file_path = os.path.join(QUESTIONS_PATH, f'{file_name}.txt')
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f'Approach {index}\n{data}\n\n')


def save_data_to_csv(report_file_name, question, number_of_attempts, format_success, average_time, min_time, max_time):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    QUESTIONS_PATH = os.path.join(BASE_DIR, 'tests')
    os.makedirs(QUESTIONS_PATH, exist_ok=True)
    file_path = os.path.join(QUESTIONS_PATH, f'{report_file_name}.csv')
    file_exists = os.path.isfile(file_path)

    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['Question', 'Attempts', 'Format Success', 'Average Time', 'Min Time', 'Max Time'])

        writer.writerow([ question, number_of_attempts, format_success, f"{average_time:.3f}", f"{min_time:.3f}", f"{max_time:.3f}" ])



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

        success: int = 0
        n: int = 10
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
                success += 1
            except AssertionError:
                pass

            save(f'result_{base_name}', outcome, i+1)
        
        average_time = statistics.mean(times)
        min_time = min(times)
        max_time = max(times)
        save_data_to_csv(report_file_name, file_name[:-4], n, success, average_time, min_time, max_time)

if __name__ == '__main__':
    main()